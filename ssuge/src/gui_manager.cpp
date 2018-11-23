#include <stdafx.h>
#include <gui_manager.h>
template<> ssuge::GuiManager* ssuge::Singleton<ssuge::GuiManager>::msSingleton = NULL;
ssuge::GuiManager::GuiManager() {
	Ogre::OverlayManager * mgr = Ogre::OverlayManager::getSingletonPtr();
	mGuiOverlay = mgr->create("GuiManagerGui");

	// Create a panel to hold all text elements
	panel = (Ogre::OverlayContainer*)(mgr->createOverlayElement("Panel", "GuiManagerGui\\Panel"));
	mGuiOverlay->add2D(panel);
	mGuiOverlay->show();
}
void ssuge::GuiManager::addGuiComponent(std::string name, ssuge::GuiComponent* comp) {
	if (comp->img) {
		panel->addChild(comp->getImageElem());
	}
	else {
		panel->addChild(comp->getTextElem());
	}
	mGuiComponents[name] = comp;	
}
ssuge::GuiComponent* ssuge::GuiManager::getGuiComponent(std::string compname) {
	return mGuiComponents[compname];
}