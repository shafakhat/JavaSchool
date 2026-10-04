---
title: Java AWT ContainerListener handle container event
nav: Java AWT ContainerListener...
description: }/*fromwww.java2s.com*/publicvoid componentRemoved(ContainerEvent e) {
section: Imported
order: 20079
source: http://www.java2s.com/ref/java/java-awt-containerlistener-handle-container-event.html
---
- java.awt.event
- java.awt.event ActionEvent ActionListener AdjustmentListener AWTEventListener ComponentListener ContainerListener FocusAdapter FocusEvent FocusListener HierarchyListener InputEvent Event ItemEvent ItemListener KeyAdapter KeyEvent KeyListener MouseAdapter MouseEvent MouseMotionAdapter MouseMotionListener MouseWheelListener WindowAdapter WindowEvent WindowFocusListener WindowStateListener

## Description

Java AWT ContainerListener handle container event

```java title=Example.java
import java.awt.event.ContainerEvent;
import java.awt.event.ContainerListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;

publicclass Main {

  publicstaticvoid main(String[] a) {
    JFrame frame = newJFrame();
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

    JPanel buttonPanel = newJPanel();
    buttonPanel.addContainerListener(newContainerListener() {

      publicvoid componentAdded(ContainerEvent e) {
        displayMessage(" added to ", e);
      }/*fromwww.java2s.com*/publicvoid componentRemoved(ContainerEvent e) {
        displayMessage(" removed from ", e);
      }

      void displayMessage(String action, ContainerEvent e) {
        System.out.println(((JButton) e.getChild()).getText() + " was" + action
            + e.getContainer().getClass().getName());
      }
    });
    buttonPanel.add(newJButton("A"));

    frame.add(buttonPanel);

    frame.setSize(300, 200);
    frame.setVisible(true);
  }

}
```

PreviousNext

## Related

- Java AWT AdjustmentListener handle adjustment event
- Java AWTEventListener create custom event listener
- Java AWT ComponentListener handle component event
- Java FocusAdapter handle focus event
- Java AWT FocusEvent is temporary
