#pragma once
#include <stdafx.h>
#include <Python.h>
#include <game_object.h>



typedef struct
{
	PyObject_HEAD
	ssuge::GameObject * mGameObject;
} script_GameObject;
