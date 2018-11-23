#include <stdafx.h>
#include <application.h>
#include <game_object.h>
#include <game_object_manager.h>
#include <gui_manager.h>

// The template-specialization to declare the singleton variable for the Application class
template<> ssuge::Application* ssuge::Singleton<ssuge::Application>::msSingleton = NULL;


ssuge::Application::Application()  : OgreBites::ApplicationContext("ssuge", false), mLogManager(NULL), mGameObjectManager(NULL), mScriptManager(NULL), 
																			 mSoundManager(NULL), mInputManager(NULL)
{
	
}


ssuge::Application::~Application()
{
	// We'll do most of our clean-up in shutdown
}



void ssuge::Application::setup()
{
	// do not forget to call the base first
	OgreBites::ApplicationContext::setup();

	// The reason I create the input manager here (rather than with our other managers below)
	// is because when the window is created, a resize-event is sent to our application.  The input
	// manager needs to intercept this and call some OgreBites::ApplicationContext functions.
	mInputManager = new InputManager(mSDLWindow, "..\\bindings.txt");

	// get a pointer to some already-created objects and create a scene manager
	mRoot = getRoot();
	mSceneManager = mRoot->createSceneManager(Ogre::ST_GENERIC);

	
	mWindow = getRenderWindow();

	// register our scene with the RTSS
	Ogre::RTShader::ShaderGenerator* shadergen = Ogre::RTShader::ShaderGenerator::getSingletonPtr();
	shadergen->addSceneManager(mSceneManager);

	// Create a light source (this will change once we have a LightComponent)
	Ogre::Light* light = mSceneManager->createLight("MainLight");
	Ogre::SceneNode* lightNode = mSceneManager->getRootSceneNode()->createChildSceneNode();
	lightNode->setPosition(0, 50, 0);
	lightNode->attachObject(light);

	// This will also change once we have a CameraComponent
	Ogre::SceneNode* camNode = mSceneManager->getRootSceneNode()->createChildSceneNode();
	camNode->setPosition(0, 100, 65);
	camNode->lookAt(Ogre::Vector3(0, 0, 0), Ogre::Node::TS_PARENT);
	Ogre::Camera* cam = mSceneManager->createCamera("myCam");
	cam->setNearClipDistance(0.1f);
	cam->setFarClipDistance(1000.0f);
	cam->setAutoAspectRatio(true);
	camNode->attachObject(cam);
	mWindow->addViewport(cam);



	int width = mWindow->getViewport(0)->getActualWidth();
	int height = mWindow->getViewport(0)->getActualHeight();
	// Setup shadows
	mSceneManager->setShadowTechnique(Ogre::SHADOWTYPE_STENCIL_MODULATIVE);
	mSceneManager->setAmbientLight(Ogre::ColourValue(0.3f, 0.3f, 0.3f));


	// Set up the overlay system
	//mOverlaySystem = new Ogre::OverlaySystem();
	mSceneManager->addRenderQueueListener(getOverlaySystem());

	// Create our "managers"
	mLogManager = new LogManager("ssuge.log", 25);
	mScriptManager = new ScriptManager();
	mGameObjectManager = new GameObjectManager();
	mSoundManager = new SoundManager();
	mGuiManager = new GuiManager();
	mCollisionManager = new CollisionManager();
	
	// Miscellaneous setup
	//createDebugPanel();
	//std::string output = "width: " + std::to_string(width) + " , Height: " + std::to_string(height);
	//LOG_MANAGER->log(output);
	// Load our setup python script
	SCRIPT_MANAGER->loadScript("..\\Media\\init.py");
}


void ssuge::Application::shutdown()
{
	// Do any cleanup of our objects
	// (empty for now)

	// Delete our managers
	if (mInputManager)
		delete mInputManager;
	if (mSoundManager)
		delete mSoundManager;
	if (mGameObjectManager)
		delete mGameObjectManager;
	if (mScriptManager)
		delete mScriptManager;
	if (mLogManager)
		delete mLogManager;
	if (mGuiManager)
		delete mGuiManager;
	if (mCollisionManager)
		delete mCollisionManager;

	// Let the ApplicationContext do its thing
	OgreBites::ApplicationContext::shutdown();
}


/*bool ssuge::Application::keyPressed(const OgreBites::KeyboardEvent & evt)
{

	switch (evt.keysym.sym)
	{
	case SDLK_ESCAPE:
		getRoot()->queueEndRendering();
		return false;
	case SDLK_F11:
		if (mDebugOverlay)
		{
			if (mDebugOverlay->isVisible())
				mDebugOverlay->hide();
			else
				mDebugOverlay->show();
		}
		break;
	default:
		LOG_MANAGER->log("Keypress: " + std::to_string(evt.keysym.sym), 3.0f);
		break;
	}

	return true;
}*/


bool ssuge::Application::frameStarted(const Ogre::FrameEvent & evt)
{
	// I *don't* want to do this anymore.  We're making our InputManager in charge of processing
	// SDL events, not OgreBites.
	//if (!ApplicationContext::frameStarted(evt))
	//	return false;

	// Update the stats panel
	float spacing = 16.0f;
	/*if (mDebugOverlay && mDebugOverlay->isVisible())
	{
		Ogre::OverlayManager * mgr = Ogre::OverlayManager::getSingletonPtr();
		Ogre::TextAreaOverlayElement * text = (Ogre::TextAreaOverlayElement*)mgr->getOverlayElement("DebugStatsGUI\\Text0");
		text->setCaption("Average FPS: " + std::to_string(mWindow->getAverageFPS()));
		text->setPosition(mgr->getViewportWidth() - 200.0f, 0.0f);

		text = (Ogre::TextAreaOverlayElement*)mgr->getOverlayElement("DebugStatsGUI\\Text1");
		text->setCharHeight(spacing);
		text->setCaption("Triangle Count: " + std::to_string(mWindow->getTriangleCount()));
		text->setPosition(mgr->getViewportWidth() - 200.0f, spacing);
		text->setCharHeight(spacing);
	}*/
	LOG_MANAGER->update(evt.timeSinceLastFrame);

	// Update the GOM, which will in turn update all game objects
	GAME_OBJECT_MANAGER->update(evt.timeSinceLastFrame);

	COLLISION_MANAGER->sphereCollisions();

	//SOUND_MANAGER->update(evt.timeSinceLastFrame);
	// Update the Input manager, which will process all input.  This method will return false
	// if the window was closed or true if it wasn't.
	return INPUT_MANAGER->update();
}



void ssuge::Application::createDebugPanel()
{
	Ogre::OverlayManager * mgr = Ogre::OverlayManager::getSingletonPtr();
	mDebugOverlay = mgr->create("DebugStatsGUI");

	// Create a panel to hold all text elements
	Ogre::OverlayContainer * panel = (Ogre::OverlayContainer*)(mgr->createOverlayElement("Panel", "DebugStatsGUI\\Panel"));
	mDebugOverlay->add2D(panel);

	// Create the text elements
	for (unsigned int i = 0; i < 2; i++)
	{
		Ogre::TextAreaOverlayElement * text = (Ogre::TextAreaOverlayElement*)mgr->createOverlayElement("TextArea", "DebugStatsGUI\\Text" + std::to_string(i));
		text->setMetricsMode(Ogre::GMM_PIXELS);
		text->setFontName("SdkTrays/Value");
		text->setColourBottom(Ogre::ColourValue(1.0f, 0.4f, 0.4f));
		text->setColourTop(Ogre::ColourValue(1.0f, 1.0f, 1.0f));
		panel->addChild(text);
	}

	// Show the overlay
	mDebugOverlay->show();
}



void ssuge::Application::resizeWindow(int w, int h)
{
	mWindow->resize(w, h);
	windowResized(mWindow);
}



void ssuge::Application::startShutdown()
{
	//closeApp();
	getRoot()->queueEndRendering();
	//ApplicationContext::shutdown();
}