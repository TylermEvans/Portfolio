#include <stdafx.h>
#include <input_manager.h>
#include <application.h>
#include <utility.h>

// The template-specialization to declare the singleton variable for the LogManager class
template<> ssuge::InputManager* ssuge::Singleton<ssuge::InputManager>::msSingleton = NULL;

ssuge::InputManager::InputManager(SDL_Window * win) : mWindow(win), mGamepad(NULL)
{
	// Enable gamepad support.  Currently I'm only looking for one joystick
	SDL_InitSubSystem(SDL_INIT_JOYSTICK);
	if (SDL_NumJoysticks() > 0)
	{
		mGamepad = SDL_JoystickOpen(0);
	}

	loadDefaultBindings();
}


ssuge::InputManager::InputManager(SDL_Window * win, std::string binding_fname) : mWindow(win), mGamepad(NULL)
{
	// Enable gamepad support.  Currently I'm only looking for one joystick
	SDL_InitSubSystem(SDL_INIT_JOYSTICK);
	if (SDL_NumJoysticks() > 0)
	{
		mGamepad = SDL_JoystickOpen(0);
	}

	loadBindings(binding_fname);
}



ssuge::InputManager::~InputManager()
{
	if (mGamepad)
		SDL_JoystickClose(mGamepad);
}


bool ssuge::InputManager::update()
{
	SDL_Event e;
	bool rv = true;
	// Process all waiting events.
	while (SDL_PollEvent(&e))
	{
		switch (e.type)
		{
		case SDL_QUIT:
			rv = false;
			break;
		case SDL_WINDOWEVENT:
			if (e.window.event == SDL_WINDOWEVENT_RESIZED)
				APPLICATION->resizeWindow(e.window.data1, e.window.data2);
			break;

		case SDL_KEYDOWN:
			if (e.key.repeat == 0)				// optional?
				processKeyEvent(e, true);
			break;
		case SDL_KEYUP:
			processKeyEvent(e, false);
			break;

		case SDL_JOYAXISMOTION:
			processGamepadAxis(e);
			break;
		case SDL_JOYBUTTONDOWN:
			processGamepadAction(e, true);
			break;
		case SDL_JOYBUTTONUP:
			processGamepadAction(e, false);
			break;
		case SDL_JOYHATMOTION:
			processGamepadDPad(e);
			break;

		case SDL_MOUSEBUTTONDOWN:
			processMouseAction(e, true);
			break;
		case SDL_MOUSEBUTTONUP:
			processMouseAction(e, false);
			break;
		case SDL_MOUSEWHEEL:
			processMouseAction(e, true);		// The boolean isn't really applicable here, but 
			break;								// I'm treating wheel events as button presses.
		case SDL_MOUSEMOTION:
			processMouseMove(e);
			break;
		
		}
	}

	return rv;
}




float ssuge::InputManager::getAxis(std::string name, unsigned int num)
{
	std::map<std::pair<std::string, unsigned int>, float>::iterator it = mAxisValues.find(std::pair<std::string, unsigned int>(name, num));
	if (it != mAxisValues.end())
	{
		return it->second;
	}
	else
	{
		EXCEPTION("Undefined axis name: '" + name + "'");
	}
}


void ssuge::InputManager::registerListener(Listener * g)
{
	for (unsigned int i = 0; i < mListeners.size(); i++)
	{
		if (mListeners[i] == g)
			return;					// already a listener!
	}
	// If we get here, g isn't in our listener list -- add it!
	mListeners.push_back(g);
}



void ssuge::InputManager::unregisterListener(Listener * g)
{
	std::vector<Listener*>::iterator it = mListeners.begin();
	while (it != mListeners.end())
	{
		if (*it == g)
		{
			it = mListeners.erase(it);
			return;				// Should only be one!
		}
		else
			++it;
	}
}


bool ssuge::InputManager::isActionValid(std::string name)
{
	std::map<std::string, int>::iterator it = mActionValues.find(name);
	return it != mActionValues.end();
}



bool ssuge::InputManager::getActionState(std::string name)
{
	std::map<std::string, int>::iterator it = mActionValues.find(name);
	if (it != mActionValues.end())
		return it->second > 0;
	return false;
}


Ogre::Vector2 ssuge::InputManager::getMousePositionNormalized()
{
	int w, h;
	SDL_GetWindowSize(mWindow, &w, &h);
	return Ogre::Vector2((float)mMouseData[0] / w, (float)mMouseData[1] / h);
}



Ogre::Vector2 ssuge::InputManager::getMousePosition()
{
	return Ogre::Vector2(mMouseData[0], mMouseData[1]);
}



Ogre::Vector2 ssuge::InputManager::getRelativeMouseMovement()
{
	return Ogre::Vector2(mMouseData[2], mMouseData[3]);
}



void ssuge::InputManager::setMouseMode(bool relative_mode)
{
	//SDL_SetRelativeMouseMode(relative_mode ? SDL_TRUE : SDL_FALSE);
	SDL_ShowCursor(relative_mode ? SDL_FALSE : SDL_TRUE);
}



void ssuge::InputManager::clearBindings()
{
	// Clear the bindings tables
	mAxisValues.clear();
	mActionValues.clear();
	mKeyboardActionBindings.clear();
	mKeyboardAxisBindings.clear();
	mGamepadActionBindings.clear();
	mGamepadAxisMultiplier.clear();
	mGamepadDPadBindings.clear();
	mMouseButtonBindings.clear();
	mMouseWheelBindings.clear();

	// Clear the mouse data
	memset(mMouseData, 0, sizeof(int) * 4);

	// Clear the dpad value
	mGamepadDPadData = 0;
	
	// Set up the available axes...(if we want to support multiple gamepads, we'd likely increase this 
	// from 2).
	for (unsigned int i = 0; i < 2; i++)
	{
		mAxisValues[std::pair<std::string, unsigned int>("horizontal", i)] = 0.0f;
		mAxisValues[std::pair<std::string, unsigned int>("vertical", i)] = 0.0f;
		mAxisValues[std::pair<std::string, unsigned int>("other", i)] = 0.0f;
	}
}


void ssuge::InputManager::loadDefaultBindings()
{
	clearBindings();

	// Set up the available actions (this will eventually be done in script(s))
	mActionValues["menu"] = 0;
	mActionValues["jump"] = 0;
	mActionValues["attack"] = 0;
	mActionValues["misc"] = 0;

	// Set up the initial bindings (this will also be done in script(s))
	mKeyboardAxisBindings[SDLK_a] = { "horizontal", 0, -1.0f };
	mKeyboardAxisBindings[SDLK_d] = { "horizontal", 0, 1.0f };
	mKeyboardAxisBindings[SDLK_w] = { "vertical", 0, 1.0f };
	mKeyboardAxisBindings[SDLK_s] = { "vertical", 0, -1.0f };
	mKeyboardAxisBindings[SDLK_LEFT] = { "horizontal", 1, -1.0f };
	mKeyboardAxisBindings[SDLK_RIGHT] = { "horizontal", 1, 1.0f };
	mKeyboardAxisBindings[SDLK_UP] = { "vertical", 1, 1.0f };
	mKeyboardAxisBindings[SDLK_DOWN] = { "vertical", 1, -1.0f };
	mKeyboardAxisBindings[SDLK_PAGEUP] = { "other", 0, 2.0f };
	mKeyboardAxisBindings[SDLK_RIGHTBRACKET] = { "other", 1, 2.0f };
	// ... actions
	mKeyboardActionBindings[SDLK_ESCAPE] = "menu";
	mKeyboardActionBindings[SDLK_SPACE] = "jump";


	// Set up the initial gamepad bindings (this will also be done in script(s))
	mGamepadAxisMultiplier[std::pair<std::string, unsigned int>("horizontal", 0)] = 1.0;
	mGamepadAxisMultiplier[std::pair<std::string, unsigned int>("vertical", 0)] = 1.0f;
	mGamepadAxisMultiplier[std::pair<std::string, unsigned int>("horizontal", 1)] = 1.0;
	mGamepadAxisMultiplier[std::pair<std::string, unsigned int>("vertical", 1)] = -1.0f;
	mGamepadAxisMultiplier[std::pair<std::string, unsigned int>("other", 0)] = 1.0;
	mGamepadAxisMultiplier[std::pair<std::string, unsigned int>("other", 0)] = -1.0f;
	// ... actions

	// Set up the initial mouse button bindings
	mMouseButtonBindings[SDL_BUTTON_LEFT] = "attack";
	mMouseButtonBindings[SDL_BUTTON_RIGHT] = "menu";
}


void ssuge::InputManager::loadBindings(std::string fname)
{
	clearBindings();

	// Load the ini file
	std::vector<IniSection> sections;
	if (!parseIniFile(fname, sections))
	{
		std::string key, value;

		for (unsigned int i = 0; i < sections.size(); i++)
		{
			if (sections[i].mLabel == "key-bindings")
			{
				for (unsigned int j = 0; j < sections[i].mPairs.size(); j++)
				{
					key = sections[i].mPairs[j].first;
					value = sections[i].mPairs[j].second;

					SDL_Keycode kcode = SDL_GetKeyFromName(key.c_str());
					if (kcode != SDLK_UNKNOWN)
					{
						// See if this is an action or an axis binding
						if (contains(value, ":"))
						{
							// Assume it's an axis.  
							std::vector<std::string> parts;
							split(value, parts, ":");
							if (parts.size() == 3 && (parts[0] == "vertical" || parts[0] == "horizontal" || parts[0] == "other") &&
								is_integer(parts[1]) && is_double(parts[2]))
							{
								mKeyboardAxisBindings[kcode] = { parts[0], (unsigned int)to_integer(parts[1]), (float)to_double(parts[2]) };
							}
						}
						else
						{
							// Assume it's an action.  If we don't already have the action referenced, create it
							if (!isActionValid(value))
								mActionValues[value] = 0;
							mKeyboardActionBindings[kcode] = value;
						}
					}

				}
			}
			else if (sections[i].mLabel == "mouse-bindings")
			{
				for (unsigned int j = 0; j < sections[i].mPairs.size(); j++)
				{
					key = sections[i].mPairs[j].first;
					value = sections[i].mPairs[j].second;

					if (key == "Left")
						mMouseButtonBindings[SDL_BUTTON_LEFT] = value;
					else if (key == "Right")
						mMouseButtonBindings[SDL_BUTTON_RIGHT] = value;
					else if (key == "Middle")
						mMouseButtonBindings[SDL_BUTTON_MIDDLE] = value;
					else if (key == "Up")
						mMouseWheelBindings[1] = value;
					else if (key == "Down")
						mMouseWheelBindings[-1] = value;
				}
			}
			else if (sections[i].mLabel == "gamepad-bindings")
			{
				for (unsigned int j = 0; j < sections[i].mPairs.size(); j++)
				{
					key = sections[i].mPairs[j].first;
					value = sections[i].mPairs[j].second;
					std::vector<std::string> parts;
					split(value, parts, ":");

					int action_binding_val = -1;
					int dpad_binding_val = -1;

					if (key == "A")
						action_binding_val = 0;
					else if (key == "B")
						action_binding_val = 1;
					else if (key == "X")
						action_binding_val = 2;
					else if (key == "Y")
						action_binding_val = 3;
					else if (key == "LB")
						action_binding_val = 4;
					else if (key == "RB")
						action_binding_val = 5;
					else if (key == "Menu")
						action_binding_val = 6;
					else if (key == "Start")
						action_binding_val = 7;

					else if (key == "left-analog" && parts.size() > 1 && is_double(parts[1]) && (parts[0] == "horizontal" || parts[0] == "vertical"))
						mGamepadAxisMultiplier[std::pair<std::string, unsigned int>(parts[0], 0)] = ssuge::to_double(parts[1]);
					else if (key == "right-analog" && parts.size() > 1 && is_double(parts[1]) && (parts[0] == "horizontal" || parts[0] == "vertical"))
						mGamepadAxisMultiplier[std::pair<std::string, unsigned int>(parts[0], 1)] = ssuge::to_double(parts[1]);
					else if (key == "left-thumb" && parts.size() > 1 && is_double(parts[1]) && parts[0] == "other")
						mGamepadAxisMultiplier[std::pair<std::string, unsigned int>("other", 0)] = ssuge::to_double(parts[1]);
					else if (key == "right-thumb" && parts.size() > 1 && is_double(parts[1]) && parts[0] == "other")
						mGamepadAxisMultiplier[std::pair<std::string, unsigned int>("other", 1)] = ssuge::to_double(parts[1]);

					else if (key == "UpDPad")
						dpad_binding_val = 1;
					else if (key == "RightDPad")
						dpad_binding_val = 2;
					else if (key == "DownDPad")
						dpad_binding_val = 4;
					else if (key == "RightDPad")
						dpad_binding_val = 8;


					if (action_binding_val >= 0)
					{
						if (!isActionValid(value))
							mActionValues[value] = 0;
						mGamepadActionBindings[action_binding_val] = value;
					}

					if (dpad_binding_val >= 0)
					{
						if (!isActionValid(value))
							mActionValues[value] = 0;
						mGamepadDPadBindings[(unsigned char)dpad_binding_val] = value;
					}
				}
			}
		}
	}
	else
	{
		// Something went wrong loading that file -- just fall back to the default bindings
		loadDefaultBindings();
	}
}




void ssuge::InputManager::processKeyEvent(const SDL_Event & e, bool starting)
{
	std::string action_name = "";
	std::string axis_name = "";
	float axis_value = 0.0f;
	unsigned int axis_num = 0;
	

	std::map<SDL_Keycode, AxisBinding>::iterator axis_it = mKeyboardAxisBindings.begin();
	while (axis_it != mKeyboardAxisBindings.end())
	{
		if (axis_it->first == e.key.keysym.sym)
		{
			axis_name = axis_it->second.mAxisName;
			axis_value = axis_it->second.mValue;
			axis_num = axis_it->second.mAxisNum;
			break;
		}
		++axis_it;
	}

	std::map<SDL_Keycode, std::string>::iterator action_it = mKeyboardActionBindings.begin();
	while (action_it != mKeyboardActionBindings.end())
	{
		if (action_it->first == e.key.keysym.sym)
		{
			action_name = action_it->second;
			break;
		}
		++action_it;
	}

	if (action_name != "")
	{
		mActionValues[action_name] += starting ? 1 : -1;
		broadcastAction(action_name, starting);
	}
	if (axis_name != "")
	{
		mAxisValues[std::pair<std::string, unsigned int>(axis_name, axis_num)] += starting ? axis_value : -axis_value;
		broadcastAxis(axis_name, axis_num, axis_value);
	}
}



void ssuge::InputManager::processGamepadAxis(const SDL_Event & e)
{
	std::string axis_name;
	unsigned int axis_num = 0;

	// I was (here) attempting to allow the user to name the axes bound to each portion
	// of the controller, but this felt unnecessary -- I think it's more important to allow them
	// to choose what to do with it/
	/*std::map<unsigned char, AxisBinding>::iterator it = mGamepadAxisBindings.begin();
	while (it != mGamepadAxisBindings.end())
	{
		if (it->first == e.jaxis.axis)
		{
			axis_name = it->second.mAxisName;
			axis_num = it->second.mAxisNum;
			axis_value = it->second.mValue * e.jaxis.value / 32768.0f;
		}
		++it;
	}*/

	// The new, hard-coded (at least in axis names) version:
	switch (e.jaxis.axis)
	{
	case 0:		axis_name = "horizontal";	axis_num = 0;		break;
	case 1:		axis_name = "vertical";		axis_num = 0;		break;
	case 3:		axis_name = "horizontal";	axis_num = 1;		break;
	case 4:		axis_name = "vertical";		axis_num = 1;		break;
	case 2:		axis_name = "other";		axis_num = 0;		break;
	case 5:		axis_name = "other";		axis_num = 1;		break;
	}

	if (axis_name != "")
	{
		float multiplier = 1.0;
		std::map<std::pair<std::string, unsigned int>, float>::iterator it = mGamepadAxisMultiplier.find(std::pair<std::string, unsigned int>(axis_name, axis_num));
		if (it != mGamepadAxisMultiplier.end())
			multiplier = it->second;
		
		float axis_value = multiplier * (e.jaxis.value / 32768.0f);
		mAxisValues[std::pair<std::string, unsigned int>(axis_name, axis_num)] = axis_value;
		broadcastAxis(axis_name, axis_num, axis_value);
		
		
	}
}



void ssuge::InputManager::processGamepadAction(const SDL_Event & e, bool starting)
{
	std::map<unsigned char, std::string>::iterator it = mGamepadActionBindings.find(e.jbutton.button);
	if (it != mGamepadActionBindings.end())
	{
		std::map<std::string, int>::iterator it2 = mActionValues.find(it->second);
		if (it2 != mActionValues.end())
		{
			if (e.type == SDL_JOYBUTTONDOWN)
				it2->second++;
			else
				it2->second--;
			broadcastAction(it->second, e.type == SDL_JOYBUTTONDOWN);
		}
	}
}



void ssuge::InputManager::processGamepadDPad(const SDL_Event & e)
{
	std::vector<unsigned char> directions_active;

	if (e.jhat.value & 0x01)
		directions_active.push_back(1);		// "UpDPad"
	if (e.jhat.value & 0x02)
		directions_active.push_back(2);		// "RightDPad"
	if (e.jhat.value & 0x04)
		directions_active.push_back(4);		// "DownDPad"
	if (e.jhat.value & 0x08)
		directions_active.push_back(8);		// "LeftDPad"

	for (unsigned int i = 0; i < directions_active.size(); i++)
	{
		// See if this event is different than what it was last time we had a change.
		// If not, we don't need to do anything (one of the other dpad directions changed)
		if ((mGamepadDPadData & directions_active[i]) != (e.jhat.value & directions_active[i]))
		{
			bool starting = (e.jhat.value & directions_active[i]) > 0;

			// See if we have an action bound to this dpad
			std::map<unsigned char, std::string>::iterator it = mGamepadDPadBindings.find(directions_active[i]);
			if (it != mGamepadDPadBindings.end())
			{
				std::map<std::string, int>::iterator it2 = mActionValues.find(it->second);
				if (starting)
					it2->second++;
				else
					it2->second--;
				broadcastAction(it->second, starting);
			}
		}
	}

	// Set the gamepad current value to that read from the jhat value
	mGamepadDPadData = e.jhat.value;
}



void ssuge::InputManager::processMouseAction(const SDL_Event & e, bool starting)
{
	if (e.type == SDL_MOUSEWHEEL)
	{
		if (e.wheel.y > 0)
		{
			// away from user
			std::map<int, std::string>::iterator it = mMouseWheelBindings.find(1);
			if (it != mMouseWheelBindings.end())
				broadcastAction(it->second, true);
		}
		else if (e.wheel.y < 0)
		{
			// towards user
			std::map<int, std::string>::iterator it = mMouseWheelBindings.find(-1);
			if (it != mMouseWheelBindings.end())
				broadcastAction(it->second, true);
		}
	}
	else
	{
		// Mouse button press
		std::map<unsigned int, std::string>::iterator it = mMouseButtonBindings.find(e.button.button);
		if (it != mMouseButtonBindings.end())
		{
			if (e.button.state == SDL_PRESSED)
				mActionValues[it->second]++;
			else
				mActionValues[it->second]--;
			broadcastAction(it->second, e.button.state == SDL_PRESSED);
		}
	}
}



void ssuge::InputManager::processMouseMove(const SDL_Event & e)
{
	mMouseData[0] = e.motion.x;
	mMouseData[1] = e.motion.y;
	mMouseData[2] = e.motion.xrel;
	mMouseData[3] = e.motion.yrel;

	broadcastTouch(0, mMouseData[0], mMouseData[1], mMouseData[2], mMouseData[3]);
}



void ssuge::InputManager::broadcastAction(std::string name, bool is_starting)
{
	for (unsigned int i = 0; i < mListeners.size(); i++)
		mListeners[i]->onAction(name, is_starting);
}



void ssuge::InputManager::broadcastAxis(std::string name, unsigned int num, float new_val)
{
	for (unsigned int i = 0; i < mListeners.size(); i++)
		mListeners[i]->onAxis(name, num, new_val);
}


void ssuge::InputManager::broadcastTouch(unsigned int touch_num, int x, int y, int xrel, int yrel)
{
	for (unsigned int i = 0; i < mListeners.size(); i++)
		mListeners[i]->onTouch(touch_num, x, y, xrel, yrel);
}