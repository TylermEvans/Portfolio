#pragma once
#include <stdafx.h>
#include <component.h>
namespace ssuge {
	class GameObject;
	class GuiComponent : public Component {


		private:
			std::string mString;
			Ogre::OverlayElement* mImage;
			Ogre::TextAreaOverlayElement * mText;
			
			

		public:
			GuiComponent(std::string name, bool img_or_not, GameObject * owner);
			ComponentType getType() { return ComponentType::GUI; }
			void setText(std::string text);
			void setImage(std::string img);
			void setPosition(float x, float y);
			void setDimensions(float x, float y);
			Ogre::TextAreaOverlayElement* getTextElem() { return mText; }
			Ogre::OverlayElement* getImageElem() { return mImage; }
			std::string getGuiName() { return mString; }
			void setCharHeight(float h);
			bool img;
			
	};
}
