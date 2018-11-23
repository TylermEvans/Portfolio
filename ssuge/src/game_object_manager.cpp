#include <stdafx.h>
#include <game_object_manager.h>
#include <utility.h>
#include <script_manager.h>
#include <application.h>

template<>
ssuge::GameObjectManager * ssuge::Singleton<ssuge::GameObjectManager>::msSingleton = NULL;

		

ssuge::GameObjectManager::~GameObjectManager()
{
	std::map<int, std::map<std::string, GameObject*>>::iterator it = mGroups.begin();
	while (it != mGroups.end())
	{
		std::map<std::string, GameObject*>::iterator it2 = it->second.begin();
		while (it2 != it->second.end())
		{
			delete it2->second;
			++it2;
		}
		it->second.clear();

		++it;
	}
	mGroups.clear();
	mGroupHidden.clear();
	mGroupIDsToNames.clear();
	mGroupNamesToID.clear();
}


ssuge::GameObject * ssuge::GameObjectManager::createGameObject(std::string group_name, std::string object_name)
{
	std::map<std::string, int>::iterator it = mGroupNamesToID.find(group_name);
	if (it != mGroupNamesToID.end())
		return createGameObject(it->second, object_name);
	else
		EXCEPTION("Undefined group name: '" + group_name + "'");
}


ssuge::GameObject * ssuge::GameObjectManager::createGameObject(int group_id, std::string object_name)
{
	std::map<int, std::map<std::string, GameObject*>>::iterator it = mGroups.find(group_id);
	if (it == mGroups.end())
		EXCEPTION("Undefined group num: " + std::to_string(group_id) + " (call createGroup first!)");
	else
	{
		std::map<std::string, GameObject*>::iterator it2 = it->second.find(object_name);
		if (it2 == it->second.end())
		{
			// Valid group and object name -- insert it and return it.
			GameObject * go = new GameObject(object_name, group_id);
			it->second[object_name] = go;
			if (mGroupHidden[group_id])
				go->setVisible(false);
			return go;
		}
		else
			EXCEPTION("Group " + std::to_string(group_id) + " already has a member named '" + object_name + "'");
	}
}




ssuge::GameObject * ssuge::GameObjectManager::getGameObject(int group_id, std::string object_name)
{
	std::map<int, std::map<std::string, GameObject*>>::iterator it = mGroups.find(group_id);
	if (it != mGroups.end())
	{
		std::map<std::string, GameObject*>::iterator it2 = it->second.find(object_name);
		if (it2 != it->second.end())
			return it2->second;
	}
	return NULL;
}


ssuge::GameObject * ssuge::GameObjectManager::getGameObject(std::string group_name, std::string object_name)
{
	std::map<std::string, int>::iterator it = mGroupNamesToID.find(group_name);
	if (it != mGroupNamesToID.end())
	{
		return getGameObject(it->second, object_name);
	}
	return NULL;
}



ssuge::GameObject * ssuge::GameObjectManager::getGameObject(std::string object_name)
{
	std::map<int, std::map<std::string, GameObject*>>::iterator it = mGroups.begin();
	while (it != mGroups.end())
	{
		std::map<std::string, GameObject*>::iterator it2 = it->second.find(object_name);
		if (it2 == it->second.end())
			return NULL;
		else
			return it2->second;
		it++;
	}
	return NULL;
}


void ssuge::GameObjectManager::destroyGameObject(int group_id, std::string object_name)
{
	std::map<int, std::map<std::string, GameObject*>>::iterator it = mGroups.find(group_id);
	if (it == mGroups.end())
		EXCEPTION("Undefined group: " + std::to_string(group_id));
	else
	{
		std::map<std::string, GameObject*>::iterator it2 = it->second.find(object_name);
		if (it2 != it->second.end())
		{
			delete it2->second;
			it->second.erase(it2);
		}
		else
			EXCEPTION("Game Object '" + object_name + "' not found in group#" + std::to_string(group_id));
	}
}



void ssuge::GameObjectManager::destroyGameObject(GameObject * g)
{
	std::map<int, std::map<std::string, GameObject*>>::iterator it = mGroups.begin();
	while (it != mGroups.end())
	{
		std::map<std::string, GameObject*>::iterator it2 = it->second.begin();
		while (it2 != it->second.end())
		{
			if (it2->second == g)
			{
				delete it2->second;
				it2 = it->second.erase(it2);
				return;
			}
			else
				++it2;
		}

		++it;
	}
}



int ssuge::GameObjectManager::getGroupID(std::string name)
{
	std::map<std::string, int>::iterator it = mGroupNamesToID.find(name);
	if (it != mGroupNamesToID.end())
		return it->second;
	else
		return -1;
}


void ssuge::GameObjectManager::createGroup(int id, std::string name)
{
	bool already_exists = false;
	std::map<std::string, int>::iterator it1 = mGroupNamesToID.find(name);
	std::map<int, std::string>::iterator it2 = mGroupIDsToNames.find(id);
	if (it1 != mGroupNamesToID.end() || it2 != mGroupIDsToNames.end())
		already_exists = true;

	if (already_exists)
		EXCEPTION("There is already a group with the name '" + name + "' or the id " + std::to_string(id));
	else
	{
		mGroupNamesToID[name] = id;
		mGroupIDsToNames[id] = name;
		mGroupHidden[id] = false;
		mGroups[id] = std::map<std::string, GameObject*>();
		mNextGroupNumber = id + 1;
	}
}



void ssuge::GameObjectManager::createGroup(std::string name)
{
	createGroup(mNextGroupNumber++, name);
}



void ssuge::GameObjectManager::destroyGroup(int id, bool only_delete_contents)
{
	std::map<int, std::map<std::string, GameObject*>>::iterator it = mGroups.find(id);
	if (it != mGroups.end())
	{
		// Delete the contents of the given sub-map
		std::map<std::string, GameObject*>::iterator it2 = it->second.begin();
		while (it2 != it->second.end())
		{
			delete it2->second;
			++it2;
		}
		it->second.clear();

		// If only_delete_contents is false, the user wants to remove this group as well
		if (!only_delete_contents)
		{
			mGroups.erase(it);
			std::map<int, std::string>::iterator it3 = mGroupIDsToNames.find(id);
			mGroupIDsToNames.erase(it3);
			std::string name = it3->second;
			std::map<std::string, int>::iterator it4 = mGroupNamesToID.find(name);	// Shouldn't ever fail.
			mGroupNamesToID.erase(it4);
			
		}
	}
}


void ssuge::GameObjectManager::setVisible(int id, bool is_visible)
{
	std::map<int, std::map<std::string, GameObject*>>::iterator it = mGroups.find(id);
	if (it != mGroups.end())
	{
		std::map<std::string, GameObject*>::iterator it2 = it->second.begin();
		while (it2 != it->second.end())
		{
			it2->second->setVisible(is_visible);
			++it2;
		}
		mGroupHidden[id] = is_visible;
	}
}



bool ssuge::GameObjectManager::getVisible(int id)
{
	std::map<int, bool>::iterator it = mGroupHidden.find(id);
	if (it != mGroupHidden.end())
		return it->second;
	else
		return false;
}


std::string ssuge::GameObjectManager::getGroupName(int id)
{
	std::map<int, std::string>::iterator it = mGroupIDsToNames.find(id);
	if (it != mGroupIDsToNames.end())
		return it->second;
	return "???";
}



void ssuge::GameObjectManager::update(float dt)
{
	std::map<int, std::map<std::string, GameObject*>>::iterator it = mGroups.begin();
	while (it != mGroups.end())
	{
		std::map<std::string, GameObject*>::iterator it2 = it->second.begin();
		while (it2 != it->second.end())
		{
			it2->second->update(dt);
			++it2;
		}
		++it;
	}
}




int ssuge::GameObjectManager::loadGroup(std::string fname)
{
	std::ifstream fp(fname);

	if (!fp.is_open())
		return 1;

	std::string group_name, path_name, extension;
	break_fname(fname, path_name, group_name, extension, true);
	createGroup(group_name);

	GameObject * gobj = NULL;
	std::string name;
	std::vector<std::string> parts;

	while (!fp.eof())
	{
		std::string line;
		std::getline(fp, line);
		if (line.length() == 0 || line[0] == '#')
			continue;

		if (line.length() > 2 && line[0] == '[' && line[line.length() - 1] == ']')
		{
			name = line.substr(1, line.length() - 2);
			// Create the game object
			gobj = createGameObject(group_name, name);
		}
		else if (gobj == NULL)
			continue;

		std::string temp = line.substr(0, 10);

		if (line.length() > 10 && line.substr(0, 10) == "component:")
		{
			split(line, parts);
			if (parts.size() == 2)
			{
				if (parts[1] == "camera")
				{
					CameraComponent * cc = gobj->createCameraComponent();
					cc->setClipDistances(0.5f, 10000.0f);
					cc->connectToViewport(APPLICATION->getViewport(0));
				}
			}
			else if (parts.size() == 3)
			{
				if (parts[1] == "mesh")
					gobj->createMeshComponent(parts[2]);
			}
			else if (parts.size() > 2 && parts[1] == "light")
			{
				LightComponent * lc = NULL;
				float x, y, z;
				sscanf_s(parts[3].c_str(), "%f", &x);
				sscanf_s(parts[4].c_str(), "%f", &y);
				sscanf_s(parts[5].c_str(), "%f", &z);
				if (parts[2] == "spotlight")
					lc = gobj->createLightComponent(LightType::SPOT);
				else if (parts[2] == "point")
					lc = gobj->createLightComponent(LightType::POINT);
				else if (parts[2] == "direction")
					lc = gobj->createLightComponent(LightType::DIRECTIONAL);
				
				if (parts.size() == 8 && parts[2] == "spotlight")
				{
					float ia, oa;
					sscanf_s(parts[6].c_str(), "%f", &ia);
					sscanf_s(parts[7].c_str(), "%f", &oa);
					lc->setSpotlightParams(ia, oa);
				}
				if (parts[2] == "direction" || parts[2] == "spotlight")
					lc->setDirection(Ogre::Vector3(x, y, z));
				if (parts[2] == "point")
					lc->setPositionOffset(Ogre::Vector3(x, y, z));

			}
			else if (parts.size() == 4)
			{
				if (parts[1] == "sound")
				{
					ssuge::SoundComponent * snd_comp = gobj->createSoundComponent(parts[3], parts[2] == "3d");
					snd_comp->setLooping(true);		// temporary!
					snd_comp->play();
				}
			}
		

			// component: light spotlight 0 -1 0 15.0 35.0
			// component: light point 50 0 0
			// component: light direction 0 -1 0
		}
		else if (line.length() > 9 && line.substr(0, 9) == "position:")
		{
			split(line, parts);
			if (parts.size() == 4)
			{
				float x, y, z;
				sscanf_s(parts[1].c_str(), "%f", &x);
				sscanf_s(parts[2].c_str(), "%f", &y);
				sscanf_s(parts[3].c_str(), "%f", &z);
				gobj->setPosition(Ogre::Vector3(x, y, z));
			}
		}
		else if (line.length() > 6 && line.substr(0, 6) == "scale:")
		{
			split(line, parts);
			if (parts.size() == 4)
			{
				float x, y, z;
				sscanf_s(parts[1].c_str(), "%f", &x);
				sscanf_s(parts[2].c_str(), "%f", &y);
				sscanf_s(parts[3].c_str(), "%f", &z);
				gobj->setScale(Ogre::Vector3(x, y, z));
			}
		}
		else if (line.length() > 12 && line.substr(0, 12) == "orientation:")
		{
			split(line, parts);
			if (parts.size() == 5)
			{
				float deg, x, y, z;
				sscanf_s(parts[1].c_str(), "%f", &deg);
				sscanf_s(parts[2].c_str(), "%f", &x);
				sscanf_s(parts[3].c_str(), "%f", &y);
				sscanf_s(parts[4].c_str(), "%f", &z);
				gobj->setOrientation(Ogre::Quaternion(Ogre::Degree(deg), Ogre::Vector3(x, y, z)));
			}
		}
		else if (line.length() > 7 && line.substr(0, 7) == "parent:")
		{
			split(line, parts);
			if (parts.size() == 2)
			{
				GameObject * parent = getGameObject(parts[1]);
				if (parent != NULL)
				{
					gobj->setParent(parent, false);
				}
			}
		}
		else if (line.length() > 7 && line.substr(0, 7) == "script:")
		{
			// A line like this:
			// script: ssuge.OgreHead blarg 3.14

			// Pick apart the line
			split(line, parts);
			if (parts.size() >= 2)
			{
				// Attempt to find the requested class within (python) ssuge
				PyObject * pclass = SCRIPT_MANAGER->findGlobal(parts[1]);
				if (pclass != NULL)
				{
					// Construct a init-args tuple for calling the given class.  This has to contain
					// the group name and name.  It can optionally take other parameters -- if anything else is
					// given on the line in the lvl script, use it for these optional parameters.
					PyObject * args = PyTuple_New(parts.size());
					PyTuple_SetItem(args, 0, PyUnicode_FromString(group_name.c_str()));
					PyTuple_SetItem(args, 1, PyUnicode_FromString(name.c_str()));
					for (unsigned int i = 2; i < parts.size(); i++)
					{
						if (is_integer(parts[i]))
							PyTuple_SetItem(args, i, PyLong_FromLong(to_integer(parts[i])));
						else if (is_double(parts[i]))
							PyTuple_SetItem(args, i, PyFloat_FromDouble(to_double(parts[i])));
						else
							PyTuple_SetItem(args, i, PyUnicode_FromString(parts[i].c_str()));
					}

					// Create the python game object
					PyObject * result = PyObject_CallObject(pclass, args);
					if (result == NULL)
						SCRIPT_MANAGER->handleError();
					else
					{
						// Have the c++ game object hang onto this reference.  Note: It "owns" this reference now
						// and should decref it if the game object goes out of scope.
						gobj->attachScriptObject(result);
					}

					// Decref the args tuple
					Py_DECREF(args);

					// Decref the pclass (findGlobals returned a new reference that we're now done with)
					Py_DECREF(pclass);
				}
			}
		}
	}

	return 0;
}