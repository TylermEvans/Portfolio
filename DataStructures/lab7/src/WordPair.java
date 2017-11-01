public class WordPair implements Comparable<WordPair>
{
    protected String mKey;
    protected Integer mValue;
    public WordPair(String key, Integer val)
    {
        mKey = key;
        mValue = val;
    }
    public Integer getVal()
    {

        return mValue;
    }
    public String getKey()
   {

        return mKey;
   }

    @Override
    public int compareTo(WordPair o)
    {
       return (Integer)mValue.compareTo(o.mValue);

    }
}

