#pragma once
#include <sstream>

template<typename T>
string str(const T& v) {
	std::ostringstream iss;
	iss << v;
	return iss.str();
}

