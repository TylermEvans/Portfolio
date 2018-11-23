#pragma once
#include "stdafx.h"
#include <component.h>
#include <OgreSphere.h>
namespace ssuge {
	class GameObject;
	class ColliderComponent : public Component {

		public:
			ColliderComponent(Ogre::Vector3 origin, float radius , GameObject * owner);
			float rayIntersection(Ogre::Ray ray);
			ComponentType getType() { return ComponentType::COLLIDER; }
			Ogre::Vector3 getOrigin() { return mSphere.getCenter(); }
			void setOrigin(Ogre::Vector3 vec) { mSphere.setCenter(vec); }
			void setRadius(float rad) { mSphere.setRadius(rad); }
			float getRadius() { return mSphere.getRadius(); }
			Ogre::Sphere getSphere() { return mSphere; }
			void sphereIntersection(ssuge::ColliderComponent* other);
		private:
			Ogre::Sphere mSphere;
			




	};
}