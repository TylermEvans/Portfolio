#pragma once
#include <stdafx.h>
#include <game_object.h>
#include <singleton.h>

#define GAME_OBJECT_MANAGER ssuge::GameObjectManager::getSingletonPtr()

namespace ssuge
{
	/// The GameObjectManager (usually referred to as GOM) is responsible for creating and 
	/// managing all game object instances (i.e. it is a FACTORY) in user-defined groups.
	class GameObjectManager : public Singleton<GameObjectManager>
	{
	// @@@@@ ATTRIBUTES @@@@@
	protected:
		/// The mapping from group-ids to sub-groups of GameObjects
		std::map<int, std::map<std::string, GameObject*>> mGroups;

		/// A mapping from group names to group id numbers to group names
		std::map<std::string, int> mGroupNamesToID;

		/// A mapping from group id numbers to group names.
		std::map<int, std::string> mGroupIDsToNames;

		/// A mapping from group id numbers to group 
		std::map<int, bool> mGroupHidden;

		/// The next auto-create group id (maintained to be one higher than any existing group id's)
		int mNextGroupNumber;

	// @@@@@ CONSTRUCTORS / DESTRUCTORS @@@@@
	public:
		/// Constructor
		GameObjectManager() : mNextGroupNumber(0) {}

		/// Destructor
		virtual ~GameObjectManager();

	// @@@@@ METHODS @@@@@
	public:
		/// Create a new game object and put it in our master list of game objects
		GameObject * createGameObject(std::string group_name, std::string object_name);

		/// Create a new game object and put it in our master list of game objects
		GameObject * createGameObject(int group_id, std::string object_name);

		/// Destroy a game object
		void destroyGameObject(int group_id, std::string object_name);

		/// Destroy this game object
		void destroyGameObject(GameObject * g);

		/// Create a named group -- this must be called before creating objects in this group (and it mustn't be called
		/// more than once using this name or id number)
		void createGroup(int id, std::string name);

		/// Create a named group -- the auto-id number will be supplied (and incremented) 
		void createGroup(std::string name);

		/// Destroy all game objects in a group.  If only_delete_contents is false, the group itself will be deleted too.
		void destroyGroup(int id, bool only_delete_contents = true);

		/// Sets all game objects in this group to have this visibility.
		void setVisible(int id, bool is_visible);

		/// Updates all game objects in all groups.
		void update(float dt);

		/// Create a group (and contents) from an ini-style script file.  Returns 0 on success.
		int loadGroup(std::string fname);
	
	// @@@@@ GETTERS @@@@@
	public:
		/// Gets this game object (from a specific group).  Returns null if not found.
		GameObject * getGameObject(int group_id, std::string object_name);

		/// Gets this game object (from a specific named group).  Returns null if not found.
		GameObject * getGameObject(std::string group_name, std::string object_name);

		/// Finds the first occurrence of this game object name in any group (slow).  Returns null if no game objects with that name are found.
		GameObject * getGameObject(std::string object_name);
		
		/// Gets the group id of this named group (or -1 if not found)
		int getGroupID(std::string name);

		/// Gets the name of the group with this id (or "???" if that id doesn't exist)
		std::string getGroupName(int id);

		/// Is this group visible right now?
		bool getVisible(int group_id);
	};
}
