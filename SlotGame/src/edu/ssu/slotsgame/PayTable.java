package edu.ssu.slotsgame;
import edu.ssu.slotsgame.logic.BetManager;

import java.util.*;

public class PayTable {

    private static HashMap<String,ArrayList> payTable = new HashMap<>();
    private final static PayTable instance = new PayTable();


    public PayTable()
    {
        ArrayList<Integer> tmp = new ArrayList<>();

        tmp.add(0);
        tmp.add(5);
        tmp.add(10);

        payTable.put("cherry",tmp);

        tmp = new ArrayList<>();

        tmp.add(0);
        tmp.add(10);
        tmp.add(15);

        payTable.put("bell",tmp);

        tmp = new ArrayList<>();

        tmp.add(0);
        tmp.add(5);
        tmp.add(10);

        payTable.put("watermelon",tmp);

        tmp = new ArrayList<>();

        tmp.add(0);
        tmp.add(10);
        tmp.add(15);

        payTable.put("bar",tmp);


    }

    public int getPayout(String name, int matchnum)
    {


        int result = (int)payTable.get(name).get(matchnum - 1) * BetManager.getInstance_().curbet;
        return result;

    }

    public static PayTable getInstance(){
        return instance;
    }

    public static HashMap<String,ArrayList> getPayTable(){
        return payTable;
    }



}
