---
title: Moving the Cursor on the Screen
nav: Moving the Cursor on the S...
description: Imported from java2s.com: Moving the Cursor on the Screen
section: Imported
order: 20064
source: http://java2s.com/Tutorial/Java/0120__Development/MovingtheCursorontheScreen.htm
---
```java title=Example.java
import java.awt.Robot;
public class Main {
  public static void main(String[] argv) throws Exception {
    Robot robot = new Robot();
    robot.mouseMove(500, 500);
  }
}
```
