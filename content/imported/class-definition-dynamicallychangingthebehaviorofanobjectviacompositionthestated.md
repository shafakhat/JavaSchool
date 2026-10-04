---
title: Dynamically changing the behavior of an object via composition (the 'State' design pattern)
nav: Dynamically changing the b...
description: Imported from the java2s.com archive: Dynamically changing the behavior of an object via composition (the 'State' design pattern)
section: Imported - java2s Archive
order: 1201
source: https://web.archive.org/web/20140829081411/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/DynamicallychangingthebehaviorofanobjectviacompositiontheStatedesignpattern.htm
---
```java title=Example.java
abstract class Actor {
  public abstract void act();
}
class HappyActor extends Actor {
  public void act() {
    System.out.println("HappyActor");
  }
}
class SadActor extends Actor {
  public void act() {
    System.out.println("SadActor");
  }
}
class Stage {
  private Actor actor = new HappyActor();
  public void change() {
    actor = new SadActor();
  }
  public void performPlay() {
    actor.act();
  }
}
public class MainClass {
  public static void main(String[] args) {
    Stage stage = new Stage();
    stage.performPlay();
    stage.change();
    stage.performPlay();
  }
}
java title=Example.java
HappyActor
SadActor
```
