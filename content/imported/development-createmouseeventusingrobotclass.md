---
title: Create mouse event using Robot class
nav: Create mouse event using R...
description: Imported from the java2s.com archive: Create mouse event using Robot class
section: Imported - java2s Archive
order: 1999
source: https://web.archive.org/web/20140301113644/http://www.java2s.com/Tutorial/Java/0120__Development/CreatemouseeventusingRobotclass.htm
---
```java title=Example.java
import java.awt.Robot;
import java.awt.event.InputEvent;
public class Main {
  public static void main(String[] args) throws Exception {
    Robot robot = new Robot();
    robot.mouseMove(200, 200);
    robot.mousePress(InputEvent.BUTTON1_MASK);
    robot.mouseRelease(InputEvent.BUTTON1_MASK);
    robot.mouseWheel(-100);
  }
}
```

| 6.55.1. | Moving the Cursor on the Screen |
|---|---|
| 6.55.2. | Simulate a mouse click |
| 6.55.3. | Simulate a key press |
| 6.55.4. | Create key press event using Robot class? |
| 6.55.5. | Get the colour of a screen pixel |
| 6.55.6. | Create mouse event using Robot class |
| 6.55.7. | Capturing a Screen Shot |
| 6.55.8. | Capture a screenshot |
| 6.55.9. | Capturing Screen in an image using Robot class |
