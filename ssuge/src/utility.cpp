#include <stdafx.h>
#include <utility.h>



bool ssuge::contains(std::string s, std::string sub_string)
{
	return s.find(sub_string) != std::string::npos;
}



void ssuge::break_fname(const std::string fname, std::string & path, std::string & name, std::string & extension, bool convert_to_lower)
{
	int eindex = fname.rfind(".");
	if (eindex < 0)
		extension = "";
	else
	{
		extension = fname.substr(eindex + 1, fname.length() - 1 - eindex);
		if (convert_to_lower)
		{
			for (unsigned int i = 0; i < extension.length(); i++)
				extension[i] = tolower(extension[i]);
		}
	}

	int pindex = fname.rfind("/");
	if (pindex < 0)
		pindex = fname.rfind("\\");
	if (pindex < 0)
		path = "";
	else
	{
		path = fname.substr(0, pindex + 1);
		if (convert_to_lower)
		{
			for (unsigned int i = 0; i < path.length(); i++)
				path[i] = tolower(path[i]);
		}
	}

	if (pindex < 0)
		pindex = 0;
	if (eindex < 0)
		eindex = fname.size() - 1;
	name = fname.substr(pindex + 1, eindex - pindex - 1);
	if (convert_to_lower)
	{
		for (unsigned int i = 0; i < name.length(); i++)
			name[i] = tolower(name[i]);
	}
}


void ssuge::split(const std::string & full_str, std::vector<std::string>& parts)
{
	parts.clear();
	std::string buffer = "";
	char temps[2] = { 0, 0 };
	for (unsigned int i = 0; i < full_str.length(); i++)
	{
		char c = full_str[i];
		if (isblank(c))
		{
			if (buffer.length() > 0)
			{
				parts.push_back(buffer);
				buffer = "";
			}
		}
		else
		{
			temps[0] = full_str[i];
			buffer += std::string(temps);
		}
	}

	if (buffer.length() > 0)
		parts.push_back(buffer);
}


void ssuge::split(const std::string & full_str, std::vector<std::string>& parts, const std::string & split_str)
{
	parts.clear();

	int n = split_str.size();
	std::string buffer;
	char temps[2] = { 0, 0 };

	for (unsigned int i = 0; i <= full_str.size() - n; i++)
	{
		if (full_str.substr(i, n) == split_str)
		{
			parts.push_back(buffer);
			buffer = "";
		}
		else
		{
			temps[0] = full_str[i];
			buffer += std::string(temps);
		}
	}
}


std::string ssuge::replace(const std::string & s, const std::string & cur_val, const std::string & new_val)
{
	unsigned int n = cur_val.size();
	unsigned int p = new_val.size();
	if (n > s.size())
		return s;

	char temps[2] = { 0, 0 };
	std::stringstream ss;
	for (unsigned int i = 0; i <= s.size() - p; i++)
	{
		if (s.substr(i, n) == cur_val)
			ss << new_val;
		else
		{
			temps[0] = s[i];
			ss << std::string(temps);
		}
	}

	return ss.str();
}



bool ssuge::is_integer(std::string s)
{
	for (unsigned int i = 0; i < s.size(); i++)
	{
		if (!isdigit(s[i]))
			return false;
	}
	return true;
}



int ssuge::to_integer(std::string s)
{
	return atoi(s.c_str());
}


bool ssuge::is_double(std::string s)
{
	for (unsigned int i = 0; i < s.size(); i++)
	{
		if (!isdigit(s[i]) && s[i] != '.' && s[i] != '+' && s[i] != '-')
			return false;
	}
	return true;
}


double ssuge::to_double(std::string s)
{
	return atof(s.c_str());
}



int ssuge::parseIniFile(std::string fname, std::vector<ssuge::IniSection> & data)
{
	data.clear();

	std::ifstream fp(fname);
	if (fp.is_open())
	{
		std::string line;
		std::getline(fp, line, '\n');
		while (!fp.eof())
		{
			if (line.size() == 0 || line[0] != '#')
			{
				int lpos = line.find("[");
				int rpos = line.find("]");
				int eq_pos = line.find("=");
				if (lpos != std::string::npos && rpos != std::string::npos)
				{
					// This is a section header
					std::string sec_name = line.substr(lpos + 1, rpos - lpos - 1);
					data.push_back(IniSection());
					data[data.size() - 1].mLabel = sec_name;
				}
				else if (eq_pos != std::string::npos)
				{
					// A key-value pair.  If this next condition is met, we have not seen our
					// first [sec-name] line -- We'll create a section called "default" for the user.  If the
					// condition is not met, just add to the current (last) section
					if (data.size() == 0)
					{
						data.push_back(IniSection());
						data[data.size() - 1].mLabel = "default";
					}

					std::string left = line.substr(0, eq_pos);
					std::string right = line.substr(eq_pos + 1, line.size() - eq_pos - 1);
					data[data.size() - 1].mPairs.push_back(std::pair<std::string, std::string>(left, right));
				}
			}

			std::getline(fp, line, '\n');
		}
		return 0;
	}
	else
		return 1;
}