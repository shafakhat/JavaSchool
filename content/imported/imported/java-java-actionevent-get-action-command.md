---
title: Java ActionEvent get action command
nav: Java ActionEvent get actio...
description: Main() {//www.java2s.comJFrame jfrm = newJFrame("A Button Example");
section: Imported - java2s Archive
order: 1001
source: https://web.archive.org/web/20210102122059/http://www.java2s.com/ref/java/java-actionevent-get-action-command.html
---
- java.awt.event
- java.awt.event ActionEvent ActionListener AdjustmentListener AWTEventListener ComponentListener ContainerListener FocusAdapter FocusEvent FocusListener HierarchyListener InputEvent Event ItemEvent ItemListener KeyAdapter KeyEvent KeyListener MouseAdapter MouseEvent MouseMotionAdapter MouseMotionListener MouseWheelListener WindowAdapter WindowEvent WindowFocusListener WindowStateListener

## Description

Java ActionEvent get action command

```java title=Example.java
import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;

publicclass Main implementsActionListener {
   JButton jbtnA = newJButton("Alpha");
   JButton jbtnB = newJButton("Beta");

   Main() {//www.java2s.comJFrame jfrm = newJFrame("A Button Example");
      jfrm.setLayout(newFlowLayout());
      jfrm.setSize(220, 90);
      jfrm.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

      jbtnA.addActionListener(this);
      jbtnB.addActionListener(this);

      jfrm.add(jbtnA);
      jfrm.add(jbtnB);

      jfrm.setVisible(true);
   }

   publicvoid actionPerformed(ActionEvent ae) {
      String ac = ae.getActionCommand();

      if (ac.equals("Alpha")) {
         if (jbtnB.isEnabled()) {
            System.out.println("Alpha pressed. Beta is disabled.");
            jbtnB.setEnabled(false);
         } else {
            System.out.println("Alpha pressed. Beta is enabled.");
            jbtnB.setEnabled(true);
         }
      } elseif (ac.equals("Beta"))
         System.out.println("Beta pressed.");
   }

   publicstaticvoid main(String args[]) {
      new Main();
   }
}
```

PreviousNext

## Related

- Java ActionEvent get event source
- Java ActionEvent cast event source to JButton
- Java ActionEvent compare event source to component instance
- Java ActionEvent get action id
- Java ActionEvent get event happened time
