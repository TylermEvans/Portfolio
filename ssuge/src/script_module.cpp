#include <stdafx.h>
#include <script_functions.h>

// A hint telling the linker to look in another C file for this variable
extern PyTypeObject script_GameObjectType;


PyMethodDef ssuge_functions[] =
{
	{"log", ssuge::script::log, METH_VARARGS, "logs a message to the ssuge-log (using the C++ log manager"},
	{"getAxis", ssuge::script::getAxis, METH_VARARGS, "gets a named axis from an input device"},
	{"createGroup", ssuge::script::createGroup, METH_VARARGS, "Creates a game object manager group with the given name."},
	{"loadIni", ssuge::script::loadIni, METH_VARARGS, "Loads an ini-style script through the GameObjectManager" },
	{"loadScript", ssuge::script::loadScript, METH_VARARGS, "Loads and runs a python script"},
	{"registerInputListener", ssuge::script::registerInputListener, METH_VARARGS, "registers a game object as an input listener"},
	{"setMouseMode", ssuge::script::setMouseMode, METH_VARARGS, "changes the mouse mode"},
	{"shutdown", ssuge::script::shutdown, METH_VARARGS, "Shuts down the application"},
	{"getMousePosition", ssuge::script::getMousePos, METH_VARARGS, "gets the current mouse position" },
	{"getRayIntersections", ssuge::script::getRayIntersections, METH_VARARGS, "gets an array of the intersections from an input array to all collider components"},
	{"destroyGameObject", ssuge::script::destroyGameObject, METH_VARARGS, "destroys a game object"},
	{ NULL, NULL, 0, NULL }
};

struct PyModuleDef ssuge_definition =
{
	PyModuleDef_HEAD_INIT,
	"python ssuge module",
	"our embedded python ssuge scripting module",
	-1,
	ssuge_functions
};

PyMODINIT_FUNC PyInit_ssuge(void)
{
	PyObject * mod = PyModule_Create(&ssuge_definition);
	if (mod == NULL)
		return NULL;

	// Add the game object "class" to our module
	if (PyType_Ready(&script_GameObjectType) < 0)
		return NULL;
	Py_INCREF(&script_GameObjectType);
	PyModule_AddObject(mod, "GameObject", (PyObject*)&script_GameObjectType);

	return mod;
}
