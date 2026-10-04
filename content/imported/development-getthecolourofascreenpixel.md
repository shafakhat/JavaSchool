---
title: Get the colour of a screen pixel
nav: Get the colour of a screen...
description: Imported from the java2s.com archive: Get the colour of a screen pixel
section: Imported - java2s Archive
order: 2000
source: https://web.archive.org/web/20140301102446/http://www.java2s.com/Tutorial/Java/0120__Development/Getthecolourofascreenpixel.htm
---
```java title=Example.java
import java.awt.Color;
import java.awt.Robot;
public class Main {
  public static void main(String[] args) throws Exception{
    Robot robot = new Robot();
    Color color = robot.getPixelColor(20, 20);
    System.out.println("Red   = " + color.getRed());
    System.out.println("Green = " + color.getGreen());
    System.out.println("Blue  = " + color.getBlue());
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
