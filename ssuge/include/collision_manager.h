#pragma once
#include <stdafx.h>
#include <singleton.h>
#include <collider_component.h>
#include <vector>
#define COLLISION_MANAGER ssuge::CollisionManager::getSingletonPtr()
namespace ssuge {
	class CollisionManager : public Singleton<CollisionManager> {
		private:
			std::vector<ColliderComponent*> mComps;

		public:
			CollisionManager();
			void addComponent(ColliderComponent * comp);
			std::vector<float> rayIntersections(Ogre::Ray ray);
			void sphereCollisions();
			void removeComponent(std::string name);

	};
}
