#pragma once
#include <stdafx.h>

namespace ssuge
{
	/// Returns true if the given string contains at least one instance of the given sub-string
	bool contains(std::string s, std::string sub_string);

	/// Breaks a file name into parts (path, name and extension)
	void break_fname(const std::string fname, std::string & path, std::string & name, std::string & extension, bool covert_to_lower);

	/// Splits the given full_str into a vector of strings anywhere whitespace is found
	void split(const std::string & full_str, std::vector<std::string>& parts);

	/// Splits the given full_str into a vector of strings anywhere the split_str is found
	void split(const std::string & full_str, std::vector<std::string>& parts, const std::string & split_str);

	/// Returns a string copy of s with all occurrences of cur_val replaced with new_val
	std::string replace(const std::string & s, const std::string & cur_val, const std::string & new_val);

	/// Determines if the given string is convertable to an integer
	bool is_integer(std::string);

	/// Converts the given string to an integer (make sure to call is_integer first!)
	int to_integer(std::string);

	/// Determines if the given string is convertable to a double
	bool is_double(std::string);

	/// Converts the given string to a double (make sure to call is_double first!)
	double to_double(std::string);

	/// A structure used by parseIniFile
	typedef struct 
	{
		std::string mLabel;		/// The part in square-brackets indicating the section
		std::vector<std::pair<std::string, std::string>> mPairs;	// A list of key-value pairs
	}IniSection;

	/// Populates the passed dictionary with data from the given ini-style file.  Returns 0 on success.
	int parseIniFile(std::string fname, std::vector<IniSection> & data);
}
