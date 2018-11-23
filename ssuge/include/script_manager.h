#pragma once
#include <stdafx.h>
#include <singleton.h>
#include <Python.h>

#define SCRIPT_MANAGER ssuge::ScriptManager::getSingletonPtr()

namespace ssuge
{
	/// The ScriptManager class is responsible for housing our embedded interpreter as well
	/// as functionality to load and execute python scripts.
	class ScriptManager : public Singleton<ScriptManager>
	{
	// @@@@@ ATTRIBUTES @@@@@
	protected:
		/// The named (by filename / path) list of modules we've already loaded (so we don't have to constantly re-build them)
		std::map<std::string, PyObject*> mModules;

	public:
		/// How long do we show script-related errors message in the in-game console?
		static const float msTimeToShowScriptErrors;

	// @@@@@ CONSTRUCTORS / DESTRUCTORS @@@@@
	public:
		/// Constructor
		ScriptManager();

		/// Destructor
		~ScriptManager();

	// @@@@@ METHODS @@@@@
	public:
		/// Load a python script from the given path / filename (and cache the module in mModules)
		PyObject * loadScript(std::string fname);

		/// Prints a stack trace to the screen (and on-screen) using the log manager
		void handleError();

		/// Returns a global object from the python ssuge module (or NULL if it doesn't exist).  This is primarily
		/// used to find a python class which can then be used by the GOM to instantiate a new python object.  Note: it
		/// is the caller's responsibility to decref this object (if not null) when done.
		PyObject * findGlobal(std::string s);
	};
}
