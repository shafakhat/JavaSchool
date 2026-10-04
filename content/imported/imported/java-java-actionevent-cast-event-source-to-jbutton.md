---
title: Java ActionEvent cast event source to JButton
nav: Java ActionEvent cast even...
description: JOptionPane.showMessageDialog(null, "You clicked" + buttonText);
section: Imported - java2s Archive
order: 1029
source: https://web.archive.org/web/20210102122059/http://www.java2s.com/ref/java/java-actionevent-cast-event-source-to-jbutton.html
---
- java.awt.event
- java.awt.event ActionEvent ActionListener AdjustmentListener AWTEventListener ComponentListener ContainerListener FocusAdapter FocusEvent FocusListener HierarchyListener InputEvent Event ItemEvent ItemListener KeyAdapter KeyEvent KeyListener MouseAdapter MouseEvent MouseMotionAdapter MouseMotionListener MouseWheelListener WindowAdapter WindowEvent WindowFocusListener WindowStateListener

## Description

Java ActionEvent cast event source to JButton

```java title=Example.java
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JOptionPane;

class MyActionListener implementsActionListener {
  publicvoid actionPerformed(ActionEvent e) {
    JButton source = (JButton) e.getSource();
    String buttonText = source.getText();
    JOptionPane.showMessageDialog(null, "You clicked" + buttonText);
  }//fromwww.java2s.com
}

publicclass Main {
  publicstaticvoid main(String[] args) {
    JFrame frame = newJFrame("ActionListener");
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    JButton button = newJButton("Register");
    button.addActionListener(new MyActionListener());
    frame.getContentPane().add(button);
    frame.pack();
    frame.setVisible(true);
  }
}
```

PreviousNext

## Related

- Java ActionEvent check event source
- Java ActionEvent get action command text
- Java ActionEvent get event source
- Java ActionEvent compare event source to component instance
- Java ActionEvent get action command
