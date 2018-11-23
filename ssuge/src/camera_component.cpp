#include <stdafx.h>
#include <camera_component.h>
#include <game_object.h>
#include <application.h>

ssuge::CameraComponent::CameraComponent(GameObject * owner) : Component(owner)
{
	mCamera = APPLICATION->getSceneManager()->createCamera(owner->getName() + "_camera" + std::to_string(owner->getNumComponents(ComponentType::CAMERA)));
	owner->getSceneNode()->attachObject(mCamera);
	mCamera->setAutoAspectRatio(true);
	mCamera->setNearClipDistance(0.1f);
	mCamera->setFarClipDistance(1000.0f);
}


ssuge::CameraComponent::~CameraComponent()
{
	if (mCamera)
	{
		if (mCamera->getParentSceneNode())
			mCamera->getParentSceneNode()->detachObject(mCamera);
		APPLICATION->getSceneManager()->destroyCamera(mCamera);
	}
}
