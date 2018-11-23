#include <stdafx.h>
#include "collision_manager.h"
#include <game_object.h>
#include <log_manager.h>
template<> ssuge::CollisionManager* ssuge::Singleton<ssuge::CollisionManager>::msSingleton = NULL;

ssuge::CollisionManager::CollisionManager() {

}
void ssuge::CollisionManager::addComponent(ssuge::ColliderComponent * comp) {
	mComps.push_back(comp);
}
std::vector<float> ssuge::CollisionManager::rayIntersections(Ogre::Ray ray) {
	std::vector<float> distanceCollisions;
	for (int i = 0; i < this->mComps.size(); i++) {
		float distance = mComps[i]->rayIntersection(ray);
		distanceCollisions.push_back(distance);
	}
	return distanceCollisions;

}
void ssuge::CollisionManager::sphereCollisions() {
	if (mComps.size() > 1) {
		for (int i = 0; i < this->mComps.size(); i++) {
			for (int j = i + 1; j < this->mComps.size(); j++) {
				mComps[i]->sphereIntersection(mComps[j]);
			}
		}
	}
}
void ssuge::CollisionManager::removeComponent(std::string name) {
	std::vector<ColliderComponent*>::iterator it = mComps.begin();
	while (it != mComps.end()) {
		ColliderComponent * comp = *it;
		GameObject * owner = (GameObject*)comp->getOwner();
		if (owner->getName() == name) {
			mComps.erase(it);
			break;
		}
		it++;
	}
}