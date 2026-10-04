---
title: Java ActionListener handle enter key pressed event for JTextField
nav: Java ActionListener handle...
description: Java ActionListener handle enter key pressed event for JTextField
section: Imported - java2s Archive
order: 1012
source: https://web.archive.org/web/20210102122102/http://www.java2s.com/ref/java/java-actionlistener-handle-enter-key-pressed-event-for-jtextfield.html
---
- java.awt.event
- java.awt.event ActionEvent ActionListener AdjustmentListener AWTEventListener ComponentListener ContainerListener FocusAdapter FocusEvent FocusListener HierarchyListener InputEvent Event ItemEvent ItemListener KeyAdapter KeyEvent KeyListener MouseAdapter MouseEvent MouseMotionAdapter MouseMotionListener MouseWheelListener WindowAdapter WindowEvent WindowFocusListener WindowStateListener

## Description

Java ActionListener handle enter key pressed event for JTextField

```java title=Example.java
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JFrame;
import javax.swing.JTextField;

publicclass Main extendsJFrame {
  JTextField text = newJTextField("Press Return", 40);

  public Main() {
    setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    text.addActionListener(newActionListener() {
      publicvoid actionPerformed(ActionEvent e) {
        System.out.println("Text=" + text.getText());
      }/*fromwww.java2s.com*/
    });

    getContentPane().add(text, "North");
    pack();
  }

  publicstaticvoid main(String[] args) {
    new Main().setVisible(true);
  }
}
```

PreviousNext

## Related

- Java ActionListener add more than one action listener to JButton
- Java ActionListener remove action listener from component
- Java ActionListener handle action event on JComboBox
- Java AWT AdjustmentListener handle adjustment event
- Java AWTEventListener create custom event listener
