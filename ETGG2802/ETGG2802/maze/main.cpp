
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
#include "World.h"


void APIENTRY debugcallback( GLenum source, GLenum typ,
        GLuint id_, GLenum severity, GLsizei length,
        const GLchar* message, const void* obj ){
    cout << message << "\n";
    if( source != GL_DEBUG_SOURCE_SHADER_COMPILER && severity == GL_DEBUG_SEVERITY_HIGH )
        throw runtime_error("Encountered very bad GL error. Stopping.");
}

int main(int argc, char* argv[])
{
	cout << "STARTING\n";

    //initialize SDL
    SDL_Init(SDL_INIT_VIDEO);
    
    //Bring up a window at 20,20 with size 512x512
    SDL_Window* win = SDL_CreateWindow( 
        "ETGG",
        20,20, 
        512,512, 
        SDL_WINDOW_OPENGL);
    
    if(!win)
        throw runtime_error("Could not create window");

    //Request GL context for the window
    SDL_GL_SetAttribute(SDL_GL_CONTEXT_PROFILE_MASK, SDL_GL_CONTEXT_PROFILE_CORE);
    SDL_GL_SetAttribute(SDL_GL_DEPTH_SIZE, 24);
    SDL_GL_SetAttribute(SDL_GL_STENCIL_SIZE, 8);
    SDL_GL_SetAttribute(SDL_GL_CONTEXT_MAJOR_VERSION,3);
    SDL_GL_SetAttribute(SDL_GL_CONTEXT_MINOR_VERSION,3);
    SDL_GL_SetAttribute(SDL_GL_CONTEXT_FLAGS,SDL_GL_CONTEXT_DEBUG_FLAG);
    SDL_GL_SetAttribute(SDL_GL_CONTEXT_PROFILE_MASK, SDL_GL_CONTEXT_PROFILE_CORE);
    SDL_GLContext rc = SDL_GL_CreateContext(win);
    if(!rc)
        throw runtime_error( "Cannot create GL context" );
           
    //tell GL we want debugging messages
    glDebugMessageControl(GL_DONT_CARE,GL_DONT_CARE,GL_DONT_CARE, 0, NULL, 1 );
    glEnable(GL_DEBUG_OUTPUT_SYNCHRONOUS);
    glDebugMessageCallback(debugcallback,NULL);

    //initialize the audio subsystem
    Mix_Init(MIX_INIT_OGG);
    Mix_OpenAudio( MIX_DEFAULT_FREQUENCY, MIX_DEFAULT_FORMAT, 2, 1024 );
    Mix_AllocateChannels(16);
    Mix_Chunk* pew = Mix_LoadWAV("pew.ogg");

    
    World* world = new World();
    
    //shaders
    Program* prog = new Program("vs.txt","fs.txt");

    //view camera
    Camera* cam = new Camera();
    cam->look_at(vec3(5,1,5), vec3(10,1,10), vec3(0,1,0) );

    //tells which keys are currently down
    set<int> keys;
    
    //for timing
    int last=SDL_GetTicks();
    SDL_Event ev;

    SDL_SetRelativeMouseMode(SDL_TRUE);

    glClearColor(0.2f,0.4f,0.6f,1.0f);
    glEnable(GL_DEPTH_TEST);

    while(1){
        
        //pump the event queue...
        while(1){
            if(!SDL_PollEvent(&ev)){
                break;
            }
        
            if(ev.type == SDL_QUIT){
                exit(0);
            } else if( ev.type == SDL_KEYDOWN ){
                int k = ev.key.keysym.sym;
                keys.insert(k);
                if(k == SDLK_q){
                    exit(0);
                }
            } else if(ev.type == SDL_KEYUP){
                int k = ev.key.keysym.sym;
                keys.erase(k);
            } else if( ev.type == SDL_MOUSEBUTTONDOWN ){
                cout << "Pew!\n";
                //-1=any channel, 0=no repeat
                Mix_PlayChannel(-1,pew,0);
            } else if(ev.type == SDL_MOUSEBUTTONUP){
                //mouse up,ev.button.button,ev.button.x,ev.button.y
            } else if( ev.type == SDL_MOUSEMOTION ){
                float dx = (float)ev.motion.xrel;
                cam->turn(-0.01f*dx);
            }
        }
        
        int now = SDL_GetTicks();
        float elapsed = (float)(now-last);
        last=now;
        
        if(keys.find(SDLK_w) != keys.end() )
            cam->walk(0.01f*elapsed);
        if(keys.find(SDLK_s) != keys.end() )
            cam->walk(-0.01f*elapsed);
        if(keys.find(SDLK_j) != keys.end() )
            cam->turn(0.001f*elapsed);
        if(keys.find(SDLK_l) != keys.end() )
            cam->turn(-0.001f*elapsed);
        if(keys.find(SDLK_a) != keys.end() )
            cam->strafe(-0.01f*elapsed,0,0);
        if(keys.find(SDLK_d) != keys.end() )
            cam->strafe(0.01f*elapsed,0,0);
        if(keys.find(SDLK_i) != keys.end() )
            cam->strafe(0,0.01f*elapsed,0);
        if(keys.find(SDLK_k) != keys.end() )
            cam->strafe(0,-0.01f*elapsed,0);
            
            
        prog->use();
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
        cam->draw(prog);
        prog->setUniform("lightPos",cam->eye.xyz());
        world->draw(prog);
        
        SDL_GL_SwapWindow(win);
    } //endwhile
    
    return 0;
}

//static's are defined here
Program* Program::active=NULL;
Mesh* Robot::mesh=NULL;
