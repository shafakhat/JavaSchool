---
title: Capturing a Screen Shot
nav: Capturing a Screen Shot
description: BufferedImage bufferedImage = robot.createScreenCapture(area);
section: Imported - java2s Archive
order: 2004
source: https://web.archive.org/web/20140301114418/http://www.java2s.com/Tutorial/Java/0120__Development/CapturingaScreenShot.htm
---
```java title=Example.java
import java.awt.Rectangle;
import java.awt.Robot;
import java.awt.Toolkit;
import java.awt.image.BufferedImage;
public class Main {
  public static void main(String[] argv) throws Exception {
    Robot robot = new Robot();
    int x = 100;
    int y = 100;
    int width = 200;
    int height = 200;
    Rectangle area = new Rectangle(x, y, width, height);
    BufferedImage bufferedImage = robot.createScreenCapture(area);
    area = new Rectangle(Toolkit.getDefaultToolkit().getScreenSize());
    bufferedImage = robot.createScreenCapture(area);
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
