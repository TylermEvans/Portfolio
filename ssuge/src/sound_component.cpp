#include <stdafx.h>
#include <sound_component.h>
#include <sound_manager.h>
#include <game_object.h>

ssuge::SoundComponent::SoundComponent(ssuge::GameObject * owner, std::string fname, bool is_3d) : ssuge::Component(owner)
{
	mSound = SOUND_MANAGER->instantiateSound(fname, is_3d);
	if (is_3d)
	{
		mSound->setPosition(SOUND_MANAGER->Vector3_to_vec3df(mOwner->getWorldPosition()));
	}
}



ssuge::SoundComponent::~SoundComponent()
{
	// Not really necessary?
	//if (mSound)
	//	mSound->drop();
}


void ssuge::SoundComponent::setVisible(bool is_visible)
{
	if (mSound)
		mSound->setIsPaused(is_visible);
}



void ssuge::SoundComponent::update(float dt)
{
	if (mSound)
	{
		Ogre::Vector3 v = mOwner->getWorldPosition();
		irrklang::vec3df iv = SOUND_MANAGER->Vector3_to_vec3df(v);
		mSound->setPosition(iv);
	}
}