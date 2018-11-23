#include <stdafx.h>
#include <sound_manager.h>
#include <sound_component.h>
#include <game_object.h>

// The template-specialization to declare the singleton variable for the LogManager class
template<> ssuge::SoundManager* ssuge::Singleton<ssuge::SoundManager>::msSingleton = NULL;


ssuge::SoundManager::SoundManager() : mSoundEngine(NULL), mListener(NULL)
{
	mSoundEngine = irrklang::createIrrKlangDevice();
	mSoundEngine->setDefault3DSoundMinDistance(1.0f);
	mSoundEngine->setDefault3DSoundMaxDistance(100.0f);
}



ssuge::SoundManager::~SoundManager()
{
	if (mSoundEngine)
		mSoundEngine->drop();
}




void ssuge::SoundManager::setActiveListener(ssuge::GameObject * gobj)
{
	mListener = gobj;
}



void ssuge::SoundManager::update(float dt)
{
	if (mListener)
	{
		Ogre::Vector3 v = mListener->getWorldPosition();
		irrklang::vec3df iv = SoundManager::Vector3_to_vec3df(v);
		mSoundEngine->setListenerPosition(iv, irrklang::vec3df(0, 0, 1));
	}
}



irrklang::ISound * ssuge::SoundManager::instantiateSound(std::string fname, bool is_3d)
{
	if (is_3d)
		return mSoundEngine->play3D(fname.c_str(), irrklang::vec3df(0, 0, 0), false, true, true);
	else
		return mSoundEngine->play2D(fname.c_str(), false, true, true);
}