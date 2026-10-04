---
title: Simulate a key press
nav: Simulate a key press
description: Imported from the java2s.com archive: Simulate a key press
section: Imported - java2s Archive
order: 1997
source: https://web.archive.org/web/20140301122156/http://www.java2s.com/Tutorial/Java/0120__Development/Simulateakeypress.htm
---
```java title=Example.java
import java.awt.Robot;
import java.awt.event.KeyEvent;
public class Main {
  public static void main(String[] argv) throws Exception {
    Robot robot = new Robot();
    robot.keyPress(KeyEvent.VK_A);
    robot.keyRelease(KeyEvent.VK_A);
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
