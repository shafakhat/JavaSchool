---
title: Capturing Screen in an image using Robot class
nav: Capturing Screen in an ima...
description: Dimension screenDim = Toolkit.getDefaultToolkit().getScreenSize();
section: Imported - java2s Archive
order: 2002
source: https://web.archive.org/web/20140301122327/http://www.java2s.com/Tutorial/Java/0120__Development/CapturingScreeninanimageusingRobotclass.htm
---
```java title=Example.java
import java.awt.BorderLayout;
import java.awt.Dimension;
import java.awt.Rectangle;
import java.awt.Robot;
import java.awt.Toolkit;
import java.awt.image.BufferedImage;
import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JWindow;
public class Main {
  public static void main(String[] arg) throws Exception {
    Dimension screenDim = Toolkit.getDefaultToolkit().getScreenSize();
    Robot robot = new Robot();
    BufferedImage image = robot.createScreenCapture(new Rectangle(0, 0, (int) screenDim.getWidth(),
        (int) screenDim.getHeight()));
    JWindow window = new JWindow(new JFrame());
    window.getContentPane().setLayout(new BorderLayout());
    window.getContentPane().add(BorderLayout.CENTER, new JLabel(new ImageIcon(image)));
    window.pack();
    window.setVisible(true);
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
