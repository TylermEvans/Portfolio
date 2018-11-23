#pragma once

#include <stdafx.h>
#include <game_object.h>
#include <log_manager.h>
#include <script_manager.h>
#include <singleton.h>
#include <sound_manager.h>
#include <input_manager.h>
#include <gui_manager.h>
#include <collision_manager.h>

#define APPLICATION ssuge::Application::getSingletonPtr()

// Reference: https://ogrecave.github.io/ogre/api/1.10/setup.html#skeleton


namespace ssuge
{
	/** The Application is our manager-of-managers in ssuge.  It will set up ogre and all managers
		when an instance is created.  It is a singleton so we can access the getter methods easily 
		from elsewhere. */
	class Application : public OgreBites::ApplicationContext, public Singleton<Application>
	{
	// @@@@@@ ATTRIBUTES @@@@@
	protected:
		/// The Ogre root.  Contains and manages all other ogre objects
		Ogre::Root * mRoot;

		/// The Ogre render window.  Put here for convenience (you can always access it from the root)
		Ogre::RenderWindow * mWindow;

		/// The Ogre render system (DX11, GL3, etc.)
		Ogre::RenderSystem * mRenderSystem;

		/// The Ogre scene manager (used to create lights, cameras, entities, etc) and manages the scene hierarchy
		Ogre::SceneManager * mSceneManager;

		/// The debug overlay -- used to show stats.  Updated by the application's update mehtod
		Ogre::Overlay * mDebugOverlay;

		/// The log manager -- used to write data to a log file and to display messages in an on-screen "console"
		LogManager * mLogManager;

		/// The GOM -- used to manage all instances of game objects (and to organize them into groups)
		GameObjectManager * mGameObjectManager;

		/// Our embedded python script manager
		ScriptManager * mScriptManager;

		/// The 3d sound manager
		SoundManager * mSoundManager;

		/// The input manager
		InputManager * mInputManager;

		GuiManager * mGuiManager;
		
		CollisionManager * mCollisionManager;

		//double mDeltaTimeAccum;

	// @@@@@ METHODS OVERRIDEN from Ogre::Bites::ApplicationContext -- none of these are meant to be called directly @@@@@
	protected:
		/// Our callback used to set up everything (all managers, the scene, etc.)
		void setup() override;

		/// Our callback used to shut down everything (de-allocate everything)
		void shutdown() override;

		/// Our callback used to update the scene (called before rendering) -- we update all our managers and stats panel here.
		bool frameStarted(const Ogre::FrameEvent & evt) override;

	// @@@@@ Other METHODS @@@@@
	protected:
		/// Sets up the debug stats panel.
		void createDebugPanel();

	public:
		/// Resizes the window (called by the input manager most likely)
		void resizeWindow(int w, int h);

		/// Initiates the shutdown procedure
		void startShutdown();

	// @@@@@ GETTERS @@@@@
	public:
		/// Gets the scene manager
		Ogre::SceneManager * getSceneManager() { return mSceneManager; }

		/// Gets a viewport (viewport #0 is the main window, and is guaranteed to be there -- we need more infrastructure to support more viewports)
		Ogre::Viewport * getViewport(int num) { return mWindow->getViewport(num); }
		

	// @@@@@ CONSTRUCTORS / DESTRUCTORS @@@@@
	public:
		/// Constructor
		Application();

		/// Destructor
		~Application();
	};

}
