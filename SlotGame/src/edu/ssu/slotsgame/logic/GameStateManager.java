package edu.ssu.slotsgame.logic;


public class GameStateManager
{

    private final static GameStateManager instance_ = new GameStateManager();
    private int currentState_ = GameState.READY;
    private int prevState;


    public int getCurrentState_(){
        return currentState_;
    }
    public void setCurrentState_(int state){
        this.prevState = this.currentState_;
        this.currentState_ = state;
        EventManager.getInstance().notify(new StateEvent(GameEvent.CHANGE_STATE,this.currentState_,this.prevState));

    }

    public static GameStateManager getInstance_() {
        return instance_;
    }
}
