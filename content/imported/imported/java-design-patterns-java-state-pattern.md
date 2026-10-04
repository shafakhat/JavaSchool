---
title: Java Design Patterns Tutorial - Java Design Pattern - State Pattern
nav: Java Design Patterns Tutor...
description: In State pattern a class behavior is changed based on its state.
section: Imported - java2s Archive
order: 50130
source: https://www.java2s.com/Tutorials/Java/Java_Design_Patterns/0210__Java_State_Pattern.html
---
```java title=Example.java
« Previous
```

- Next »

In State pattern a class behavior is changed based on its state.

State pattern is a behavior pattern.

When using State pattern, we create various state objects and a context object whose behavior varies as its state object changes.

## Example

```java title=Example.java
interface State {
  publicvoid doAction(Context context);
}/*fromwww.java2s.com*/class StartState implements State {
  publicvoid doAction(Context context) {
    System.out.println("In start state");
    context.setState(this);
  }
  public String toString() {
    return"Start State";
  }
}
class StopState implements State {
  publicvoid doAction(Context context) {
    System.out.println("In stop state");
    context.setState(this);
  }
  public String toString() {
    return"Stop State";
  }
}
class PlayState implements State {
  publicvoid doAction(Context context) {
    System.out.println("In play state");
    context.setState(this);
  }
  public String toString() {
    return"Play State";
  }
}
class Context {
  private State state;
  public Context() {
    state = null;
  }
  publicvoid setState(State state) {
    this.state = state;
  }
  public State getState() {
    return state;
  }
}
publicclass Main {
  publicstaticvoid main(String[] args) {
    Context context = new Context();
    StartState startState = new StartState();
    startState.doAction(context);
    System.out.println(context.getState().toString());
    PlayState playState = new PlayState();
    playState.doAction(context);
    StopState stopState = new StopState();
    stopState.doAction(context);
    System.out.println(context.getState().toString());
  }
}
```

The code above generates the following result.

- Next »
- « Previous
