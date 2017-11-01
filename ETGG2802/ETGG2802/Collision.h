#pragma once
#include <vector>
bool collision(float x, float z, vector<vec3>&cpos) {
	bool collide = false;
	for (int i = 0; i < cpos.size(); ++i) {
		if (x >= cpos.at(i).x - 1.1 && x <= cpos.at(i).x + 1.1 && z >= cpos.at(i).z - 1.1 && z <= cpos.at(i).z + 1.1) {

			collide = true;
		}

	}
	return collide;
}
