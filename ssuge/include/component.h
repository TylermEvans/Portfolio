#pragma once
#include <stdafx.h>



namespace ssuge
{
	// Forward declaration of GameObject class
	class GameObject;

	/// The master list of component types -- update this whenever a new type of component is created
	enum class ComponentType {MESH, LIGHT, CAMERA, SOUND, GUI, COLLIDER};

	/// The Component class is an abstract base class for all other components.  We did this so we
	/// could have one container for all components, but actually store MeshComponents, LightComponents, etc.
	class Component
	{
	// @@@@@ ATTRIBUTES @@@@@
	protected:
		/// The containing game object
		GameObject * mOwner;

	// @@@@@ CONTRUCTORS / DESTRUCTORS @@@@@
	public:
		/// The constructor
		Component(GameObject * owner) : mOwner(owner) { }

		/// The destructor
		virtual ~Component() { }

	// @@@@@ METHODS that all derived component classes must define
	public:
		/// What type of component is this?  Necessary since we sometimes (like in the game object container)
		/// only see a list of component*'s.  We can determine what type they are using this method.
		virtual ComponentType getType() = 0;

		/// Returns the containing game object
		virtual GameObject * getOwner() { return mOwner; }

		/// The derived class should re-define this if the component needs to be updated every frame.
		virtual void update(float dt) {}

		/// When is_visible is false, the component should become inactive (the definition of inactive varies by component)
		virtual void setVisible(bool is_visible) { }
	};
}