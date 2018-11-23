#include <stdafx.h>
#include <script_manager.h>
#include <Python.h>
#include <log_manager.h>

// Inialize the static singleton variable
template<>
ssuge::ScriptManager * ssuge::Singleton<ssuge::ScriptManager>::msSingleton = NULL;

// Initialize the static error-log time variable.
const float ssuge::ScriptManager::msTimeToShowScriptErrors = 30.0f;

// Defined in script_module.cpp
PyMODINIT_FUNC PyInit_ssuge(void);

ssuge::ScriptManager::ScriptManager()
{
	// Loads our "ssuge" module to the interpreter (this prevents us
	// from having to "import ssuge" everywhere).  This must be called
	// before Py_Initialize
	int rv = PyImport_AppendInittab("ssuge", &PyInit_ssuge);

	// From justinwatson.name/2017/03/21/Embedding_Python_in_C++.html
	// Make python look in this file for all the modules (normally in the Libs folder of a python install)
	Py_SetPath(L".\\python36.zip");
	
	// Starts the internal interpreter
	Py_InitializeEx(0);
}



ssuge::ScriptManager::~ScriptManager()
{
	// Shutdown the internal interpreter
	Py_Finalize();
}



PyObject * ssuge::ScriptManager::loadScript(std::string fname)
{
	// See if we have that script already cached
	std::map<std::string, PyObject*>::iterator it = mModules.find(fname);
	if (it != mModules.end())
		return it->second;

	// Part I: Load the file into a char-buffer
	std::fstream fp;
	unsigned int file_size;
	char* buffer = NULL;

	// Determine the file size
	fp.open(fname, std::ios::in | std::ios::binary);
	if (!fp.is_open() || !fp.good())
		return NULL;

	fp.seekg(0L, std::ios::end);
	file_size = (unsigned int)fp.tellg();
	fp.seekg(0L, std::ios::beg);

	// Read the contents of the file
	buffer = new char[file_size + 1];
	if (buffer)
	{
		fp.read(buffer, file_size);
		buffer[(int)fp.tellg()] = 0;
	}
	fp.close();

	if (!buffer)
		return NULL;

	// Part II: Compile the char-buffer into a byte-code object.
	PyObject * byteCode = Py_CompileString(buffer, fname.c_str(), Py_file_input);
	if (byteCode == NULL)
	{
		handleError();
		return NULL;
	}

	// Part III: Execute the byte-code object
	PyObject * module = PyImport_ExecCodeModule((char*)fname.c_str(), byteCode);
	Py_DECREF(byteCode);
	if (module)
		mModules[fname] = module;
	else
		handleError();

	return module;
}


void ssuge::ScriptManager::handleError()
{
	std::string errString;
	int i, len;
	std::stringstream rvStream;
	PyObject * pErrType, *pErrValue, *pErrTraceback, *pErrString, *pTemp, *pModule = NULL;
	PyObject * pFunc = NULL, *pArgs = NULL, *pValue;
	PyObject * errData[3];     // To avoid a bunch of copy-pasting when calling (python) format_exception below

	PyErr_Fetch(&pErrType, &pErrValue, &pErrTraceback);
	PyErr_NormalizeException(&pErrType, &pErrValue, &pErrTraceback);

	errData[0] = pErrType;
	errData[1] = pErrValue;
	errData[2] = pErrTraceback;

	//rvStream << "ERROR: ";

	// Reference: http://www.gossamer-threads.com/lists/python/python/150924
	/*if (pErrValue)
	{
		// Get the type of error
		rvStream << "ErrorType: '";
		pTemp = PyObject_Str(pErrType);
		if (pTemp != NULL)
		{
			rvStream << PyUnicode_AsUTF8(pTemp);
			Py_DECREF(pTemp);
		}
		rvStream << "' ";
	}*/

	rvStream << std::endl;

	// Get the error description
	rvStream << "ErrorValue: \"";
	pErrString = PyObject_Str(pErrValue);
	if (pErrString)
	{
		pTemp = PyUnicode_AsUTF8String(pErrString);
		if (pTemp)
		{
			// This is the error description...
			rvStream << std::string(PyBytes_AsString(pTemp));
			Py_DECREF(pTemp);
		}
		Py_DECREF(pErrString);
	}
	rvStream << "\"";

	// Import traceback info
	pTemp = PyUnicode_FromString("traceback");
	if (pTemp)
	{
		pModule = PyImport_Import(pTemp);
		Py_DECREF(pTemp);
	}
	if (pModule)
	{
		// Note: see the "traceback" module in the (normal) python docs.
		// The traceback module should have a format_exception function which returns a list
		// of (python) string objects.  These represent the "callstack" errors.
		pFunc = PyObject_GetAttrString(pModule, "format_exception");
		if (pFunc)
		{
			// Construct an arguments tuple with one element: the traceback object from above
			pArgs = PyTuple_New(3);
			if (pArgs)
			{
				// Note: Inserting an item in a tuple steals a reference.  So...INCREF all 3 of them
				// if they're not NULL so the final Py_XDECREF won't fail.
				for (i = 0; i<3; i++)
				{
					if (errData[i])
					{
						Py_INCREF(errData[i]);
						PyTuple_SetItem(pArgs, i, errData[i]);
					}
					else
					{
						Py_INCREF(Py_None);
						PyTuple_SetItem(pArgs, i, Py_None);
					}
				}

				// Now, call the format_tb function, which should return a list of strings
				pValue = PyObject_CallObject(pFunc, pArgs);
				if (pValue != NULL)
				{
					len = PyList_Size(pValue);
					if (len > 0)
						rvStream << "\nStack: \n";
					for (i = 0; i<len; i++)
					{
						// Note: PyList_GetItem returns a borrowed reference, so there's no need to adjust
						// the ref-counts.
						rvStream << PyUnicode_AsUTF8(PyList_GetItem(pValue, i)) << "\n";
					}
					Py_DECREF(pValue);
				}
				Py_DECREF(pArgs);
			}
			Py_DECREF(pFunc);
		}
		Py_DECREF(pModule);
	}


	errString = rvStream.str();

	Py_XDECREF(pErrValue);
	Py_XDECREF(pErrType);
	Py_XDECREF(pErrTraceback);

	LOG_MANAGER->log(errString, msTimeToShowScriptErrors);
}



PyObject * ssuge::ScriptManager::findGlobal(std::string s)
{
	// Import ssuge here
	PyObject * module_name = PyUnicode_FromString("ssuge");
	PyObject * ssuge_mod = PyImport_Import(module_name);
	Py_DECREF(module_name);

	if (ssuge_mod != NULL)
	{
		// Now try to access the requested ssuge-global variable
		if (PyObject_HasAttrString(ssuge_mod, s.c_str()))
			return PyObject_GetAttrString(ssuge_mod, s.c_str());
	}
	return NULL;
}