#include <stdafx.h>
#include <script_functions.h>
#include <log_manager.h>
#include <game_object_manager.h>
#include <script_game_object.h>
#include <script_manager.h>
#include <input_manager.h>
#include <application.h>
#include <collision_manager.h>

extern PyTypeObject script_GameObjectType;

/*PyObject * ssuge::script::createGameObject(PyObject* module, PyObject * args)
{
	// Check for errors
	if (!PyTuple_Check(args) || PyTuple_Size(args) != 2 || !PyUnicode_Check(PyTuple_GetItem(args, 0)) ||
		!PyUnicode_Check(PyTuple_GetItem(args, 1)))
	{
		PyErr_SetString(PyExc_ValueError, "You must pass a (string) group name and (string) object name");
		return NULL;
	}

	// Get C parameters from python
	char * group_name = PyUnicode_AsUTF8(PyTuple_GetItem(args, 0));
	char * object_name = PyUnicode_AsUTF8(PyTuple_GetItem(args, 1));

	// Create a C++ game object
	ssuge::GameObject * gobj = GAME_OBJECT_MANAGER->createGameObject(std::string(group_name), std::string(object_name));

	// Create a ssuge game object and return it.
	// Reference: https://stackoverflow.com/questions/4163018/create-an-object-using-pythons-c-api
	PyObject * init_args = PyTuple_New(0);
	PyObject *python_gobj = PyObject_CallObject((PyObject *)&ssuge_GameObjectType, init_args);
	Py_DECREF(init_args);

	// Make connections between the python and C++ game objects
	gobj->attachScriptObject(python_gobj);
	((script_GameObject*)python_gobj)->mGameObject = gobj;

	return python_gobj;
}*/


PyObject * ssuge::script::log(PyObject * module, PyObject * args)
{
	if (!PyTuple_Check(args) || PyTuple_Size(args) < 1 || !PyUnicode_Check(PyTuple_GetItem(args, 0)))
	{
		PyErr_SetString(PyExc_ValueError, "You must call this method with at least one string argument.");
		return NULL;
	}

	char * cstr = PyUnicode_AsUTF8(PyTuple_GetItem(args, 0));

	if (PyTuple_Size(args) == 2 && PyNumber_Check(PyTuple_GetItem(args, 1)))
	{
		PyObject * num = PyNumber_Float(PyTuple_GetItem(args, 1));
		double cnum = PyFloat_AsDouble(num);
		Py_DECREF(num);

		LOG_MANAGER->log("[SCRIPT] " + std::string(cstr), (float)cnum);		// display on-screen too
	}
	else
		LOG_MANAGER->log("[SCRIPT] " + std::string(cstr));

	Py_INCREF(Py_None);
	return Py_None;
}




PyObject * ssuge::script::createGroup(PyObject * module, PyObject * args)
{
	if (!PyTuple_Check(args) || PyTuple_Size(args) != 1 || !PyUnicode_Check(PyTuple_GetItem(args, 0)))
	{
		PyErr_SetString(PyExc_ValueError, "You must call this method with one string argument.");
		return NULL;
	}

	char * cstr = PyUnicode_AsUTF8(PyTuple_GetItem(args, 0));

	GAME_OBJECT_MANAGER->createGroup(std::string(cstr));

	Py_INCREF(Py_None);
	return Py_None;
}


PyObject * ssuge::script::loadIni(PyObject * module, PyObject * args)
{
	if (!PyTuple_Check(args) || PyTuple_Size(args) != 1 || !PyUnicode_Check(PyTuple_GetItem(args, 0)))
	{
		PyErr_SetString(PyExc_ValueError, "You must call this method with one string argument.");
		return NULL;
	}

	char * cstr = PyUnicode_AsUTF8(PyTuple_GetItem(args, 0));

	// Actually load the group
	if (GAME_OBJECT_MANAGER->loadGroup(std::string(cstr)))
		LOG_MANAGER->log("Error loading ini file '" + std::string(cstr) + "'", SCRIPT_MANAGER->msTimeToShowScriptErrors);

	Py_INCREF(Py_None);
	return Py_None;
}



PyObject * ssuge::script::loadScript(PyObject * module, PyObject * args)
{
	if (!PyTuple_Check(args) || PyTuple_Size(args) != 1 || !PyUnicode_Check(PyTuple_GetItem(args, 0)))
	{
		PyErr_SetString(PyExc_ValueError, "You must call this method with one string argument.");
		return NULL;
	}

	char * cstr = PyUnicode_AsUTF8(PyTuple_GetItem(args, 0));

	// Actually run the script
	PyObject * result = SCRIPT_MANAGER->loadScript(std::string(cstr));
	if (result == NULL)
		LOG_MANAGER->log("Error loading script file from python: '" + std::string(cstr) + "'", SCRIPT_MANAGER->msTimeToShowScriptErrors);

	Py_INCREF(Py_None);
	return Py_None;
}


PyObject * ssuge::script::getAxis(PyObject * module, PyObject * args)
{
	if (!PyTuple_Check(args) || PyTuple_Size(args) != 2 || !PyUnicode_Check(PyTuple_GetItem(args, 0)) ||
		!PyLong_Check(PyTuple_GetItem(args, 1)))
	{
		PyErr_SetString(PyExc_ValueError, "You must call this method with one string argument [the name of the axis] and an integer [which axis].");
		return NULL;
	}

	// Get the name of the axis
	std::string axis_name = std::string(PyUnicode_AsUTF8(PyTuple_GetItem(args, 0)));
	int axis_num = PyLong_AsLong(PyTuple_GetItem(args, 1));

	// Return the value of the given axis (if it's defined) -- otherwise, raise an exception
	//if (INPUT_MANAGER->hasAxis(axis_name))
	//{
	return PyFloat_FromDouble((float)INPUT_MANAGER->getAxis(axis_name, axis_num));
	//}
	//else
	//{
	//	PyErr_SetString(PyExc_ValueError, ("unknown axis '" + axis_name + "'").c_str());
	//	return NULL;
	//}
}


PyObject * ssuge::script::registerInputListener(PyObject * module, PyObject * args)
{
	if (!PyTuple_Check(args) || PyTuple_Size(args) != 1 || !PyObject_IsInstance(PyTuple_GetItem(args, 0), (PyObject*)&script_GameObjectType))
	{
		PyErr_SetString(PyExc_TypeError, "You must pass a ssuge.GameObject-derived object to this function");
		return NULL;
	}

	script_GameObject * gobj = (script_GameObject*)PyTuple_GetItem(args, 0);

	INPUT_MANAGER->registerListener(gobj->mGameObject);

	Py_INCREF(Py_None);
	return Py_None;
}



PyObject * ssuge::script::shutdown(PyObject * module, PyObject * args)
{
	if (!PyTuple_Check(args) || PyTuple_Size(args) != 0)
	{
		PyErr_SetString(PyExc_ValueError, "You must call this method with no arguments.");
		return NULL;
	}

	APPLICATION->startShutdown();

	Py_INCREF(Py_None);
	return Py_None;
}
PyObject * ssuge::script::getMousePos(PyObject * module, PyObject * args) {

	Ogre::Vector2 mousePos = INPUT_MANAGER->getMousePosition();
	PyObject* tuple = PyTuple_New(2);
	PyTuple_SetItem(tuple, 0, PyFloat_FromDouble(mousePos.x));
	PyTuple_SetItem(tuple, 1, PyFloat_FromDouble(mousePos.y));
	Py_INCREF(tuple);
	return tuple;

}
PyObject * ssuge::script::getRayIntersections(PyObject * module, PyObject * args) {
	float x1 = PyFloat_AsDouble(PyTuple_GetItem(args, 0));
	float y1 = PyFloat_AsDouble(PyTuple_GetItem(args, 1));
	float z1 = PyFloat_AsDouble(PyTuple_GetItem(args, 2));
	float x2 = PyFloat_AsDouble(PyTuple_GetItem(args, 3));
	float y2 = PyFloat_AsDouble(PyTuple_GetItem(args, 4));
	float z2 = PyFloat_AsDouble(PyTuple_GetItem(args, 5));
	Ogre::Ray r = Ogre::Ray();
	r.setOrigin(Ogre::Vector3(x1,y1,z1));
	r.setDirection(Ogre::Vector3(x2, y2, z2).normalisedCopy());
	std::vector<float> distances = COLLISION_MANAGER->rayIntersections(r);
	PyObject * dists = PyTuple_New(distances.size());
	for (int i = 0; i < distances.size(); i++) {
		PyTuple_SetItem(dists, i, PyFloat_FromDouble(distances[i]));
	}
	Py_INCREF(dists);
	return dists;
}



PyObject * ssuge::script::setMouseMode(PyObject * module, PyObject * args)
{
	if (!PyTuple_Check(args) || PyTuple_Size(args) != 1 || !PyBool_Check(PyTuple_GetItem(args, 0)))
	{
		PyErr_SetString(PyExc_ValueError, "Pass ...");
		return NULL;
	}

	if (PyObject_IsTrue(PyTuple_GetItem(args, 0)))
		INPUT_MANAGER->setMouseMode(true);
	else
		INPUT_MANAGER->setMouseMode(false);

	Py_INCREF(Py_None);
	return Py_None;
}
PyObject * ssuge::script::destroyGameObject(PyObject * module, PyObject * args) {
	script_GameObject * obj = (script_GameObject*)PyTuple_GetItem(args, 0);
	GAME_OBJECT_MANAGER->destroyGameObject(obj->mGameObject);
	Py_DECREF(obj);
	Py_INCREF(Py_None);
	return Py_None;
}