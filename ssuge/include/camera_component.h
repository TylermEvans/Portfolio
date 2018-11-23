#pragma once
#include <stdafx.h>
#include <component.h>

namespace ssuge
{
	// Forward reference to the game object class (which we include in the .cpp file to avoid a circular dependency)
	class GameObject;

	/// The CameraComponent class is used to create a camera which is attached to a GameObject.  It is a bit unique
	/// in that it can have positional / rotationall offsets (from the parent game object).  This is to facilitate 
	/// first-person, third-person cameras.
	class CameraComponent : public Component
	{
	// @@@@@ ATTRIBUTES @@@@@
	protected:
		/// The Ore Camera this is based on.
		Ogre::Camera * mCamera;

	// @@@@@ CONSTRUCTOR / DESTRUCTORS @@@@@
	public:
		/// Constructor
		CameraComponent(GameObject * owner);

		/// Destructor
		~CameraComponent();
		
	// @@@@@ OVERRIDES from Component class @@@@@
	public:
		/// Tells the caller what type we are.
		ComponentType getType() override { return ComponentType::CAMERA; }
		
		/// Makes this component inactive if is_visible is set to true
		void setVisible(bool is_visible) override { mCamera->setVisible(is_visible); }

	// @@@@@ METHODS @@@@@
	public:
		/// Sets the directional offset of this camera (from game object)
		void setDirection(Ogre::Vector3 d) { mCamera->setDirection(d); }

		/// Sets the positional offset of this camera (from game object)
		void setPositionOffset(Ogre::Vector3 p) { mCamera->setPosition(p); }

		/// Sets the near and far clip values for the camera
		void setClipDistances(float n, float f) { mCamera->setNearClipDistance(n); mCamera->setFarClipDistance(f); }

		/// Connects this contained camera to a viewport (making it render there)
		void connectToViewport(Ogre::Viewport * v) { v->setCamera(mCamera); }

		Ogre::Ray getRayCast(float x, float y) { return mCamera->getCameraToViewportRay(x, y); }
	};
}
