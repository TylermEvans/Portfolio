package lab05_TE;


import etec2101.HashMap;

import java.util.Objects;

public class Main {
    public static void main(String[] args)
    {
        HashMap<String,Integer> mMap = new HashMap<String,Integer>(5,0.7f,10);
        mMap.set("bob",10);
        mMap.set("sarah",20);
        System.out.println(mMap);





    }
}
