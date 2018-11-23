#pragma once
#include <stdafx.h>
#include <singleton.h>

#define SOUND_MANAGER ssuge::SoundManager::getSingletonPtr()

namespace ssuge
{
	// Forward declarations
	class GameObject;
	class SoundComponent;

	/// The SoundManager is used as a factory to create sound components.  I made this (but not for most other
	/// components) a manager / Factory because there are some centrally-located methods (like setting the listener)
	/// that I though made more sense here.
	class SoundManager : public Singleton<SoundManager>
	{
	// @@@@@ ATTRIBUTES @@@@@
	protected:
		/// The irrklang sound engine
		irrklang::ISoundEngine* mSoundEngine;

		/// The 3d sound listener (if not set, (0,0,0) is assumed)
		ssuge::GameObject * mListener;

	// @@@@@ CONSTRUCTORS / DESTRUCTUOR @@@@@
	public:
		/// Constructor
		SoundManager();

		/// Destructor
		~SoundManager();

	// @@@@@ METHODS @@@@@
	public:
		/// Makes this game object the listener for 3d sound effects -- in our update method, we poll this objects current position.
		void setActiveListener(GameObject * gobj);

		/// Should be called once per frame.
		void update(float dt);

	// @@@@@ UTILITY FUNCTIONS @@@@@
	public:
		/// Convert an irrklang::vec3df to an Ogre::Vector3
		static const Ogre::Vector3 vec3df_to_Vector3(const irrklang::vec3df & v) { return Ogre::Vector3(v.X, v.Y, v.Z); }

		/// Convert an Ogre::Vector3 to an irrklang::vec3df
		static const irrklang::vec3df Vector3_to_vec3df(const Ogre::Vector3 & v) { return irrklang::vec3df(v.x, v.y, v.z); }

	// @@@@@ METHODS only available to SoundComponents @@@@@
	protected:
		/// Gets the sound engine (probably not necessary?)
		irrklang::ISoundEngine* getSoundEngine() { return mSoundEngine; }

		/// Creates a sound instance
		irrklang::ISound * instantiateSound(std::string fname, bool is_3d);

	// @@@@@ FRIENDS @@@@@
		friend class SoundComponent;
	};
}