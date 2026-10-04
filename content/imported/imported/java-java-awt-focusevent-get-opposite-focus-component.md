---
title: Java AWT FocusEvent get opposite focus component
nav: Java AWT FocusEvent get op...
description: Imported from java2s.com: Java AWT FocusEvent get opposite focus component
section: Imported
order: 20097
source: http://www.java2s.com/ref/java/java-awt-focusevent-get-opposite-focus-component.html
---
- java.awt.event
- java.awt.event ActionEvent ActionListener AdjustmentListener AWTEventListener ComponentListener ContainerListener FocusAdapter FocusEvent FocusListener HierarchyListener InputEvent Event ItemEvent ItemListener KeyAdapter KeyEvent KeyListener MouseAdapter MouseEvent MouseMotionAdapter MouseMotionListener MouseWheelListener WindowAdapter WindowEvent WindowFocusListener WindowStateListener

## Description

Java AWT FocusEvent get opposite focus component

```java title=Example.java
import java.awt.Component;
import java.awt.event.FocusAdapter;
import java.awt.event.FocusEvent;

import javax.swing.JButton;
import javax.swing.JFrame;

publicclass Main {
  publicstaticvoid main(String[] argv) throwsException {
    JButton component = newJButton("a");
    component.addFocusListener(new MyFocusListener());

    JFrame f = newJFrame();
    f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    f.add(component);/*fromwww.java2s.com*/
    f.pack();
    f.setVisible(true);

  }
}

class MyFocusListener extendsFocusAdapter {
  publicvoid focusGained(FocusEvent evt) {

    Component c = evt.getOppositeComponent();
    System.out.println(c.getName());
  }

  publicvoid focusLost(FocusEvent evt) {

    Component c = evt.getOppositeComponent();
    System.out.println(c.getName() + "Opposite Component");
  }
}
```

PreviousNext

## Related

- Java AWT ContainerListener handle container event
- Java FocusAdapter handle focus event
- Java AWT FocusEvent is temporary
- Java FocusListener get component gained focus
- Java FocusListener get component lost focus
