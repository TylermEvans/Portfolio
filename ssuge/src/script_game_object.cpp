#include <stdafx.h>
#include <script_game_object.h>
#include <structmember.h>
#include <game_object.h>
#include <application.h>
#include <gui_component.h>
#include <gui_manager.h>
#include <application.h>
#include <game_object_manager.h>

extern PyTypeObject script_GameObjectType;

PyObject * script_GameObject_new(PyTypeObject * type, PyObject * args, PyObject * kwargs)
{
	script_GameObject * obj = (script_GameObject*)type->tp_alloc(type, 0);
	obj->mGameObject = NULL;
	return (PyObject*)obj;
}


int script_GameObject_init(script_GameObject * self, PyObject* args, PyObject * kwargs)
{
	// The caller must provide two strings in args: the name of the group and the name of the object
	// They can, if they wish, provide extra arguments which will be forwarded to the onCreate method (if present)
	if (!PyTuple_Check(args) || PyTuple_Size(args) < 2 || !PyUnicode_Check(PyTuple_GetItem(args, 0)) ||
		!PyUnicode_Check(PyTuple_GetItem(args, 1)))
	{
		PyErr_SetString(PyExc_ValueError, "You must provide at least a group name (string) and object name (string) to this constructor");
		return NULL;
	}

	char * group_name = PyUnicode_AsUTF8(PyTuple_GetItem(args, 0));
	char * object_name = PyUnicode_AsUTF8(PyTuple_GetItem(args, 1));

	// First check to see if the given game object already exists (it might, if loaded from a lvl-type script)
	ssuge::GameObject * gobj = GAME_OBJECT_MANAGER->getGameObject(std::string(group_name), std::string(object_name));

	// If it doesn't already exist, create the c++ game object.
	if (gobj == NULL)
		gobj = GAME_OBJECT_MANAGER->createGameObject(std::string(group_name), std::string(object_name));

	// In either case make the python object's pointer point to it.
	self->mGameObject = gobj;

	// If the class used to instantiate this isn't ssuge.GameObject (but is a sub-type of it), make the c++ game object "script-aware".
	// Note: if this isn't true, it likely means the user was just creating a normal ssuge.GameObject (and probably doesn't want
	// it to be script aware)
	PyObject * self_type = PyObject_Type((PyObject*)self);
	if (PyType_IsSubtype((PyTypeObject*)self_type, &script_GameObjectType) && (void*)&script_GameObjectType != (void*)self_type)
	{
		gobj->attachScriptObject((PyObject*)self);

		// Pick out any extra elements in args, package as tuple (which is empty if only the group name and object name were passed)
		// and call the onCreate method of the sub-class (if there is one)
		PyObject * meth_args = PyTuple_GetSlice(args, 2, PyTuple_Size(args));
		gobj->callScriptMethod("onCreate", meth_args);
		Py_DECREF(meth_args);
	}
	Py_DECREF(self_type);

	

	return 0;
}



PyObject * script_GameObject_str(script_GameObject * self)
{
	return PyUnicode_FromString("temporary...");
}



void script_GameObject_dealloc(script_GameObject * self)
{
	// Make the c++ game object script un-aware
	if (self->mGameObject != NULL)
		self->mGameObject = NULL;
}



PyObject* script_GameObject_addChild(script_GameObject * self, PyObject * args, PyObject * kwargs)
{
	if (!PyTuple_Check(args) || PyTuple_Size(args) != 1 || !PyObject_IsInstance(PyTuple_GetItem(args, 0), (PyObject*)&script_GameObjectType))
	{
		PyErr_SetString(PyExc_TypeError, "You must pass a ssuge.GameObject (or derived class) instance to this method");
		return NULL;
	}

	script_GameObject * child = (script_GameObject*)PyTuple_GetItem(args, 0);

	child->mGameObject->setParent(self->mGameObject, true);

	Py_INCREF(Py_None);
	return Py_None;
}



PyObject* script_GameObject_createMeshComponent(script_GameObject * self, PyObject * args, PyObject * kwargs)
{
	if (!PyTuple_Check(args) || PyTuple_Size(args) != 1 || !PyUnicode_Check(PyTuple_GetItem(args, 0)))
	{
		PyErr_SetString(PyExc_ValueError, "You must pass a mesh file name");
		return NULL;
	}

	char * fname = PyUnicode_AsUTF8(PyTuple_GetItem(args, 0));
	self->mGameObject->createMeshComponent(std::string(fname));
	Py_INCREF(Py_None);
	return Py_None;
}

PyObject* script_GameObject_createGuiComponent(script_GameObject * self, PyObject * args, PyObject * kwargs) {
	char * fname = PyUnicode_AsUTF8(PyTuple_GetItem(args, 0));
	bool img = PyFloat_AsDouble(PyTuple_GetItem(args, 1));
	ssuge::GuiComponent * gui = self->mGameObject->createGuiComponent(std::string(fname), img);
	GUI_MANAGER->addGuiComponent(std::string(fname), gui);
	Py_INCREF(Py_None);
	return Py_None;
}
PyObject* script_GameObject_createColliderComponent(script_GameObject * self, PyObject * args, PyObject * kwargs) {
	float vx = PyFloat_AsDouble(PyTuple_GetItem(args, 0));
	float vy = PyFloat_AsDouble(PyTuple_GetItem(args, 1));
	float vz = PyFloat_AsDouble(PyTuple_GetItem(args, 2));
	float radius = PyFloat_AsDouble(PyTuple_GetItem(args, 3));
	Ogre::Vector3 vec(vx, vy, vz);
	self->mGameObject->createColliderComponent(vec, radius);
	Py_INCREF(Py_None);
	return Py_None;
}
PyObject* script_GameObject_removeColliderComponent(script_GameObject * self, PyObject * args, PyObject * kwargs) {
	char * name = PyUnicode_AsUTF8(PyTuple_GetItem(args, 0));
	COLLISION_MANAGER->removeComponent(name);
	Py_INCREF(Py_None);
	return Py_None;
}


PyObject* script_GameObject_createCameraComponent(script_GameObject * self, PyObject * args, PyObject * kwargs)
{
	if (!PyTuple_Check(args) || PyTuple_Size(args) != 1 || !PyLong_Check(PyTuple_GetItem(args, 0)))
	{
		PyErr_SetString(PyExc_ValueError, "You must pass a viewport index#");
		return NULL;
	}

	int vport_num = PyLong_AsLong(PyTuple_GetItem(args, 0));

	ssuge::CameraComponent * cc = self->mGameObject->createCameraComponent();
	cc->connectToViewport(APPLICATION->getViewport(vport_num));

	Py_INCREF(Py_None);
	return Py_None;
}



PyObject* script_GameObject_getParentPosition(script_GameObject * self, PyObject * args, PyObject * kwargs)
{
	if (!PyTuple_Check(args) || PyTuple_Size(args) != 0)
	{
		PyErr_SetString(PyExc_ValueError, "This method takes no arguments (besides self)");
		return NULL;
	}

	PyObject * rval = PyTuple_New(3);
	Ogre::Vector3 v = self->mGameObject->getPosition();
	PyTuple_SetItem(rval, 0, PyFloat_FromDouble((double)v.x));
	PyTuple_SetItem(rval, 1, PyFloat_FromDouble((double)v.y));
	PyTuple_SetItem(rval, 2, PyFloat_FromDouble((double)v.z));

	return rval;
}



PyObject* script_GameObject_getWorldPosition(script_GameObject * self, PyObject * args, PyObject * kwargs)
{
	if (!PyTuple_Check(args) || PyTuple_Size(args) != 0)
	{
		PyErr_SetString(PyExc_ValueError, "This method takes no arguments (besides self)");
		return NULL;
	}

	PyObject * rval = PyTuple_New(3);
	Ogre::Vector3 v = self->mGameObject->getWorldPosition();
	PyTuple_SetItem(rval, 0, PyFloat_FromDouble((double)v.x));
	PyTuple_SetItem(rval, 1, PyFloat_FromDouble((double)v.y));
	PyTuple_SetItem(rval, 2, PyFloat_FromDouble((double)v.z));

	return rval;
}


PyObject* script_GameObject_rotateWorld(script_GameObject * self, PyObject * args, PyObject * kwargs)
{
	if (!PyTuple_Check(args) || PyTuple_Size(args) != 4 || !PyNumber_Check(PyTuple_GetItem(args, 0)) ||
		!PyNumber_Check(PyTuple_GetItem(args, 1)) || !PyNumber_Check(PyTuple_GetItem(args, 2)) || !PyNumber_Check(PyTuple_GetItem(args, 3)))
	{
		PyErr_SetString(PyExc_ValueError, "You must pass 4 number parameters: degrees, x,y,z (axis)");
		return NULL;
	}

	PyObject * deg = PyNumber_Float(PyTuple_GetItem(args, 0));
	PyObject * x = PyNumber_Float(PyTuple_GetItem(args, 1));
	PyObject * y = PyNumber_Float(PyTuple_GetItem(args, 2));
	PyObject * z = PyNumber_Float(PyTuple_GetItem(args, 3));
	float cdeg = (float)PyFloat_AsDouble(deg);
	float cx = (float)PyFloat_AsDouble(x);
	float cy = (float)PyFloat_AsDouble(y);
	float cz = (float)PyFloat_AsDouble(z);
	Py_DECREF(deg);
	Py_DECREF(x);
	Py_DECREF(y);
	Py_DECREF(z);

	script_GameObject * sobj = (script_GameObject*)self;
	sobj->mGameObject->rotateWorld(cdeg, cx, cy, cz);

	Py_INCREF(Py_None);
	return Py_None;
}


PyObject* script_GameObject_setOrientation(script_GameObject * self, PyObject * args, PyObject * kwargs)
{
	if (!PyTuple_Check(args) || PyTuple_Size(args) != 4 || !PyNumber_Check(PyTuple_GetItem(args, 0)) ||
		!PyNumber_Check(PyTuple_GetItem(args, 1)) || !PyNumber_Check(PyTuple_GetItem(args, 2)) ||
		!PyNumber_Check(PyTuple_GetItem(args, 3)))
	{
		PyErr_SetString(PyExc_ValueError, "You must pass 4 number parameters: degrees,x,y,z (quaternion)");
		return NULL;
	}

	PyObject * deg = PyNumber_Float(PyTuple_GetItem(args, 0));
	PyObject * x = PyNumber_Float(PyTuple_GetItem(args, 1));
	PyObject * y = PyNumber_Float(PyTuple_GetItem(args, 2));
	PyObject * z = PyNumber_Float(PyTuple_GetItem(args, 3));
	float cdeg = (float)PyFloat_AsDouble(deg);
	float cx = (float)PyFloat_AsDouble(x);
	float cy = (float)PyFloat_AsDouble(y);
	float cz = (float)PyFloat_AsDouble(z);
	Py_DECREF(deg);
	Py_DECREF(x);
	Py_DECREF(y);
	Py_DECREF(z);

	script_GameObject * sobj = (script_GameObject*)self;
	sobj->mGameObject->setOrientation(cdeg, cx, cy, cz);

	Py_INCREF(Py_None);
	return Py_None;
}



PyObject* script_GameObject_setPosition(script_GameObject * self, PyObject * args, PyObject * kwargs)
{
	if (!PyTuple_Check(args) || PyTuple_Size(args) != 3 || !PyNumber_Check(PyTuple_GetItem(args, 0)) ||
		!PyNumber_Check(PyTuple_GetItem(args, 1)) || !PyNumber_Check(PyTuple_GetItem(args, 2)))
	{
		PyErr_SetString(PyExc_ValueError, "You must pass 3 number parameters: x,y,z (parent-position-offset)");
		return NULL;
	}

	PyObject * x = PyNumber_Float(PyTuple_GetItem(args, 0));
	PyObject * y = PyNumber_Float(PyTuple_GetItem(args, 1));
	PyObject * z = PyNumber_Float(PyTuple_GetItem(args, 2));
	float cx = (float)PyFloat_AsDouble(x);
	float cy = (float)PyFloat_AsDouble(y);
	float cz = (float)PyFloat_AsDouble(z);
	Py_DECREF(x);
	Py_DECREF(y);
	Py_DECREF(z);

	script_GameObject * sobj = (script_GameObject*)self;
	sobj->mGameObject->setPosition(cx, cy, cz);

	Py_INCREF(Py_None);
	return Py_None;
}



PyObject* script_GameObject_setPositionWorld(script_GameObject * self, PyObject * args, PyObject * kwargs)
{
	if (!PyTuple_Check(args) || PyTuple_Size(args) != 3 || !PyNumber_Check(PyTuple_GetItem(args, 0)) ||
		!PyNumber_Check(PyTuple_GetItem(args, 1)) || !PyNumber_Check(PyTuple_GetItem(args, 2)))
	{
		PyErr_SetString(PyExc_ValueError, "You must pass 3 number parameters: x,y,z (world position)");
		return NULL;
	}

	PyObject * x = PyNumber_Float(PyTuple_GetItem(args, 0));
	PyObject * y = PyNumber_Float(PyTuple_GetItem(args, 1));
	PyObject * z = PyNumber_Float(PyTuple_GetItem(args, 2));
	float cx = (float)PyFloat_AsDouble(x);
	float cy = (float)PyFloat_AsDouble(y);
	float cz = (float)PyFloat_AsDouble(z);
	Py_DECREF(x);
	Py_DECREF(y);
	Py_DECREF(z);

	script_GameObject * sobj = (script_GameObject*)self;
	sobj->mGameObject->setPositionWorld(cx, cy, cz);

	Py_INCREF(Py_None);
	return Py_None;
}


PyObject* script_GameObject_setScale(script_GameObject * self, PyObject * args, PyObject * kwargs)
{
	if (!PyTuple_Check(args) || PyTuple_Size(args) != 3 || !PyNumber_Check(PyTuple_GetItem(args, 0)) ||
		!PyNumber_Check(PyTuple_GetItem(args, 1)) || !PyNumber_Check(PyTuple_GetItem(args, 2)))
	{
		PyErr_SetString(PyExc_ValueError, "You must pass 3 number parameters: x,y,z (scale factor)");
		return NULL;
	}

	PyObject * x = PyNumber_Float(PyTuple_GetItem(args, 0));
	PyObject * y = PyNumber_Float(PyTuple_GetItem(args, 1));
	PyObject * z = PyNumber_Float(PyTuple_GetItem(args, 2));
	float cx = (float)PyFloat_AsDouble(x);
	float cy = (float)PyFloat_AsDouble(y);
	float cz = (float)PyFloat_AsDouble(z);
	Py_DECREF(x);
	Py_DECREF(y);
	Py_DECREF(z);

	script_GameObject * sobj = (script_GameObject*)self;
	sobj->mGameObject->setScale(cx, cy, cz);

	Py_INCREF(Py_None);
	return Py_None;
}



PyObject* script_GameObject_translateLocal(script_GameObject * self, PyObject * args, PyObject * kwargs)
{
	if (!PyTuple_Check(args) || PyTuple_Size(args) != 3 || !PyNumber_Check(PyTuple_GetItem(args, 0)) ||
		!PyNumber_Check(PyTuple_GetItem(args, 1)) || !PyNumber_Check(PyTuple_GetItem(args, 2)))
	{
		PyErr_SetString(PyExc_ValueError, "You must pass 3 number parameters: x,y,z (loca translation vector)");
		return NULL;
	}

	PyObject * x = PyNumber_Float(PyTuple_GetItem(args, 0));
	PyObject * y = PyNumber_Float(PyTuple_GetItem(args, 1));
	PyObject * z = PyNumber_Float(PyTuple_GetItem(args, 2));
	float cx = (float)PyFloat_AsDouble(x);
	float cy = (float)PyFloat_AsDouble(y);
	float cz = (float)PyFloat_AsDouble(z);
	Py_DECREF(x);
	Py_DECREF(y);
	Py_DECREF(z);

	script_GameObject * sobj = (script_GameObject*)self;
	sobj->mGameObject->translateLocal(cx, cy, cz);

	Py_INCREF(Py_None);
	return Py_None;
}


PyObject* script_GameObject_translateWorld(script_GameObject * self, PyObject * args, PyObject * kwargs)
{
	if (!PyTuple_Check(args) || PyTuple_Size(args) != 3 || !PyNumber_Check(PyTuple_GetItem(args, 0)) ||
		!PyNumber_Check(PyTuple_GetItem(args, 1)) || !PyNumber_Check(PyTuple_GetItem(args, 2)))
	{
		PyErr_SetString(PyExc_ValueError, "You must pass 3 number parameters: x,y,z (world translation vector)");
		return NULL;
	}

	PyObject * x = PyNumber_Float(PyTuple_GetItem(args, 0));
	PyObject * y = PyNumber_Float(PyTuple_GetItem(args, 1));
	PyObject * z = PyNumber_Float(PyTuple_GetItem(args, 2));
	float cx = (float)PyFloat_AsDouble(x);
	float cy = (float)PyFloat_AsDouble(y);
	float cz = (float)PyFloat_AsDouble(z);
	Py_DECREF(x);
	Py_DECREF(y);
	Py_DECREF(z);

	script_GameObject * sobj = (script_GameObject*)self;
	sobj->mGameObject->translateWorld(cx, cy, cz);

	Py_INCREF(Py_None);
	return Py_None;
}

PyObject * script_GameObject_setMaterial(script_GameObject* self, PyObject * args, PyObject * kwargs) {
	if (PyTuple_Size(args) == 2) {
		char * cname = PyUnicode_AsUTF8(PyTuple_GetItem(args, 0));
		float mval = PyFloat_AsDouble(PyTuple_GetItem(args, 1));
		self->mGameObject->getMeshComponent()->setMaterial(cname, mval);
	}
	else {
		char * cname = PyUnicode_AsUTF8(PyTuple_GetItem(args, 0));
		self->mGameObject->getMeshComponent()->setMaterial(cname);
	}
	Py_INCREF(Py_None);
	return Py_None;
}

PyObject * script_GameObject_setGuiText(script_GameObject* self, PyObject * args, PyObject * kwargs) {
	char * name = PyUnicode_AsUTF8(PyTuple_GetItem(args, 0));
	ssuge::GuiComponent * gui = self->mGameObject->getGuiComponent();
	gui->setText(std::string(name));
	Py_INCREF(Py_None);
	return Py_None;
}
PyObject * script_GameObject_dimensions(script_GameObject* self, PyObject * args, PyObject * kwargs) {
	float x = PyFloat_AsDouble(PyTuple_GetItem(args, 0));
	float y = PyFloat_AsDouble(PyTuple_GetItem(args, 1));
	ssuge::GuiComponent * gui = self->mGameObject->getGuiComponent();
	gui->setDimensions(x, y);
	Py_INCREF(Py_None);
	return Py_None;
}
PyObject * script_GameObject_position(script_GameObject* self, PyObject * args, PyObject * kwargs) {
	float x = PyFloat_AsDouble(PyTuple_GetItem(args, 0));
	float y = PyFloat_AsDouble(PyTuple_GetItem(args, 1));
	ssuge::GuiComponent * gui = self->mGameObject->getGuiComponent();
	gui->setPosition(x, y);
	Py_INCREF(Py_None);
	return Py_None;
}
PyObject * script_GameObject_charHeight(script_GameObject* self, PyObject * args, PyObject * kwargs) {
	float x = PyFloat_AsDouble(PyTuple_GetItem(args, 0));
	ssuge::GuiComponent * gui = self->mGameObject->getGuiComponent();
	gui->setCharHeight(x);
	Py_INCREF(Py_None);
	return Py_None;
}
PyObject * script_GameObject_setImage(script_GameObject* self, PyObject * args, PyObject * kwargs) {
	char * name = PyUnicode_AsUTF8(PyTuple_GetItem(args, 0));
	ssuge::GuiComponent * gui = self->mGameObject->getGuiComponent();
	gui->setImage(std::string(name));
	Py_INCREF(Py_None);
	return Py_None;
}
PyObject * script_GameObject_getCameraToViewportRay(script_GameObject* self, PyObject * args, PyObject * kwargs) {
	float x, y;
	x = PyFloat_AsDouble(PyTuple_GetItem(args, 0));
	y = PyFloat_AsDouble(PyTuple_GetItem(args, 1));
	Ogre::Ray r = APPLICATION->getRenderWindow()->getViewport(0)->getCamera()->getCameraToViewportRay(x, y);
	PyObject* newargs = PyTuple_New(6);
	PyTuple_SetItem(newargs, 0, PyFloat_FromDouble(r.getOrigin().x));
	PyTuple_SetItem(newargs, 1, PyFloat_FromDouble(r.getOrigin().y));
	PyTuple_SetItem(newargs, 2, PyFloat_FromDouble(r.getOrigin().z));
	PyTuple_SetItem(newargs, 3, PyFloat_FromDouble(r.getDirection().x));
	PyTuple_SetItem(newargs, 4, PyFloat_FromDouble(r.getDirection().y));
	PyTuple_SetItem(newargs, 5, PyFloat_FromDouble(r.getDirection().z));
	Py_IncRef(newargs);
	return newargs;	
}
PyObject * script_GameObject_getBoundingRad(script_GameObject* self, PyObject * args, PyObject * kwargs) {
	
		float rad = self->mGameObject->getMeshComponent()->getBoundingRad();
		PyObject * result = PyTuple_New(1);
		PyTuple_SetItem(result, 0, PyFloat_FromDouble(rad));
		Py_IncRef(result);
		return result;
	
}
PyObject * script_GameObject_getScale(script_GameObject* self, PyObject * args, PyObject* kwargs) {
	PyObject * results = PyTuple_New(3);
	Ogre::Vector3 vect = self->mGameObject->getScale();
	PyTuple_SetItem(results, 0, PyFloat_FromDouble(vect.x));
	PyTuple_SetItem(results, 1, PyFloat_FromDouble(vect.y));
	PyTuple_SetItem(results, 2, PyFloat_FromDouble(vect.z));
	Py_IncRef(results);
	return results;

}
PyObject * script_GameObject_setSpherePosition(script_GameObject* self, PyObject * args, PyObject * kwargs) {
	float x = PyFloat_AsDouble(PyTuple_GetItem(args, 0));
	float y = PyFloat_AsDouble(PyTuple_GetItem(args, 1));
	float z = PyFloat_AsDouble(PyTuple_GetItem(args, 2));
	self->mGameObject->getColliderComponent()->setOrigin(Ogre::Vector3(x, y, z));
	Py_IncRef(Py_None);
	return Py_None;
}
PyObject * script_GameObject_setSphereRadius(script_GameObject* self, PyObject * args, PyObject * kwargs) {
	float rad = PyFloat_AsDouble(PyTuple_GetItem(args, 0));
	self->mGameObject->getColliderComponent()->setRadius(rad);
	Py_IncRef(Py_None);
	return Py_None;
}
PyObject * script_GameObject_setMeshVisible(script_GameObject* self, PyObject * args, PyObject *kwargs) {
	bool val = PyLong_AsLong(PyTuple_GetItem(args, 0));
	self->mGameObject->getMeshComponent()->setVisible(val);
	Py_INCREF(Py_None);
	return Py_None;
}

PyMemberDef script_GameObject_members[] =
{
	{ NULL }
};


PyMethodDef script_GameObject_methods[] =
{
	{"addChild", (PyCFunction)script_GameObject_addChild, METH_VARARGS, "adds the passed child game object as a child of this game object."},
	{"createMeshComponent", (PyCFunction)script_GameObject_createMeshComponent, METH_VARARGS, "creates a mesh component on this game object"},
	{"createCameraComponent", (PyCFunction)script_GameObject_createCameraComponent, METH_VARARGS, "creates a camera component and attaches it to the given viewport #"},
	{"getParentPosition", (PyCFunction)script_GameObject_getParentPosition, METH_VARARGS, "gets this objects position relative to its parent" },
	{"getWorldPosition", (PyCFunction)script_GameObject_getWorldPosition, METH_VARARGS, "gets world-space position"},
	{"rotateWorld", (PyCFunction)script_GameObject_rotateWorld, METH_VARARGS, "rotates the game object (in world space)"},
	{"setOrientation", (PyCFunction)script_GameObject_setOrientation, METH_VARARGS, "sets the orientation of this game object"},
	{"setPositionParent", (PyCFunction)script_GameObject_setPosition, METH_VARARGS, "sets the position of this object (relative to the parent)"},
	{"setPositionWorld", (PyCFunction)script_GameObject_setPositionWorld, METH_VARARGS, "sets the position of this object (relative to the world)"},
	{"setScale", (PyCFunction)script_GameObject_setScale, METH_VARARGS, "scales this object (relative to current scale)"},
	{"translateLocal", (PyCFunction)script_GameObject_translateLocal, METH_VARARGS, "translates this object (relative to its local axes)"},
	{"translateWorld", (PyCFunction)script_GameObject_translateWorld, METH_VARARGS, "translates this object (relative to the world axes)" },
	{ "setMaterial", (PyCFunction)script_GameObject_setMaterial, METH_VARARGS, "sets the entitys material" },
	{"setGuiText", (PyCFunction)script_GameObject_setGuiText, METH_VARARGS, "sets a gui text compoenents text"},
	{ "setGuiDimensions", (PyCFunction)script_GameObject_dimensions, METH_VARARGS, "sets a gui components dimensions" },
	{ "setGuiPosition", (PyCFunction)script_GameObject_position, METH_VARARGS, "sets a gui components position" },
	{ "setGuiCharHeight", (PyCFunction)script_GameObject_charHeight, METH_VARARGS, "sets a gui text components char height" },
	{ "setGuiImage", (PyCFunction)script_GameObject_setImage, METH_VARARGS, "sets a gui image" },
	{ "createGuiComponent", (PyCFunction)script_GameObject_createGuiComponent, METH_VARARGS, "creates a gui component" },
	{"getCameraToViewportRay", (PyCFunction)script_GameObject_getCameraToViewportRay, METH_VARARGS, "gets a ray through the a screen pixel pos"},
	{"createColliderComponent", (PyCFunction)script_GameObject_createColliderComponent, METH_VARARGS, "creates a collider component"},
	{"getBoundingRad", (PyCFunction)script_GameObject_getBoundingRad, METH_VARARGS, "gets the bounding radius of the attacthed mesh"},
	{"getScale", (PyCFunction)script_GameObject_getScale, METH_VARARGS, "gets the gobj scale"},
	{"setSpherePosition", (PyCFunction)script_GameObject_setSpherePosition, METH_VARARGS, "sets the sphere colliders pos"},
	{"setSphereRadius", (PyCFunction)script_GameObject_setSphereRadius, METH_VARARGS, "sets the sphere colliders radius"},
	{"setMeshVisible", (PyCFunction)script_GameObject_setMeshVisible, METH_VARARGS, "sets the mesh to be visible or not"},
	{"removeColliderComponent", (PyCFunction)script_GameObject_removeColliderComponent, METH_VARARGS, "removes the collider component attatched to game object"},
	{ NULL, NULL, 0, NULL }
};



PyTypeObject script_GameObjectType =
{
	PyVarObject_HEAD_INIT(NULL, 0)					// Initializes the header-stuff
	"python GameObject class",						// tp_name
	sizeof(script_GameObject),						// tp_basicsize
	0,												// tp_itemsize
	(destructor)script_GameObject_dealloc,			// tp_dealloc
	0,												// tp_print
	0,												// tp_getattr
	0,												// tp_setattr
	0,												// tp_reserved
	0,												// tp_repr
	0,												// tp_as_number
	0,												// tp_as_sequence
	0, 												// tp_as_mapping
	0,												// tp_hash
	0,												// tp_call
	(reprfunc)script_GameObject_str,				// tp_str
	0,												// tp_getattro
	0,												// tp_setattro
	0,												// tp_as_buffer
	Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,		// tp_flags
	"ssuge GameObject wrapper",						// tp_doc
	0,												// tp_traverse
	0,												// tp_clear
	0,												// tp_richcompare
	0,												// tp_weaklistoffset
	0,												// tp_iter
	0,												// tp_iternext
	script_GameObject_methods,						// tp_methods
	script_GameObject_members,						// tp_members
	0,												// tp_getset
	0,												// tp_base
	0,												// tp_dict
	0,												// tp_descr_get
	0,												// tp_descr_set
	0,												// tp_dictoffset
	(initproc)script_GameObject_init,				// tp_init
	0,												// tp_alloc
	script_GameObject_new,							// tp_new
													// (there are more, we just needed to get down to tp_new...)
};