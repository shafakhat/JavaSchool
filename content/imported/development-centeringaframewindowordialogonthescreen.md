---
title: Centering a Frame, Window, or Dialog on the Screen
nav: Centering a Frame, Window,...
description: Imported from the java2s.com archive: Centering a Frame, Window, or Dialog on the Screen
section: Imported - java2s Archive
order: 1798
source: https://web.archive.org/web/20140829082609/http://www.java2s.com/Tutorial/Java/0120__Development/CenteringaFrameWindoworDialogontheScreen.htm
---
```java title=Example.java
import java.awt.Dimension;
import java.awt.Toolkit;
import javax.swing.JFrame;
public class Main {
  public static void main(String[] argv) throws Exception {
    Dimension dim = Toolkit.getDefaultToolkit().getScreenSize();
    JFrame window = new JFrame();
    window.setSize(300,300);
    int w = window.getSize().width;
    int h = window.getSize().height;
    int x = (dim.width - w) / 2;
    int y = (dim.height - h) / 2;
    window.setLocation(x, y);
    window.setVisible(true);
  }
}
```

| 6.25.1. | java.awt.Toolkit |
|---|---|
| 6.25.2. | Getting the Screen Size |
| 6.25.3. | Centering a Frame, Window, or Dialog on the Screen |
