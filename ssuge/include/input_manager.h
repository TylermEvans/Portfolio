#pragma once
#include <stdafx.h>
#include <singleton.h>

#define INPUT_MANAGER ssuge::InputManager::getSingletonPtr()

namespace ssuge
{
	/// The InputManager is responsible for processing (SDL) input and notifying interested
	/// listeners of those events.  It also support device-polling functions.
	class InputManager : public Singleton<InputManager>
	{
	// @@@@@ NESTED CLASSES @@@@@
	public:
		/// This is an "interface" class for any object that wants to observe input-related events
		class Listener
		{
		public:
			/// Called by the InputManager when an action (button, key, etc.) is pressed.
			virtual void onAction(std::string action_name, bool is_starting) {}

			/// Called by the InputManager when an axis changes state.
			virtual void onAxis(std::string name, unsigned int num, float new_val) {}

			/// Called by the InputManager when a touch-device moves.  Currently only mouse (device = 0) is supported
			virtual void onTouch(unsigned int device, int x, int y, int xrel, int yrel) {}
		};


	protected:
		struct AxisBinding
		{
			std::string mAxisName;		// The axis this binds to (e.g. "horizontal")
			unsigned int mAxisNum;		// The axis number this binds to (e.g. 0 for "horizontal")
			float mValue;				// for keypresses indicates the value to set the axis to
										// for gamepads, it's a multiplier (useful for inverting y-axis)
		};


	// @@@@@ ATTRIBUTES @@@@@
	protected:
		/// A pointer to the SDL Window (which was created by the application)
		SDL_Window * mWindow;

		/// The first joystick controller (NULL if none are present)
		SDL_Joystick * mGamepad;

		/// The list of listening game objects
		std::vector<Listener*> mListeners;

		/// The current axis values
		std::map<std::pair<std::string, unsigned int>, float> mAxisValues;

		/// The current action values (I'm using an int as multiple devices may map to this action (e.g. space bar on keyboard
		/// and a button on gamepad#1) -- each time an event starts that action, increase this by one, when it releases, decrease it by
		/// one.  We consider the action "active" if the count is greater than 0)
		std::map<std::string, int> mActionValues;

		/// The current keyboard AXIS bindings
		std::map<SDL_Keycode, AxisBinding> mKeyboardAxisBindings;

		/// The current keyboard ACTION bindings
		std::map<SDL_Keycode, std::string> mKeyboardActionBindings;

		/// The current gamepad button ACTION bindings (Note: the axes are automatically mapped)
		std::map<unsigned char, std::string> mGamepadActionBindings;

		/// The current gamepad dpad ACTION bindings (the keys are 1, 2, 4, 8 for up, right, down, left)
		std::map<unsigned char, std::string> mGamepadDPadBindings;

		/// The multiplier to use for gamepad axes (if any)
		std::map<std::pair<std::string, unsigned int>, float> mGamepadAxisMultiplier;

		/// Current mouse-button ACTION bindings (for normal buttons)
		std::map<unsigned int, std::string> mMouseButtonBindings;

		/// Current mouse-button ACTION bindings (for scroll wheel -- this should just have two entries
		///    -1 (for towards user) and +1 (for away from user)).  Note: Wheel events do trigger a script
		/// callback, but do not affect the action count.
		std::map<int, std::string> mMouseWheelBindings;

		/// The current mouse readings: the first two numbers is the mouse's absolute position (in pixels);
		/// The second two numbers are the relative readings (also in pixels)
		int mMouseData[4];

		/// The current dhat value.  And with 0x01 to get up-state, 0x02 right-state, 0x04 down-state, 0x08 left-state
		unsigned char mGamepadDPadData;
	


	// @@@@@ CONSTRUCTOR / DESTRUCTOR @@@@@ 
	public:
		/// The constructor
		InputManager(SDL_Window * win);

		/// The constructor which also loads a bindings file
		InputManager(SDL_Window * win, std::string binding_fname);

		/// The destructor
		~InputManager();

	// @@@@@ METHODS @@@@@ 
	public:
		/// Process all waiting events, notify listeners.  Return false if the close button was pressed
		bool update();

		/// Returns the value of this axis (-1...+1), or returns 0.0 if that axis doesn't exist.
		float getAxis(std::string name, unsigned int num);

		/// Registers a game object as a listener
		void registerListener(Listener * g);

		/// Removes a game object listener (no effect if g is not a listener)
		void unregisterListener(Listener * g);

		/// Returns true if this action name is valid or not
		bool isActionValid(std::string name);

		/// Returns the current state of an action (true = pressed, false = not); raises an exception if name is invalid
		bool getActionState(std::string name);

		/// Returns the current mouse position (expressed as a relative value: (0.0, 0.0) = upper-left, (1.0,1.0) = lower-right
		Ogre::Vector2 getMousePositionNormalized();

		/// Returns the current mouse position (expressed in pixel coordinates)
		Ogre::Vector2 getMousePosition();

		/// Returns the relative mouse movement (since the last frame)
		Ogre::Vector2 getRelativeMouseMovement();

		/// Toggles the way the mouse is treated.  If relative_mode is set to true, the mouse is hidden and relative movements
		/// are reported by onTouch events and getMouse;
		void setMouseMode(bool relative_mode);

		/// Clears all current bindings (and axes / action names)
		void clearBindings();

		/// Reset bindings to their default values.
		void loadDefaultBindings();

		/// Load bindings from a file -- if the file is bad, loadDefaulBindings will be called instead
		void loadBindings(std::string fname);

	protected:
		/// Process (internally) a key event
		void processKeyEvent(const SDL_Event & e, bool starting);

		/// Process (internally) a joystick axis event
		void processGamepadAxis(const SDL_Event & e);

		/// Process (internally) a joystick action event
		void processGamepadAction(const SDL_Event & e, bool starting);

		/// Process (internally) a joystick dpad event
		void processGamepadDPad(const SDL_Event & e);

		/// Process (internally) a mouse button event (or wheel event, in which case starting parameter is ignored)
		void processMouseAction(const SDL_Event & e, bool starting);

		/// Process (internally) a mouse move event
		void processMouseMove(const SDL_Event & e);

		/// Send out a message to all listeners (note: do we want to specify what type of events a listener cares about?)
		void broadcastAction(std::string name, bool is_starting);

		/// Send out an axis-message to all listeners
		void broadcastAxis(std::string name, unsigned int axis_num, float new_val);

		/// Send out a touch message to all listeners
		void broadcastTouch(unsigned int touch_num, int x, int y, int xrel, int yrel);
	};
}
