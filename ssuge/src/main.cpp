#include <stdafx.h>
#include <application.h>

int main(int argc, char ** argv)
{
	ssuge::Application app;
	
	app.initApp();
	app.getRoot()->startRendering();
	app.closeApp();

	return 0;
}