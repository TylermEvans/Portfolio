#pragma once
#include <stdafx.h>
#include <component.h>

namespace ssuge
{
	// Forward reference to game object class
	class GameObject;

	/// The SoundComponent class is used to attach a 3d or 2d sound to a game object
	class SoundComponent : public Component
	{
	// @@@@@ ATTRIBUTES @@@@@
	protected:
		/// The irrklang sound instance pointer.
		irrklang::ISound * mSound;

	// @@@@@ CONSTRUCTORS / DESTRUCTOR @@@@@
	public:
		/// The constructor
		SoundComponent(GameObject * owner, std::string fname, bool is_3d);

		/// The destructor
		~SoundComponent();

	// @@@@@ OVERRIDES from COMPONENT @@@@@
	public:
		/// Returns the type of this component.
		ComponentType getType() { return ComponentType::SOUND; }

		/// Makes this sound stop playing if is_visible if false.
		void setVisible(bool is_visible) override;

		/// Update the sound position
		void update(float dt) override;

	// @@@@@ METHODS @@@@@
	public:
		/// Make this sound loop if is_looping is set to true.
		void setLooping(bool is_looping) { mSound->setIsLooped(is_looping); }

		/// Makes this sound start playing
		void play() { mSound->setIsPaused(false); }

		/// Pauses this sound.
		void stop() { mSound->setIsPaused(true); }
	};
}
