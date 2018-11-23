package edu.ssu.slotsgame.Testers;

import edu.ssu.slotsgame.SpinButton;
import edu.ssu.slotsgame.logic.GameState;
import edu.ssu.slotsgame.logic.GameStateManager;
import org.junit.Test;
import org.junit.Assert;

public class SpinButtonTester
{

    @Test
    public void testSpinDisable()
    {
        //Test 1: Disable Spin Button
        //Assume currentState_ is set to GameState.READY

        SpinButton b = new SpinButton("SPIN");
        boolean state = b.isEnabled();
        GameStateManager.getInstance_().setCurrentState_(GameState.SPIN);
        String failStr = "Spin Button Test 1 (testSpinDisable: FAILED" + "(GameState) was" + state + ", should have been " + !b.isEnabled();
        Assert.assertEquals(failStr,!state,b.isEnabled());
        String passStr = "Spin Buttone Test Test 1 (testSpinDisable: PASSED " + "(isEnabled) is false";
        System.out.println(passStr);

    }

    @Test
    public void testSpinEnable()
    {
        //Test 2: Enable Spin Button
        //Assume currentState_ is set to GameState.SPIN
        SpinButton b = new SpinButton("SPIN");
        GameStateManager.getInstance_().setCurrentState_(GameState.SPIN);
        boolean state = b.isEnabled();
        GameStateManager.getInstance_().setCurrentState_(GameState.READY);
        String failStr = "Spin Buttone Test 2 (testSpinEnable: FAILED" + "(GameState) was "+state + ", should of been " + b.isEnabled();
        Assert.assertEquals(failStr,state,!b.isEnabled());
        String passStr = "Spin Buttone Test 2 (testSpinEnablel: PASSED " + "(isEnabled) is true";
        System.out.println(passStr);

    }




}
