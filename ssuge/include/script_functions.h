#pragma once
#include <stdafx.h>
#include <Python.h>

namespace ssuge
{
	namespace script
	{
		/// A python wrapper around our log manager's log method
		/// usage: ssuge.log(string_to_log)
		/// usage: ssuge.log(string_to_log, time_on_display)
		PyObject * log(PyObject * module, PyObject * args);

		/// A python wrapper around our GOM's createGameObject method
		/// usage: ssuge.createGameObject("group-name", "object-name")
		PyObject * createGameObject(PyObject* module, PyObject * args);

		/// Creates a game object manager group
		/// usage: ssuge.createGroup("group-name")
		PyObject * createGroup(PyObject * module, PyObject * args);

		/// Loads an ini-style script from python
		/// usage: ssuge.loadIni("my_level.lvl")
		PyObject * loadIni(PyObject * module, PyObject * args);

		/// Runs a python script (from python!)
		/// usage: ssuge.loadScript("my_script.py")
		PyObject * loadScript(PyObject * module, PyObject * args);

		/// Returns a numeric value for a named axis
		/// usage: ssuge.getAxis("axis-name")
		PyObject * getAxis(PyObject * module, PyObject * args);

		/// Registers a python ssuge.GameObject-derived object as an input listener (so it will receive onAction and
		/// onAxis callbacks)
		/// usage: ssuge.registerInputListener(gobj)
		PyObject * registerInputListener(PyObject * module, PyObject * args);

		/// Shuts down the application
		/// usage: ssuge.shutdown()
		PyObject * shutdown(PyObject * module, PyObject * args);

		/// Sets the mouse-mode
		PyObject * setMouseMode(PyObject * module, PyObject * args);

		PyObject * getMousePos(PyObject * module, PyObject * args);

		PyObject * getRayIntersections(PyObject* module, PyObject * args);

		PyObject * destroyGameObject(PyObject* module, PyObject * args);

		
	}
}
