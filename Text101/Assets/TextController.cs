using UnityEngine;
using UnityEngine.UI;
using System.Collections;

public class TextController : MonoBehaviour 
{

	public Text text;
	private enum States {cell,mirror,sheets_0,lock_0,cell_mirror,sheets_1,lock_1,freedom};
	private States mState;
	// Use this for initialization
	void Start () 
	{
		mState = States.cell;
	}
	
	// Update is called once per frame
	void Update () 
	{
		print (mState);
		if (mState == States.cell) {
			state_cell ();
		} else if (mState == States.sheets_0) {

			state_sheets_0 ();
		} else if (mState == States.mirror) {
			
			state_mirror ();
		} else if (mState == States.lock_0) {
			
			state_lock_0 ();
		} else if (mState == States.cell_mirror) {
			
			state_cell_mirror ();
		} else if (mState == States.sheets_1) {
			
			state_sheets_1 ();
		} else if (mState == States.lock_1) {
			
			state_lock_1 ();
		} else if (mState == States.freedom) {
			state_freedom();
		}


	}

	void state_cell()
	{
		text.text = "You awaken to find that you are in a dark cell. " +
			"This cell is decrepit and it seems to have been lost " +
				"to the ages. The cell is dark and forboding and the " +
				"only light is the light of the full moon coming  through a " +
				"high window. Occupying the room is a plain cot with dirty sheets " +
				"on it. You notice that there is also a dingy mirror on the wall. " +
				"The last thing you notice is the rusty gate that is the only thing keeping " +
				"you away from the freedom you desire.\n\n" +
				"Press S to view the dirty Sheets , Press M to look in the Mirror, Press L to view the Lock on the rusty door.";

		if (Input.GetKeyDown (KeyCode.S)) 
		{
			mState = States.sheets_0;
		}
		if (Input.GetKeyDown (KeyCode.M)) 
		{
			mState = States.mirror;
		}
		if (Input.GetKeyDown (KeyCode.L)) 
		{
			mState = States.lock_0;
		}



	}
	void state_sheets_0()
	{
		text.text = "You examine the sheets closely and you find it is hard " +
			"to make out the color of them in this dark cell. The one " +
			"thing you do notice however is the dark brownish-red stains that " +
			"seem to dot the sheet. It seems you have not been the first to suffer in this cell.\n\n" +
			" Press R to Return to investigating your cell";
		
		if (Input.GetKeyDown (KeyCode.R)) 
		{
			mState = States.cell;
		}
		
	}
	void state_mirror()
	{
		text.text = "You walk towards the mirror and examine it. " +
			"The moonlight shines off the mirror and in " +
			"the reflection you see a shattered image of " +
			"yourself. The mirror is broken. It and you " +
			"are looking rough around the edges.\n\n " +
			"Press R to Return to investigating your cell, " +
			"Press T to Take the mirror off the wall.";
		if (Input.GetKeyDown(KeyCode.R)) 
		{
			mState = States.cell;
		}
		if (Input.GetKeyDown (KeyCode.T)) 
		{
			mState = States.cell_mirror;

		}
		
	}
	void state_lock_0()
	{
		text.text = "You examine the door and you see that "+
					"the lock is rusted. A sharp object or " +
					"some brute force might be able to force it open.\n\n" + 
					"Press R to Return to investigating the Cell";
		
		if (Input.GetKeyDown (KeyCode.R)) 
		{
			mState = States.cell;
		}
		
	}
	void state_cell_mirror()
	{
		text.text = "You grab the mirror and take it off the wall " +
			"The mirror is not bolted down and it is easy " +
			"to lift.\n\n" +
			"Press S to examine the Sheets once more, "+
			"Press L to examine the locked door once more.";
		
		if (Input.GetKeyDown (KeyCode.S)) 
		{
			mState = States.sheets_1;
		}
		if (Input.GetKeyDown (KeyCode.L)) 
		{
			mState = States.lock_1;
		}


	}
	void state_lock_1()
	{
		text.text = "You walk over to the locked door and you " +
					"set the cracked mirror down in order to examine " +
					"the old rusted lock.\n\n" +
					"Press R to Return to wandering around the cell, " +
					"Press O to Try and force the lock open.";
		if (Input.GetKeyDown (KeyCode.R)) 
		{
			mState = States.cell_mirror;
		}
		if (Input.GetKeyDown (KeyCode.O)) 
		{
			mState = States.freedom;
		}
		
		
	}
	void state_sheets_1()
	{
		text.text = "You walk back over to the sheets and you look " +
			"for anything else of interests. You don't seem to find much.\n\n" +
			"Press R to Return to wandering the cell.";
		
		if (Input.GetKeyDown (KeyCode.R)) 
		{
			mState = States.cell_mirror;
		}
		
		
	}
	void state_freedom()
	{

		text.text = "You decide to take the mirror and smash the side of it against the " +
			"rusted lock. This action is succesfull. The lock shatters and the door " +
			"creaks open slowly. You slowly step outside the door and hope that " +
			"none of the guards heard the commotion. You have passed the first step " +
			"on your road to freedom. ";

	}

}
