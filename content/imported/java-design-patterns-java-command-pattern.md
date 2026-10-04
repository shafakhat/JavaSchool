---
title: Java Design Patterns Tutorial - Java Design Pattern - Command Pattern
nav: Java Design Patterns Tutor...
description: Command pattern is a data driven design pattern It is one of the behavioral pattern.
section: Imported - java2s Archive
order: 50125
source: https://www.java2s.com/Tutorials/Java/Java_Design_Patterns/0150__Java_Command_Pattern.html
---
Command pattern is a data driven design pattern It is one of the behavioral pattern.

A request is wrapped under a object as command and passed to invoker object.

Invoker object passes the command to the corresponding object and that object executes the command.

## Example

```java title=Example.java
import java.util.ArrayList;
import java.util.List;
interface Command {
  void execute();
}
class MouseCursor {
  privateint x = 10;
  privateint y = 10;
  publicvoid move() {
    System.out.println("Old Position:"+x +":"+y);
    x++;
    y++;
    System.out.println("New Position:"+x +":"+y);
  }
  publicvoid reset() {
    System.out.println("reset");
    x = 10;
    y = 10;
  }
}
class MoveCursor implements Command {
  private MouseCursor abcStock;
  public MoveCursor(MouseCursor abcStock) {
    this.abcStock = abcStock;
  }
  publicvoid execute() {
    abcStock.move();
  }
}
class ResetCursor implements Command {
  private MouseCursor abcStock;
  public ResetCursor(MouseCursor abcStock) {
    this.abcStock = abcStock;
  }
  publicvoid execute() {
    abcStock.reset();
  }
}
class MouseCommands {
  private List<Command> orderList = new ArrayList<Command>();
  publicvoid takeOrder(Command order) {
    orderList.add(order);
  }
  publicvoid placeOrders() {
    for (Command order : orderList) {
      order.execute();
    }
    orderList.clear();
  }
}
publicclass Main {
  publicstaticvoid main(String[] args) {
    MouseCursor cursor = new MouseCursor();
    MoveCursor moveCursor = new MoveCursor(cursor);
    ResetCursor resetCursor = new ResetCursor(cursor);
    MouseCommands commands= new MouseCommands();
    commands.takeOrder(moveCursor);
    commands.takeOrder(resetCursor);
    commands.placeOrders();
  }
}
```

The code above generates the following result.

- « Previous
