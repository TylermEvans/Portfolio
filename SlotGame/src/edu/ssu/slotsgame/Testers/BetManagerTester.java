package edu.ssu.slotsgame.Testers;


import edu.ssu.slotsgame.config.GameParameters;
import edu.ssu.slotsgame.logic.BetManager;
import org.junit.Test;
import org.junit.Assert;



public class BetManagerTester {


    @Test
    public void testIncreaseBet()
    {
        // Test 1: increaseBet increases currentBet_ by one
        // assume MIN_BET < MAX_BET
        BetManager.getInstance_().curbet = GameParameters.MIN_BET;
        BetManager.getInstance_().increaseBet();
        String failStr = "Bet Manager Test 1 (increaseBet): FAILED " + "(curbet) was " + BetManager.getInstance_().curbet+ ", should have been "  + (GameParameters.MIN_BET + 1) + ")";
        Assert.assertEquals(failStr,BetManager.getInstance_().curbet,GameParameters.MIN_BET+1);
        String passStr = "Bet Manager Test 1 (increaseBet): PASSED"+ "(curbet) was increased by 1";
        System.out.println(passStr);
    }



    @Test
    public void testDecreaseBet()
    {
        //Test 2: increaseBet will not increase curbet if  it's already the maximum allowed
        // assume MIN_BET<MAX_BET
        BetManager.getInstance_().curbet = GameParameters.MAX_BET;
        BetManager.getInstance_().increaseBet();
        String failStr = "Bet Manager Test 2 (increaseBet): FAILED " + "(curbet) was " + BetManager.getInstance_().curbet + ", should have been " + (GameParameters.MAX_BET) + ")";

        Assert.assertEquals(failStr,BetManager.getInstance_().curbet ,GameParameters.MAX_BET);

        String passStr = "Bet Manager Test 2 (increaseBet): PASSED " + "(curbet) did not go above maximum";
        System.out.println(passStr);





    }
    @Test
    public void testMaxBet(){
        //Test 3: decreaseBet decreases curbet by one
        //assume MIN_BET < MAX_BET
        BetManager.getInstance_().curbet = GameParameters.MAX_BET;
        BetManager.getInstance_().decreaseBet();

        String failStr = "Bet Manager Test 3 (decreaseBet): FAILED " + "(curbet) was " + BetManager.getInstance_().curbet + ", should have been " + (GameParameters.MIN_BET + 1) + ")";

        Assert.assertEquals(failStr,BetManager.getInstance_().curbet, GameParameters.MAX_BET - 1);

        String passStr = "Bet Manager Test 3 (decreaseBet): PASSED " + "(curbet) was increased by 1";
        System.out.println(passStr);


    }
    @Test
    public void testMinBet()
    {
        //Test 4: decreaseBet will not decrease curbet if it's alredy the minimum allowed
        // assume MIN_BET < MAX_BET
        BetManager.getInstance_().curbet = GameParameters.MIN_BET;
        BetManager.getInstance_().decreaseBet();

        String failStr = "Bet Manager Test 4 (decreaseBet): FAILED " + "(curbet) was " + BetManager.getInstance_().curbet + ", should have been " + (GameParameters.MIN_BET) + ")";

        Assert.assertEquals(failStr,BetManager.getInstance_().curbet,GameParameters.MIN_BET);

        String passStr = "Bet Manager Test 4 (decreaseBet): PASSED " + "(curbet) did no go below the minimum ";
        System.out.println(passStr);
    }

}
