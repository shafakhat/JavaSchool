---
title: Java AWT ComponentListener handle component event
nav: Java AWT ComponentListener...
description: }/*fromwww.java2s.com*/publicvoid componentMoved(ComponentEvent e) {
section: Imported
order: 20071
source: http://www.java2s.com/ref/java/java-awt-componentlistener-handle-component-event.html
---
- java.awt.event
- java.awt.event ActionEvent ActionListener AdjustmentListener AWTEventListener ComponentListener ContainerListener FocusAdapter FocusEvent FocusListener HierarchyListener InputEvent Event ItemEvent ItemListener KeyAdapter KeyEvent KeyListener MouseAdapter MouseEvent MouseMotionAdapter MouseMotionListener MouseWheelListener WindowAdapter WindowEvent WindowFocusListener WindowStateListener

## Description

Java AWT ComponentListener handle component event

```java title=Example.java
import java.awt.Dimension;
import java.awt.event.ComponentEvent;
import java.awt.event.ComponentListener;

import javax.swing.JFrame;

class My implementsComponentListener {
   publicvoid componentHidden(ComponentEvent e) {
      System.out.println("componentHidden");
   }/*fromwww.java2s.com*/publicvoid componentMoved(ComponentEvent e) {
      System.out.println("componentMoved");
   }

   publicvoid componentResized(ComponentEvent e) {
      System.out.println("componentResized");

   }

   publicvoid componentShown(ComponentEvent e) {
      System.out.println("component shown");
   }
}

publicclass Main extendsJFrame {
   public Main() {
      addComponentListener(new My());
   }

   publicstaticvoid main(String[] arg) {
      Main m = new Main();

      m.setVisible(true);
      m.setSize(newDimension(300, 100));
      m.setLocation(50, 50);
   }
}
```

PreviousNext

## Related

- Java ActionListener handle enter key pressed event for JTextField
- Java AWT AdjustmentListener handle adjustment event
- Java AWTEventListener create custom event listener
- Java AWT ContainerListener handle container event
- Java FocusAdapter handle focus event
