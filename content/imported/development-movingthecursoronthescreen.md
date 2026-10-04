---
title: Moving the Cursor on the Screen
nav: Moving the Cursor on the S...
description: Imported from the java2s.com archive: Moving the Cursor on the Screen
section: Imported - java2s Archive
order: 1995
source: https://web.archive.org/web/20140829084003/http://www.java2s.com/Tutorial/Java/0120__Development/MovingtheCursorontheScreen.htm
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
