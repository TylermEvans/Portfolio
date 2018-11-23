package edu.ssu.slotsgame.logic;

import edu.ssu.slotsgame.logic.Subject;

import java.util.HashMap;
import java.util.ArrayList;

public class EventManager implements Subject
{
    private final static EventManager instance_ = new EventManager();

    private HashMap<Integer, ArrayList<Observer>> observerMap_;

    public static EventManager getInstance()
    {
        return instance_;
    }

    private EventManager()
    {
        observerMap_ = new HashMap<Integer, ArrayList<Observer>>();
    }

    public void attach(Observer o, int gameEventType)
    {
        Integer type = new Integer(gameEventType);
        if (!observerMap_.containsKey(type))
        {
            observerMap_.put(type, new ArrayList<Observer>());
        }

        observerMap_.get(type).add(o);
    }

    public void detach(Observer o, int gameEventType)
    {
        Integer type = new Integer(gameEventType);
        if (observerMap_.containsKey(type))
        {
            observerMap_.get(type).remove(o);
        }
    }

    public void notify(GameEvent e)
    {
        Integer type = new Integer(e.getType());
        if (observerMap_.containsKey(type))
        {
            ArrayList<Observer> observerList = observerMap_.get(type);
            for (int i = 0; i < observerList.size(); ++i)
            {
                observerList.get(i).notify(e);
            }
        }
    }
}