import java.io.*;
import java.util.*;

import etec2101.HashMap;


public class WordCounter
{
    protected HashMap mMap;
    protected BinaryHeap<WordPair> mHeap = new BinaryHeap<WordPair>(BinaryHeap.HeapType.MAXHEAP);
    public WordCounter(String filename,int nwords)
    {
        mMap = new HashMap<String,Integer>(5000,0.7f,5000);



        try
        {
            Scanner s = new Scanner(new File(filename));
            String buffer = "";
            int count = 1;

            while (s.hasNext())
            {

                String aWord = s.next();
                aWord = aWord.trim();
                for (int i = 0; i<=aWord.length()-1; i++)
                {
                    char c = aWord.charAt(i);
                    if (c == ',')
                    {
                        continue;
                    }
                    else if (c == ':')
                    {
                        continue;
                    }
                    else if (c == ';')
                    {
                        continue;
                    }
                    else if (c == '?')
                    {
                        continue;
                    }
                    else if (c == '!')
                    {
                        continue;
                    }
                    else if (c == '*')
                    {
                        continue;
                    }
                    else if (c == '"')
                    {
                        continue;
                    }
                    else if (c == '.')
                    {
                        continue;
                    }
                    else if (c == '1')
                    {
                        continue;
                    }
                    else if (c == '2')
                    {
                        continue;
                    }
                    else if (c == '3')
                    {
                        continue;
                    }
                    else if (c == '4')
                    {
                        continue;
                    }
                    else if (c == '5')
                    {
                        continue;
                    }
                    else if (c == '6')
                    {
                        continue;
                    }
                    else if (c == '7')
                    {
                        continue;
                    }
                    else if (c == '8')
                    {
                        continue;
                    }
                    else if (c == '9')
                    {
                        continue;
                    }
                    else if (c == '0')
                    {
                        continue;
                    }
                    else
                    {
                        buffer = buffer+c;
                    }
                }
                if(mMap.get(buffer)==null)
                {
                    mMap.set(buffer,count);

                }
                else
                {
                    int newcount = (int)mMap.get(buffer)+1;
                    mMap.set(buffer,newcount);

                }
                buffer = "";

            }

        }
        catch(FileNotFoundException e)
        {
            System.out.println("File Not Found");


        }
        HashMap.HashMapIterator I = mMap.iterator(HashMap.IteratorType.KEY);
        Long time = System.currentTimeMillis();
        while (I.hasNext())
        {
           String cur = (String) I.next();
           int val = (int) mMap.get(cur);
           WordPair p = new WordPair(cur, val);
           mHeap.push(p);

        }

        for (int i = 0; i<nwords; i++)
        {
            WordPair p = mHeap.pop();
            System.out.println(p.getKey() + " : " + p.getVal());

        }
        Long newtime = System.currentTimeMillis();
        float elapsed = newtime-time;
        System.out.println("HeapTime : " + elapsed/1000 +" \n");










    }




}