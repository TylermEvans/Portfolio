
#include "glfuncs.h"

#include <vector>
#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <set>
#include <map>
#include <stdexcept>
#include <cassert>
#include <stdlib.h>
#include <ciso646>
#include <typeinfo>
#define _USE_MATH_DEFINES
#include <cmath>
#include <iostream>

using namespace std;

#include <SDL.h>
#include "SDL_mixer.h"
#include "Program.h"
#include "math3d.h"
#include "ImageTexture.h"
#include "Camera.h"
#include "Collision.h"
#include "World.h"
#include "Bullet.h"
#include "Square.h"
#include "Cube.h"
#include "ImageCubeTexture.h"
#include "FrameBuffer.h"
#include "SolidTexture.h"
#include "Mesh.h"



void APIENTRY debugcallback(GLenum source, GLenum typ,
	GLuint id_, GLenum severity, GLsizei length,
	const GLchar* message, const void* obj) {
	cout << message << "\n";
	if (source != GL_DEBUG_SOURCE_SHADER_COMPILER && severity == GL_DEBUG_SEVERITY_HIGH)
		throw runtime_error("Encountered very bad GL error. Stopping.");
}

void compute_blur_coefficients(vector<float>& coefficients, int r, bool box)
{

	coefficients.resize(2 * r + 1);

	if (box) {
		for (unsigned i = 0; i<coefficients.size(); ++i)
			coefficients[i] = 1.0 / coefficients.size();
	}
	else {
		float sigma = r / 3.0;
		for (unsigned i = 0; i<coefficients.size(); ++i) {
			float tmp = -r + i*1.0 / (coefficients.size() - 1) * 2 * r;
			tmp = tmp*tmp;
			tmp = tmp / (-2.0*sigma*sigma);
			tmp = exp(tmp);
			tmp = tmp / (sigma * sqrt(2 * 3.14159265358979323));
			coefficients[i] = tmp;
		}
		float sum = 0;
		for (unsigned i = 0; i<coefficients.size(); ++i)
			sum += coefficients[i];
		for (unsigned i = 0; i<coefficients.size(); ++i)
			coefficients[i] /= sum;
	}

	coefficients.resize(49);

}




int main(int argc, char* argv[])
{
	cout << "STARTING\n";

	//initialize SDL
	SDL_Init(SDL_INIT_VIDEO);

	//Bring up a window at 20,20 with size 512x512
	SDL_Window* win = SDL_CreateWindow(
		"ETGG",
		20, 20,
		1028, 1028,
		SDL_WINDOW_OPENGL);

	if (!win)
		throw runtime_error("Could not create window");

	//Request GL context for the window
	SDL_GL_SetAttribute(SDL_GL_CONTEXT_PROFILE_MASK, SDL_GL_CONTEXT_PROFILE_CORE);
	SDL_GL_SetAttribute(SDL_GL_DEPTH_SIZE, 24);
	SDL_GL_SetAttribute(SDL_GL_STENCIL_SIZE, 8);
	SDL_GL_SetAttribute(SDL_GL_CONTEXT_MAJOR_VERSION, 3);
	SDL_GL_SetAttribute(SDL_GL_CONTEXT_MINOR_VERSION, 3);
	SDL_GL_SetAttribute(SDL_GL_CONTEXT_FLAGS, SDL_GL_CONTEXT_DEBUG_FLAG);
	SDL_GL_SetAttribute(SDL_GL_CONTEXT_PROFILE_MASK, SDL_GL_CONTEXT_PROFILE_CORE);
	SDL_GLContext rc = SDL_GL_CreateContext(win);
	if (!rc)
		throw runtime_error("Cannot create GL context");

	//tell GL we want debugging messages
	glDebugMessageControl(GL_DONT_CARE, GL_DONT_CARE, GL_DONT_CARE, 0, NULL, 1);
	glEnable(GL_DEBUG_OUTPUT_SYNCHRONOUS);
	glDebugMessageCallback(debugcallback, NULL);

	//initialize the audio subsystem
	Mix_Init(MIX_INIT_OGG);
	Mix_OpenAudio(MIX_DEFAULT_FREQUENCY, MIX_DEFAULT_FORMAT, 2, 1024);
	Mix_AllocateChannels(16);
	Mix_Chunk* pew = Mix_LoadWAV("peew.ogg");


	World* world = new World();

	//shaders
	Program* prog = new Program("vs.txt", "fs.txt", { "color" });
	Program* bbprog = new Program("bbvs.txt", "bbfs.txt", { "color" });
	Program* skyprog = new Program("skyvs.txt", "skyfs.txt", { "color" });
	Program* postprocprog = new Program("ppvs.txt", "ppfs.txt", { "color" });
	Program* blurmachine = new Program("ppvs.txt", "blurmachine.txt", { "color" });
	Program* robotprog = new Program("vsrobot.txt", "fsrobot.txt", { "color" });
	Program* shadowprog = new Program("shadowvs.txt", "shadowfs.txt", { "color" });
	

	Square* usq = new Square();

	//view camera
	vec3 lightpos = vec3(5, 25, 5);
	Camera* cam = new Camera();
	Camera* cam2electricboogaloo = new Camera();
	
	cam2electricboogaloo->look_at(lightpos , vec3(3, 0, 0), vec3(0, 1, 0));
	vec3 hitheryon = vec3(cam2electricboogaloo->hither, cam2electricboogaloo->yon, cam2electricboogaloo->yon - cam2electricboogaloo->hither);

	cam->look_at(vec3(-2, 1, 0), vec3(0, 1, 0), vec3(0, 1, 0));

	//FBO
	Framebuffer2D* fbo1 = new Framebuffer2D(512, 512);
	Framebuffer2D* fbo2 = new Framebuffer2D(512, 512);
	Framebuffer2D* fbo3 = new Framebuffer2D(512, 512);
	Framebuffer2D* shadowbuffer = new Framebuffer2D(2048, 2048,3,GL_RGBA32F,GL_FLOAT);
	
	//tells which keys are currently down
	set<int> keys;

	//for timing
	int last = SDL_GetTicks();
	SDL_Event ev;
	int time = SDL_GetTicks();

	SDL_SetRelativeMouseMode(SDL_TRUE);

	glClearColor(0.2f, 0.4f, 0.6f, 1.0f);
	glEnable(GL_DEPTH_TEST);
	glDepthFunc(GL_LEQUAL);
	//bullet_list
    vector<Bullet*> b_list;
	vector<vec3> robotpos;
	//skyboxcube
	Cube* skycube = new Cube();
	vector<string> files = { "s3px.png","s3nx.png","s3py.png","s3ny.png","s3pz.png","s3nz.png" };
	//cubetex
	ImageCubeTexture* text = new ImageCubeTexture({ "right.png", "left.png", "top.png", "bottom.png", "front.png", "back.png" });
	//dummytex
	Texture* dummytex = new SolidTexture(0,0,0,1);
	glEnable(GL_BLEND);
	glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
	glBlendEquation(GL_FUNC_ADD);

	//gaussian blur calc
	vector<float> coefficients;
	int blur_radius = 15;
	bool boxblur = false;
	compute_blur_coefficients(coefficients, blur_radius, boxblur);
	bool firing = false;



	


	int mode = 1;
	
	float currentframe = 0;

	while (1) {

		//pump the event queue...
		while (1) {
			if (!SDL_PollEvent(&ev)) {
				break;
			}

			if (ev.type == SDL_QUIT) {
				exit(0);
			}
			else if (ev.type == SDL_KEYDOWN) {
				int k = ev.key.keysym.sym;
				keys.insert(k);
				if (k == SDLK_q) {
					exit(0);
				}
				if (k == SDLK_1) {
					mode = 1;
				}
				if (k == SDLK_0) {
					mode = 0;
				}
				if (k == SDLK_t) {
					lightpos += vec3(0, 0, 1);
					cam2electricboogaloo->look_at(lightpos, vec3(3, 0, 0), vec3(0, 1, 0));
					
				}
				if (k == SDLK_g) {
					lightpos += vec3(0, 0, -1);
					cam2electricboogaloo->look_at(lightpos, vec3(3, 0, 0), vec3(0, 1, 0));
				}
				if (k == SDLK_h) {
					lightpos += vec3(1, 0, 0);
					cam2electricboogaloo->look_at(lightpos, vec3(3, 0, 0), vec3(0, 1, 0));
				}
				if (k == SDLK_f) {
					lightpos += vec3(-1, 0, 0);
					cam2electricboogaloo->look_at(lightpos, vec3(3, 0, 0), vec3(0, 1, 0));
				}
				if (k == SDLK_r) {
					lightpos += vec3(0, -1, 0);
					cam2electricboogaloo->look_at(lightpos, vec3(3, 0, 0), vec3(0, 1, 0));
				}
				if (k == SDLK_y) {
					lightpos += vec3(0, 1, 0);
					cam2electricboogaloo->look_at(lightpos, vec3(3, 0, 0), vec3(0, 1, 0));
				}
				

			}
			else if (ev.type == SDL_KEYUP) {
				int k = ev.key.keysym.sym;
				keys.erase(k);
			}
			else if (ev.type == SDL_MOUSEBUTTONDOWN) {
				//-1=any channel, 0=no repeat
				Mix_PlayChannel(-1, pew, 0);
				firing = true;
			}
			else if (ev.type == SDL_MOUSEBUTTONUP) {
				firing = false;
				//mouse up,ev.button.button,ev.button.x,ev.button.y
			}
			else if (ev.type == SDL_MOUSEMOTION) {
				float dx = (float)ev.motion.xrel;
				cam->turn(-0.01f*dx);
				
			}
		}

		int now = SDL_GetTicks();
		float elapsed = (float)(now - last);
		last = now;
		if (firing == true && time<SDL_GetTicks()-200) 
		{
			b_list.push_back(new Bullet(cam->eye, cam->U, cam->V, 1));
			time = SDL_GetTicks();


		}
		// wall collision
		if (keys.find(SDLK_w) != keys.end()) 
		{
			float px = cam->eye.x;
			float pz = cam->eye.z;
			cam->walk(0.01f*elapsed);
			if (cam->eye.y < 5 && cam->eye.y > -5 && collision(cam->eye.x, cam->eye.z, world->cubepos) == true)
			{
				cam->eye.x = px;
				cam->eye.z = pz;
			}
			cam->compute_view_matrix();
		}
		//wall collision
		if (keys.find(SDLK_s) != keys.end()) 
		{
			float px = cam->eye.x;
			float pz = cam->eye.z;
			cam->walk(-0.01f*elapsed);
			if (cam->eye.y < 5 && cam->eye.y > -5 && collision(cam->eye.x, cam->eye.z, world->cubepos) == true)
			{
				cam->eye.x = px;
				cam->eye.z = pz;
			}
			cam->compute_view_matrix();
		}

		if (keys.find(SDLK_j) != keys.end())
			cam->turn(0.001f*elapsed);

		if (keys.find(SDLK_l) != keys.end())
			cam->turn(-0.001f*elapsed);
		//wall collision
		if (keys.find(SDLK_a) != keys.end()) 
		{
			float px = cam->eye.x;
			float pz = cam->eye.z;
			cam->strafe(-0.01f*elapsed, 0, 0);
			if (cam->eye.y < 5 && cam->eye.y > -5 && collision(cam->eye.x, cam->eye.z, world->cubepos) == true)
			{
				cam->eye.x = px;
				cam->eye.z = pz;
			}
			cam->compute_view_matrix();
		}
		// wall collision
		if (keys.find(SDLK_d) != keys.end())
		{
			float px = cam->eye.x;
			float pz = cam->eye.z;
			cam->strafe(0.01f*elapsed, 0, 0);
			if (cam->eye.y < 5 && cam->eye.y > -5 && collision(cam->eye.x, cam->eye.z, world->cubepos) == true)
			{
				cam->eye.x = px;
				cam->eye.z = pz;
			}
			cam->compute_view_matrix();
		}

		if (keys.find(SDLK_i) != keys.end())
			cam->strafe(0, 0.01f*elapsed, 0);

		if (keys.find(SDLK_k) != keys.end())
			cam->strafe(0, -0.01f*elapsed, 0);
		// Bullet-wall collision
		for (int i = 0; i < b_list.size(); i++)
		{
			b_list[i]->update(elapsed);
			if (b_list[i]->life == 0) 
			{
				b_list.erase(b_list.begin() + i);
			}
		}

		//hit detection robot-bullet
		for (int i = 0; i < b_list.size(); i++)
		{
			for (int k = 0; k < world->robots.size(); k++)
			{
				vec3 tmp = world->robots[k]->pos - b_list[i]->pos;
				float dist = dot(tmp, tmp);
				if (dist < pow((b_list[i]->radius + world->robots[k]->rad), 1)) 
				{	

					cout << "hit" << endl;
					world->robots.erase(world->robots.begin() + k);
					b_list[i]->life = 0;
					break;

				}
			}
		}

		//Bullet life removal
		for (int i = 0; i < b_list.size(); i++) 
		{
			if (collision(b_list[i]->pos.x, b_list[i]->pos.z, world->cubepos) == true)
			{
				b_list[i]->life = 0;
			}
		}
		for (int i = 0; i < world->robots.size(); i++) 
		{
			robotpos.push_back(world->robots[i]->pos);

		}

		//robot movement
		world->update(elapsed, cam->eye, world->cubepos);
		cam->gunupdate(firing);







		//Normal Draw
		
		

		shadowbuffer->bind();
		shadowprog->use();
		cam2electricboogaloo->draw(shadowprog);
		shadowprog->setUniform("hitheryon", hitheryon);
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
		world->draw(shadowprog);
		world->robotdraw(shadowprog);
		shadowbuffer->unbind();

		






		fbo1->bind();
		prog->use();
		if (mode == 1) {
			prog->setUniform("mode", 1.0);
		}
		else {
			prog->setUniform("mode", 0.0);
		}
		cam->draw(prog);
		prog->setUniform("lightPos", lightpos);
		

		prog->setUniform("roughness", 32);
		prog->setUniform("eyePos", cam->eye.xyz());
		prog->setUniform("shadowbuffer", shadowbuffer->texture);
		prog->setUniform("hitheryon", hitheryon);
		prog->setUniform("lightviewmat", cam2electricboogaloo->viewmatrix);
		prog->setUniform("lightprojmat", cam2electricboogaloo->projmatrix);
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
		world->draw(prog);
		

		robotprog->use();
		if (mode == 1) {
			robotprog->setUniform("mode", 1.0);
		}
		else {
			robotprog->setUniform("mode", 0.0);
		}
		cam->draw(robotprog);
		robotprog->setUniform("lightPos", lightpos);
		robotprog->setUniform("roughness", 32);
		robotprog->setUniform("eyePos", cam->eye.xyz());
		robotprog->setUniform("shadowbuffer", shadowbuffer->texture);
		robotprog->setUniform("hitheryon", hitheryon);
		robotprog->setUniform("lightviewmat", cam2electricboogaloo->viewmatrix);
		robotprog->setUniform("lightprojmat", cam2electricboogaloo->projmatrix);	
		cam->gundraw(robotprog);
		world->robotdraw(robotprog);
		shadowbuffer->texture->unbind();
		//Bullet Draw
		bbprog->use();
		cam->draw(bbprog);
		for (int i = 0; i < b_list.size(); i++)
		{
			b_list[i]->draw(bbprog);

		}

		skyprog->use();
		cam->draw(skyprog);
		skyprog->setUniform("eyepos", cam->eye);
		skyprog->setUniform("worldMatrix", scaling(100, 100, 100));
		skycube->draw(skyprog);

		//...draw scene...
		fbo1->unbind();

		fbo2->bind();
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
		//blurring
		postprocprog->use();
		postprocprog->setUniform("tex", fbo1->texture);
		postprocprog->setUniform("blur_kernel[0]", coefficients);
		postprocprog->setUniform("kernel_size", int(2 * blur_radius + 1)); //(int)coefficients.size());
		postprocprog->setUniform("blur_radius", (float)blur_radius); //(int)coefficients.size());
		postprocprog->setUniform("deltas", vec2(1, 0));
		usq->draw(postprocprog);
		fbo2->unbind();
		postprocprog->setUniform("tex", fbo2->texture);
		postprocprog->setUniform("deltas", vec2(0, 1));
		//blurr2
		fbo3->bind();
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
		usq->draw(postprocprog);
		fbo3->unbind();


		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
		blurmachine->use();
		blurmachine->setUniform("blurred", fbo3->texture);
		blurmachine->setUniform("unblurred", fbo1->texture);
		blurmachine->setUniform("depthtexture", fbo1->depthtexture);
		float P = 1.0f + 2.0f*cam->yon / (cam->hither - cam->yon);
		float Q = 2.0f*cam->hither*cam->yon / (cam->hither - cam->yon);
		blurmachine->setUniform("P", P);
		blurmachine->setUniform("Q", Q);
		blurmachine->setUniform("focaldistance", 10.0);
		usq->draw(blurmachine);
		blurmachine->setUniform("blurred", dummytex);
		blurmachine->setUniform("unblurred", dummytex);
		blurmachine->setUniform("depthtexture", dummytex);
		SDL_GL_SwapWindow(win);

	} //endwhile

	return 0;

}

//static's are defined here
Program* Program::active = NULL;
Mesh* Robot::mesh = NULL;
//Mesh* Camera::gun = NULL;
RenderTarget* RenderTarget::active_target;
Texture* Texture::active_textures[128];
int RenderTarget::saved_viewport[4];


