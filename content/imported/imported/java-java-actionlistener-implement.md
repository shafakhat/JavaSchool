---
title: Java ActionListener implement
nav: Java ActionListener implem...
description: Imported from the java2s.com archive: Java ActionListener implement
section: Imported - java2s Archive
order: 1013
source: https://web.archive.org/web/20210102122100/http://www.java2s.com/ref/java/java-actionlistener-implement.html
---
- java.awt.event
- java.awt.event ActionEvent ActionListener AdjustmentListener AWTEventListener ComponentListener ContainerListener FocusAdapter FocusEvent FocusListener HierarchyListener InputEvent Event ItemEvent ItemListener KeyAdapter KeyEvent KeyListener MouseAdapter MouseEvent MouseMotionAdapter MouseMotionListener MouseWheelListener WindowAdapter WindowEvent WindowFocusListener WindowStateListener

## Description

Java ActionListener implement

```java title=Example.java
import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;

publicclass Main extendsJFrame {
  public Main() {
    super("JButton");

    setDefaultCloseOperation(EXIT_ON_CLOSE);
    setLayout(newFlowLayout());

    JButton closeButton1 = newJButton("Close");
    closeButton1.addActionListener(new ButtonHandler());
    getContentPane().add(closeButton1);/*www.java2s.com*/
  }

  publicstaticvoid main(String[] args) {
    Main frame = new Main();
    frame.pack();
    frame.setVisible(true);
  }
}

class ButtonHandler implementsActionListener {
  // handle button event
  @Overridepublicvoid actionPerformed(ActionEvent event) {
    System.exit(0);
  }
}
```

PreviousNext

## Related

- Java ActionEvent is meta key pressed
- Java ActionEvent is shift key pressed
- Java ActionEvent create for key event
- Java ActionListener set JFrame background via action command
- Java ActionListener handle events from different components
