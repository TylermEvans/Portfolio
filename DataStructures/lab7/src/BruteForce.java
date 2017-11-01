import etec2101.HashMap;

import java.util.ArrayList;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.LinkedList;
import java.util.Scanner;

public class BruteForce {
    protected HashMap mMap;

    public BruteForce(String filename,int nwords) {
        mMap = new HashMap<String, Integer>(5000, 0.7f, 5000);
        LinkedList<String> List = new LinkedList<>();


        try {
            Scanner s = new Scanner(new File(filename));
            String buffer = "";
            int count = 1;

            while (s.hasNext()) {

                String aWord = s.next();
                aWord = aWord.trim();
                for (int i = 0; i <= aWord.length() - 1; i++) {
                    char c = aWord.charAt(i);
                    if (c == ',') {
                        continue;
                    } else if (c == ':') {
                        continue;
                    } else if (c == ';') {
                        continue;
                    } else if (c == '?') {
                        continue;
                    } else if (c == '!') {
                        continue;
                    } else if (c == '*') {
                        continue;
                    } else if (c == '"') {
                        continue;
                    } else if (c == '.') {
                        continue;
                    } else if (c == '1') {
                        continue;
                    } else if (c == '2') {
                        continue;
                    } else if (c == '3') {
                        continue;
                    } else if (c == '4') {
                        continue;
                    } else if (c == '5') {
                        continue;
                    } else if (c == '6') {
                        continue;
                    } else if (c == '7') {
                        continue;
                    } else if (c == '8') {
                        continue;
                    } else if (c == '9') {
                        continue;
                    } else if (c == '0') {
                        continue;
                    } else {
                        buffer = buffer + c;
                    }
                }
                if (mMap.get(buffer) == null) {
                    mMap.set(buffer, count);

                } else {
                    int newcount = (int) mMap.get(buffer) + 1;
                    mMap.set(buffer, newcount);

                }
                buffer = "";

            }

        } catch (FileNotFoundException e) {
            System.out.println("File Not Found");


        }
        Long time = System.currentTimeMillis();
        ArrayList wordlist = new ArrayList();
        HashMap.HashMapIterator I = mMap.iterator(HashMap.IteratorType.KEY);
        while (I.hasNext())
        {
            String cur = (String)I.next();
            int val = (int)mMap.get(cur);
            WordPair p = new WordPair(cur,val);
            wordlist.add(p);
        }


        int highestval = 0;
        ArrayList nwordlist = new ArrayList();
        WordPair highestword = new WordPair(null, 0);
        for (int n = 0; n<nwords; n++)
        {

            highestval = 0;
            for (int i = 0; i < wordlist.size() - 1; i++)
            {
                WordPair nword = (WordPair) wordlist.get(i);
                if (nwordlist.contains(nword)!=true && highestval < nword.getVal())
                {
                    highestval = nword.getVal();
                    highestword = nword;
                }



            }
            nwordlist.add(highestword);
        }
        for (int i = 0; i<nwordlist.size(); i++)
        {
            System.out.println(((WordPair)nwordlist.get(i)).getKey()+ " : "+((WordPair)nwordlist.get(i)).getVal());


        }
        Long newtime = System.currentTimeMillis();
        float elapsed = newtime-time;
        System.out.println("BruteForceTime : "+ elapsed/1000 + " \n ");

















    }
}