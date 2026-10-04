---
title: Java ActionEvent compare event source to component instance
nav: Java ActionEvent compare e...
description: button1.setText("I've been clicked" + clickCount + " times!");
section: Imported - java2s Archive
order: 1031
source: https://web.archive.org/web/20210102122059/http://www.java2s.com/ref/java/java-actionevent-compare-event-source-to-component-instance.html
---
- java.awt.event
- java.awt.event ActionEvent ActionListener AdjustmentListener AWTEventListener ComponentListener ContainerListener FocusAdapter FocusEvent FocusListener HierarchyListener InputEvent Event ItemEvent ItemListener KeyAdapter KeyEvent KeyListener MouseAdapter MouseEvent MouseMotionAdapter MouseMotionListener MouseWheelListener WindowAdapter WindowEvent WindowFocusListener WindowStateListener

## Description

```java title=Example.java
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
publicclass Main extendsJFrameimplementsActionListener {
   privateJButton button1 = newJButton("Click Me!");
   privateint clickCount = 0;
   public Main() {
      this.setSize(200, 100);
      this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      this.setTitle("I'm Listening");
      JPanel panel1 = newJPanel();
      button1.addActionListener(this);
      panel1.add(button1);this.add(panel1);
      this.setVisible(true);
   }
   publicvoid actionPerformed(ActionEvent e) {
      if (e.getSource() == button1) {
         clickCount++;
         if (clickCount == 1)
            button1.setText("I've been clicked!");
         else
            button1.setText("I've been clicked" + clickCount + " times!");
      }
   }
   publicstaticvoid main(String[] args) {
      new Main();
   }
}
```

PreviousNext

## Related

- Java ActionEvent get action command text
- Java ActionEvent get event source
- Java ActionEvent cast event source to JButton
- Java ActionEvent get action command
- Java ActionEvent get action id
