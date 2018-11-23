#include <stdafx.h>
#include <gui_component.h>
#include <game_object.h>
#include <application.h>
#include <iostream>

ssuge::GuiComponent::GuiComponent(std::string name, bool img_or_not, GameObject * owner) : Component(owner){
	Ogre::OverlayManager* mgr = Ogre::OverlayManager::getSingletonPtr();
	img = img_or_not;
	if (img_or_not) {
		//mImage = new Ogre::Material()
		mImage = mgr->createOverlayElement("Panel", "GuiComponent\\Image" + name);
		mImage->setMaterialName(name);
		mImage->setMetricsMode(Ogre::GMM_RELATIVE);
	}
	else {
		mText = (Ogre::TextAreaOverlayElement*)mgr->createOverlayElement("TextArea", "GuiComponent\\Text" + name);
		mString = mText->getName();
		mText->setMetricsMode(Ogre::GMM_PIXELS);
		mText->setFontName("SdkTrays/Value");
		mText->setColourBottom(Ogre::ColourValue(1.0f, 0.4f, 0.4f));
		mText->setColourTop(Ogre::ColourValue(1.0f, 1.0f, 1.0f));
	}
}
void ssuge::GuiComponent::setText(std::string text) {
	mText->setCaption(text);
}
void ssuge::GuiComponent::setImage(std::string image) {
	mImage->setMaterialName(image);
}
void ssuge::GuiComponent::setPosition(float x, float y) {
	if (img) {
		mImage->setPosition(x, y);
	}
	else {
		mText->setPosition(x, y);
	}
	
}
void ssuge::GuiComponent::setDimensions(float x, float y) {
	if (img) {
		mImage->setDimensions(x, y);
	}
	else {
		mText->setDimensions(x, y);
	}
	
}
void ssuge::GuiComponent::setCharHeight(float h) {
	mText->setCharHeight(h);
}

