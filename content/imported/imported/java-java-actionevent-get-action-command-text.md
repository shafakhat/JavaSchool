---
title: Java ActionEvent get action command text
nav: Java ActionEvent get actio...
description: Imported from the java2s.com archive: Java ActionEvent get action command text
section: Imported - java2s Archive
order: 1000
source: https://web.archive.org/web/20210102122058/http://www.java2s.com/ref/java/java-actionevent-get-action-command-text.html
---
- java.awt.event
- java.awt.event ActionEvent ActionListener AdjustmentListener AWTEventListener ComponentListener ContainerListener FocusAdapter FocusEvent FocusListener HierarchyListener InputEvent Event ItemEvent ItemListener KeyAdapter KeyEvent KeyListener MouseAdapter MouseEvent MouseMotionAdapter MouseMotionListener MouseWheelListener WindowAdapter WindowEvent WindowFocusListener WindowStateListener

## Description

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
    closeButton1.setActionCommand("CloseDemo2s");
    closeButton1.addActionListener(new ButtonHandler());
    getContentPane().add(closeButton1);/*fromwww.java2s.com*/
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
    System.out.println(event.getActionCommand());
    System.exit(0);
  }
}
```

PreviousNext

## Related

- Java AWT Toolkit add event listener by mask
- Java AWT Clipboard get/set text data
- Java ActionEvent check event source
- Java ActionEvent get event source
- Java ActionEvent cast event source to JButton
