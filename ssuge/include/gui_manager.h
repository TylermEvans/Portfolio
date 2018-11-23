#pragma once
#include <stdafx.h>
#include <singleton.h>
#include <gui_component.h>
#include <map>
#define GUI_MANAGER ssuge::GuiManager::getSingletonPtr()
namespace ssuge {
	class GuiManager : public Singleton<GuiManager> {

	   public:
			std::map<std::string, ssuge::GuiComponent*> mGuiComponents;
			Ogre::Overlay * mGuiOverlay;
			Ogre::OverlayContainer* panel;
		public:
			GuiManager();
			void addGuiComponent(std::string name, ssuge::GuiComponent* comp);
			GuiComponent* getGuiComponent(std::string compname);




	};


}
