#include "stdafx.h"
#include <collider_component.h>
#include <application.h>


ssuge::ColliderComponent::ColliderComponent(Ogre::Vector3 origin, float radius, GameObject * owner) : Component(owner) {
	this->mSphere = Ogre::Sphere(origin, radius);
	
}
float ssuge::ColliderComponent::rayIntersection(Ogre::Ray ray) {
	
	std::pair<bool, float> hitResult = ray.intersects(this->mSphere);
	if (hitResult.first == true) {
		return 1;
	}
	else {
		return 0;
	}

}
void ssuge::ColliderComponent::sphereIntersection(ssuge::ColliderComponent* other) {
	bool result = mSphere.intersects(other->getSphere());
	if (result == true) {
		this->getOwner()->onCollide(other->getOwner()->getName(), result);
	}
}
