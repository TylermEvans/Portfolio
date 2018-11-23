#pragma once
#include <stdafx.h>

namespace ssuge
{
	/// A simple Exception type for all ssuge-related errors
	class Exception
	{
	// @@@@@ ATTRIBUTES @@@@@
	protected:
		/// What happened?
		std::string mDescription;

		/// What file did it happen in?
		std::string mFilename;

		/// What line did it happen in the above file?
		unsigned int mLine;

	// @@@@@ CONTRUCTORS / DESTRUCTORS @@@@@
	public:
		/// Constructor
		Exception(std::string d, std::string f, unsigned int L) : mDescription(d), mFilename(f), mLine(L) { }

	// @@@@@ METHODS @@@@@
	public:
		/// Return a formatted string containing all error information
		std::string formatted_string() { return mFilename + "@" + std::to_string(mLine) + ":" + mDescription; }
	};
}

/// A convencince macro function to throw an exception and insert the current file / line.
#define EXCEPTION(desc) throw ssuge::Exception((desc), __FILE__, __LINE__)
