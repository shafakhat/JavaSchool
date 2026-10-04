---
title: Create key press event using Robot class?
nav: Create key press event usi...
description: Imported from the java2s.com archive: Create key press event using Robot class?
section: Imported - java2s Archive
order: 1998
source: https://web.archive.org/web/20140301110517/http://www.java2s.com/Tutorial/Java/0120__Development/CreatekeypresseventusingRobotclass.htm
---
```java title=Example.java
import java.awt.Robot;
import java.awt.event.KeyEvent;
public class Main {
  public static void main(String[] args) throws Exception {
    Robot robot = new Robot();
    robot.delay(3000);
    robot.keyPress(KeyEvent.VK_Q);
    robot.keyPress(KeyEvent.VK_W);
    robot.keyPress(KeyEvent.VK_E);
    robot.keyPress(KeyEvent.VK_R);
    robot.keyPress(KeyEvent.VK_T);
    robot.keyPress(KeyEvent.VK_Y);
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
