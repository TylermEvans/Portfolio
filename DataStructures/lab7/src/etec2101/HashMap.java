package etec2101;

import java.util.Iterator;
import java.util.NoSuchElementException;
import java.util.Vector;


/**
 * Out simple associate array.  The HashMap is a collection of key- (of type K)
 * value (or type V) pairs.  This implementation uses linear probing (open addressing)
 * to find a given key-value pair.
 * @author Jason Witherell, Fall 2015
 * @param <K>: The key of all key-value pairs in this HashMap
 * @param <V> : The value of all key-value pairs in this HashMap.
 */
public class HashMap<K, V>
{
    /**
     * The key-value pairs are stored here.  null's indicate there is nothing
     * in that "slot"
     */
    protected Node[] mTable;

    /**
     * This is the number of key-value pairs in the HashMap.
     */
    protected int mSize;

    /**
     * The load factor, which should be in the range 0.0 to 1.0 (not including
     * the end-points).  If the ratio of used-slots to capacity ever meets or
     * exceeds this, we re-allocate the hash-table (because after this, we
     * would expect there to be more collisions).  0.75 is a reasonable value
     * for this parameter.
     */
    protected float mMaxLoadFactor;

    /**
     * Whenever the load factor is exceeded, we'll increase the table by this
     * amount.
     */
    protected int mSizeIncrement;

    /**
     * The iterator method takes an argument of this type.  If KEY is passed,
     * the iterator will return objects of type K, otherwise it'll return values
     * of type V.
     */
    public enum IteratorType { KEY, VALUE };


    /**
     * A simple key-value pair
     * @param <K>: The key
     * @param <V>: The value.
     */
    private class Node<K, V>
    {
        V mValue;
        K mKey;

        private Node(K key, V val)
        {
            mKey = key;
            mValue = val;
        }
    }


    /**
     * Default constructor.
     * @param initial_size: The initial capacity of the hash-map's internal table.
     *                        This should be larger than the expected number of
     *                        elements you'll store in the array.
     * @param max_load_percent: A percentage of used spots to available spots.  If
     *                          the percentage is ever over max_load_percent, we will
     *                          increase the size of the table by size_inc (and re-hash
     *                          all elements).
     * @param size_inc : The size to increase the table by when our load factor
     *                   exceeds the max_load_percent.
     */
    public HashMap(int initial_size, float max_load_percent, int size_inc)
    {
        mTable = new Node[initial_size];
        mSize = 0;
        mMaxLoadFactor = max_load_percent;
        mSizeIncrement = size_inc;
    }


    /**
     * Either adds a new key-value pair (if this key isn't in the table) or
     *   replaces the value previously associated with this key.
     * @param key
     * @param value
     */
    public void set(K key, V value)
    {
        int index = probe(key, true);
        if (mTable[index] == null)
        {
            // We're adding a new key-value pair.
            mTable[index] = new Node(key, value);
            mSize++;
        }
        else
        {
            // We're modifying an existing key-value pair.
            mTable[index] = new Node(key, value);
        }

        // See if we need to expand the array
        if ((float)mSize / mTable.length >= mMaxLoadFactor)
            expand();
    }


    /**
     * Fetches the value associate with the given key.
     * @param key: The key to search for.
     * @return : The value associated with key (if there is such a pair).  If there
     *           is no such pair, returns null.
     */
    public V get(K key)
    {
        Node n = mTable[probe(key, true)];
        if (n == null)
            return null;
        else
            return (V)n.mValue;
    }


    /**
     * Removes a key-value pair from the hash map.  This function does nothing
     *  if there is no such key-value pair.
     * @param key : The key of the key-value pair to remove.
     */
    public void remove(K key)
    {
        int index = probe(key, true);
        Node n = mTable[index];
        if (n != null && n.mKey.equals(key))
        {
            mTable[index] = null;
            mSize--;
            // Thanks to Mike Wollard for finding this error and Matt Crabtree for
            // suggesting a very creating solution.
            // The problem: if have 3 values: a, b, and c that map to index i.
            //    If we remove b, we'll set that slot to null.  But...when we later
            //    attempt to find element c, we'll incorrectly report that is non-
            //    existent since there is a null at position i+1.
            // Matt's solution: re-hash all elements after position index.
            //    This should still be a relatively small number of nodes, so
            //    I *think* it would still be considered O(1)
            Vector<Node> to_be_rehashed = new Vector();
            boolean done = false;
            for (int i = index + 1; i < mTable.length; i++ )
            {
                Node temp = mTable[i];
                if (temp == null)
                {
                    done = true;
                    break;
                }
                to_be_rehashed.add(temp);
                mTable[i] = null;
            }
            for (int i = 0; !done && i < index; i++)
            {
                Node temp = mTable[i];
                if (temp == null)
                {
                    done = true;
                    break;
                }
                to_be_rehashed.add(temp);
                mTable[i] = null;
            }
            // Now, re-add all the elements in to_be_rehashed
            for (Node temp : to_be_rehashed)
                set((K)temp.mKey, (V)temp.mValue);

        }
    }


    /**
     * @return : The number of key-value pairs in the hash-map.
     */
    public int getSize()
    {
        return mSize;
    }


    /**
     * This method is used internally to handle collisions.  When a key is
     * run through the hash function, it might find the value in question (and we're
     * done), or it could find a null (they the value isn't in the map), or
     * it could find another key.  In this latter case, we have to search for one
     * of the other two cases.  If our hash function didn't cluster the codes,
     * we shouldn't have to search many value here.
     * @param key : The value to find (or null)
     * @param stop_on_null : is probably always set to true -- indicates if
     *                       we stop when we find a null)
     * @return : the position of the value we were searching for (or null
     *             if stop_on_null is true).
     * @throws NoSuchElementException if the given key value is not in the table
     */
    private int probe(K key, boolean stop_on_null) throws NoSuchElementException
    {
        // Hash to our initial position
        int capacity = mTable.length;
        int hash = Math.abs(key.hashCode());
        int index = hash % capacity;
        Node n = mTable[index];
        if ((n != null && n.mKey.equals(key)) || (stop_on_null && n == null))
            return index;

        // If we didn't immediately find it, loop up to the end of the list
        for (int i = index + 1; i < mTable.length; i++)
        {
            n = mTable[i];
            if ((n != null && n.mKey.equals(key)) || (stop_on_null && n == null))
                return i;
        }

        // If we *still* didn't find it, loop from the beginning up to our
        // initial hash position.
        for (int i = 0; i < index; i++)
        {
            n = mTable[i];
            if ((n != null && n.mKey.equals(key)) || (stop_on_null && n == null))
                return i;
        }

        // We didn't find the value!
        throw new NoSuchElementException("Can't find element with key '" + key.toString() + "'!");
    }

    /**
     * Resizes the array (using the size_inc value passed to the constructor)
     * Note: This is a doubly-expensive operation (and so we should set our
     * capacity higher) because all values in the old table must be rehashed
     * (since our table size is different now).
     */
    private void expand()
    {
        //System.out.println("EXPANDING HashMap");
        Node[] old_table = mTable;
        mTable = new Node[mTable.length + mSizeIncrement];
        mSize = 0;
        for (int i = 0; i < old_table.length; i++)
        {
            Node n = old_table[i];
            if (n != null)
                set((K)n.mKey, (V)n.mValue);
        }
    }


    /**
     * Return an iterator which will walk through all values in the HashMap.
     * Note: a HashMap has no inherent ordering, so these values in general
     * will *not* be in the same order they were added.
     * @param t : Indicates whether we want to traverse by key or by value.
     *            Note: the iterator returns an Object, so it is up to the
     *            caller to properly cast this value.
     * @return : A HashMapIterator<K, V>
     */
    public HashMapIterator iterator(IteratorType t)
    {
        return new HashMapIterator/*<K, V>*/(this, t);
    }

    /**
     * @return : The string-representation of the key-value pairs in this
     *           HashMap.
     */
    @Override
    public String toString()
    {
        String s = "{";
        HashMapIterator/*<K, V>*/ I = iterator(IteratorType.KEY);
        while (I.hasNext())
        {
            K key = (K)I.next();
            s += key.toString() + ":" + get(key).toString();
            if (I.hasNext())
                s += ", ";
        }
        return s + "}";
    }


    /**
     * Removes all elements from this HashMap
     */
    public void clear()
    {
        for (int i = 0; i < mTable.length; i++)
            mTable[i] = null;
        mSize = 0;
    }

    /**
     * This HashMapIterator is capable of walking through the keys (of type K)
     * or the values (of type V) in the associated HashMap.
     */
    public class HashMapIterator implements Iterator
    {
        /**
         * The current position in the hash table (which is non-null)
         */
        protected int mPos;

        /**
         * The position we initially started iterating (probably 0)
         */
        protected int mInitialPos;

        /**
         * The containing HashMap
         */
        protected HashMap mOwner;

        /**
         * The type of iteration we're doing (key or value)
         */
        protected IteratorType mType;

        /**
         * Constructor
         * @param owner : The hash map through who's values we want to iterator
         * @param t : The type of traversal we want to do (KEY or VALUE)
         */
        public HashMapIterator(HashMap owner, IteratorType t)
        {
            mOwner = owner;
            mInitialPos = mPos;
            mPos = findNextNonNull();
            mType = t;
        }

        /**
         * Helper function to find the next non-null entry in the hash table.
         * @return : The position in the hash table of the next non-null (or
         *     table size if there are no more non-null entries).
         */
        protected int findNextNonNull()
        {
            int i = mPos + 1;
            while (i < mOwner.mTable.length)
            {
                if (mOwner.mTable[i] != null)
                    return i;
                i++;
            }
            i = 0;
            while (i < mInitialPos)
            {
                if (mOwner.mTable[i] != null)
                    return i;
                i++;
            }
            // If we get here, there are no more values.  Indicate this by returning
            // the size of the array (which would be an invalid position)
            return mOwner.mTable.length;
        }


        /**
         *
         * @return true if we have more non-null values in the hash-map.
         */
        public boolean hasNext()
        {
            return mPos < mOwner.mTable.length;
        }

        /**
         * @return The current value in our iteration.  It is of type
         *     K if the user indicated they wanted a key-traversal, or of type
         *     V if the user indicated they wanted a value-traversal.
         * @throws NoSuchElementException : if next was called without first
         *     checking for next value with hasNext.
         */
        public Object next() throws NoSuchElementException
        {
            if (mPos < mOwner.mTable.length && mOwner.mTable[mPos] != null)
            {
                Node n = (Node)mOwner.mTable[mPos];
                mPos = findNextNonNull();
                if (mType == IteratorType.KEY)
                    return n.mKey;
                else
                    return n.mValue;
            }
            else
                throw new NoSuchElementException("No more values to return!");
        }
    }
}
