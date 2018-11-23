#pragma once
#include <stdafx.h>
#include <component.h>

namespace ssuge
{
	class GameObject;

	/// The MeshComponent component-type is used to load and display a .mesh file instance
	class MeshComponent : public Component
	{
	// @@@@@ ATTRIBUTES @@@@@
	protected:
		/// The ogre entity.
		Ogre::Entity * mEntity;

	// CONSTRUCTORS / DESTRUCTORS @@@@@
	public:
		/// The constructor
		MeshComponent(std::string fname, GameObject * owner);

		/// Destructor
		~MeshComponent();

	// @@@@@ OVERRIDES from COMPONENT @@@@@
	public:
		/// Returns the type of this component.
		ComponentType getType() { return ComponentType::MESH; }
		
		/// Makes this mesh not render (if is_visible is false)
		void setVisible(bool is_visible) override { mEntity->setVisible(is_visible); }
		void setMaterial(std::string name, int slot) { mEntity->getSubEntity(slot)->setMaterialName(name); }
		void setMaterial(std::string name) { mEntity->setMaterialName(name); }
		float getBoundingRad() { return mEntity->getBoundingRadius(); }
	};
}
