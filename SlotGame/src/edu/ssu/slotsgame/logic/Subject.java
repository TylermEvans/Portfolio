package edu.ssu.slotsgame.logic;

public interface Subject
{
    public void attach(Observer o, int gameEventType);
    public void detach(Observer o, int gameEventType);
    public void notify(GameEvent e);
}