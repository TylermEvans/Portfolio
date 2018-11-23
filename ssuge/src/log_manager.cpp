#include <stdafx.h>
#include <log_manager.h>
#include <utility.h>

// The template-specialization to declare the singleton variable for the LogManager class
template<> ssuge::LogManager* ssuge::Singleton<ssuge::LogManager>::msSingleton = NULL;

ssuge::LogManager::LogManager(std::string fname, unsigned int num_text_lines) : mFile(fname)
{
	// Create the overlay that log manager will display over the viewport
	Ogre::OverlayManager * mgr = Ogre::OverlayManager::getSingletonPtr();
	mOverlay = mgr->create("LogManagerGUI");

	// Create a panel to hold all text elements
	Ogre::OverlayContainer * panel = (Ogre::OverlayContainer*)(mgr->createOverlayElement("Panel", "LogManagerGUI\\Panel"));
	mOverlay->add2D(panel);

	// Create the text elements
	float y_step = (float)mgr->getViewportHeight() / num_text_lines;
	for (unsigned int i = 0; i < num_text_lines; i++)
	{
		Ogre::TextAreaOverlayElement * text = (Ogre::TextAreaOverlayElement*)mgr->createOverlayElement("TextArea", "LogManagerGUI\\Text" + std::to_string(i));
		text->setMetricsMode(Ogre::GMM_PIXELS);
		text->setFontName("SdkTrays/Value");
		panel->addChild(text);
		mOverlayTextElements.push_back(text);
	}

	// Show the overlay
	mOverlay->show();
}




ssuge::LogManager::~LogManager()
{
	// Note: Ogre will clean every overlay (element) up on shutdown.

	// Close our log file
	mFile.close();
}



void ssuge::LogManager::update(float dt)
{
	Ogre::OverlayManager * mgr = Ogre::OverlayManager::getSingletonPtr();
	float y_step = (float)mgr->getViewportHeight() / mOverlayTextElements.size();
	for (unsigned int i = 0; i < mTextElementCaption.size(); )
	{
		mTextElementTimeLeft[i] -= dt;
		if (mTextElementTimeLeft[i] <= 0.0f)
		{
			mTextElementTimeLeft.erase(mTextElementTimeLeft.begin() + i);
			mTextElementCaption.erase(mTextElementCaption.begin() + i);
			mTextElementTimeMax.erase(mTextElementTimeMax.begin() + i);
		}
		else
		{
			mOverlayTextElements[i]->setCaption(mTextElementCaption[i]);
			mOverlayTextElements[i]->setPosition(0, i * y_step);
			mOverlayTextElements[i]->setDimensions((float)mgr->getViewportWidth(), y_step);
			mOverlayTextElements[i]->setCharHeight(y_step);

			float alpha = mTextElementTimeLeft[i] / mTextElementTimeMax[i];
			Ogre::ColourValue color = mOverlayTextElements[i]->getColourBottom();
			color.a = alpha;
			mOverlayTextElements[i]->setColourBottom(color);
			color = mOverlayTextElements[i]->getColourTop();
			color.a = alpha;
			mOverlayTextElements[i]->setColourTop(color);
			i++;
		}
	}
	for (unsigned int i = mTextElementCaption.size(); i < mOverlayTextElements.size(); i++)
	{
		mOverlayTextElements[i]->setCaption("");
	}
}



void ssuge::LogManager::log(std::string s, float time_on_gui)
{
	if (time_on_gui > 0)
	{
		// This next bit converts strings with newline / carriage-returns into multiple lines
		std::string clean_s = replace(s, "\n\r", "\a");
		clean_s = replace(clean_s, "\r\n", "\a");
		clean_s = replace(clean_s, "\n", "\a");
		clean_s = replace(clean_s, "\r", "\a");
		std::vector<std::string> elements;
		split(clean_s, elements, "\a");

		if (mTextElementCaption.size() >= mOverlayTextElements.size())
		{
			// Bump the first element to make room for this one
			mTextElementTimeLeft.erase(mTextElementTimeLeft.begin());
			mTextElementCaption.erase(mTextElementCaption.begin());
			mTextElementTimeMax.erase(mTextElementTimeMax.begin());
		}
		//mTextElementCaption.push_back(curs);
		mTextElementCaption.push_back(clean_s);
		mTextElementTimeLeft.push_back(time_on_gui);
		mTextElementTimeMax.push_back(time_on_gui);
	}

	// Reference: https://stackoverflow.com/questions/997946/how-to-get-current-time-and-date-in-c
	time_t t = time(NULL);
	struct tm * now = localtime(&t);

	mFile << now->tm_mon + 1 << "/" << now->tm_mday << "/" << now->tm_year + 1900;
	mFile << "@" << now->tm_hour << ":" << now->tm_min << ":" << now->tm_sec << "    ";
	mFile << s << std::endl;
}

