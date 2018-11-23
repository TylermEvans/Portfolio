#pragma once
#include <stdafx.h>
#include <exception.h>

namespace ssuge
{
	/// When a class is derived from Singleton, we can only have one instance (which must be created
	/// externally) and we get controlled global access (through the getSingletonPtr static method)
	template <class T>
	class Singleton
	{
	// @@@@@ ATTRIBUTES @@@@@
	protected:
		/// The pointer to the one and only instance (created elsewhere)
		static T * msSingleton;

	// @@@@@ CONSTRUCTORS / DESTRUCTORS @@@@@
	public:
		/// Constructor
		Singleton()
		{
			if (msSingleton != NULL)
				EXCEPTION("Singleton already exists!");
			msSingleton = (T*)this;
		}

		/// Destructor
		virtual ~Singleton()
		{
			msSingleton = NULL;
		}

		/// Gets the pointer to the singleton
		static T* getSingletonPtr()
		{
			if (msSingleton == NULL)
				EXCEPTION("Singleton doesn't exist!  You must create it externally.");
			return msSingleton;
		}
	};
}
