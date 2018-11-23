#pragma once
#include <stdafx.h>
#include <singleton.h>

#define LOG_MANAGER ssuge::LogManager::getSingletonPtr()

namespace ssuge
{
	/// The LogManager is used to save log message to a log file (re-created each time the program is run)
	/// and to optionally display messages on-screen in a "console".
	class LogManager : public Singleton<LogManager>
	{
	// @@@@@ ATTRIBUTES @@@@@
	protected:
		/// The file (which is opened when the log manager is created and stays open until it is destroyed)
		std::ofstream mFile;

		/// The Ogre overlay used to display on-screen text
		Ogre::Overlay * mOverlay;

		/// The vector of text elements used for each line on the console text.
		std::vector<Ogre::TextAreaOverlayElement*> mOverlayTextElements;

		/// The time left until this text element is removed (to get the fade effect)
		std::vector<float> mTextElementTimeLeft;

		/// The maximum amount of time given to this line of text when it was created (to calculate the amount of fade)
		std::vector<float> mTextElementTimeMax;

		/// The actual string contents of each line in the console.
		std::vector<std::string> mTextElementCaption;

	// @@@@@ CONSTRUCTORS / DESTRUCTORS @@@@@
	public:
		/// Constructor
		LogManager(std::string fname, unsigned int num_text_lines);
		
		/// Destructor
		virtual ~LogManager();

	// @@@@@ METHODS @@@@@
	public:
		/// Should be called once per frame (to update the text fade and "bumping")
		virtual void update(float dt);

		/// Log a message to the log file.  If time_on_gui is positive, it will also be displayed in the "console"
		/// (and will remain there until time_on_gui seconds elapse).
		virtual void log(std::string s, float time_on_gui = -1.0f);
	};
}


