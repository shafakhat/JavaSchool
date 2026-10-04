---
title: Java AWT AdjustmentListener handle adjustment event
nav: Java AWT AdjustmentListene...
description: privateJScrollBar bar = newJScrollBar(SwingConstants.HORIZONTAL, 50, 10, 0, 100);
section: Imported
order: 20047
source: http://www.java2s.com/ref/java/java-awt-adjustmentlistener-handle-adjustment-event.html
---
- java.awt.event
- java.awt.event ActionEvent ActionListener AdjustmentListener AWTEventListener ComponentListener ContainerListener FocusAdapter FocusEvent FocusListener HierarchyListener InputEvent Event ItemEvent ItemListener KeyAdapter KeyEvent KeyListener MouseAdapter MouseEvent MouseMotionAdapter MouseMotionListener MouseWheelListener WindowAdapter WindowEvent WindowFocusListener WindowStateListener

## Description

Java AWT AdjustmentListener handle adjustment event

```java title=Example.java
import java.awt.BorderLayout;
import java.awt.event.AdjustmentEvent;
import java.awt.event.AdjustmentListener;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JScrollBar;
import javax.swing.SwingConstants;

publicclass Main extendsJFrameimplementsAdjustmentListener {
   privateJScrollBar bar = newJScrollBar(SwingConstants.HORIZONTAL, 50, 10, 0, 100);

   public Main() {
      setSize(350, 100);/*fromwww.java2s.com*/
      setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      bar.addAdjustmentListener(this);
      JPanel pane = newJPanel();
      pane.setLayout(newBorderLayout());
      pane.add(bar, "South");
      setContentPane(pane);
   }

   publicvoid adjustmentValueChanged(AdjustmentEvent evt) {
      Object source = evt.getSource();
      int newValue = bar.getValue();
      System.out.println(newValue);
      repaint();
   }

   publicstaticvoid main(String[] arguments) {
      JFrame frame = new Main();
      frame.setVisible(true);
   }

}
```

PreviousNext

## Related

- Java ActionListener remove action listener from component
- Java ActionListener handle action event on JComboBox
- Java ActionListener handle enter key pressed event for JTextField
- Java AWTEventListener create custom event listener
- Java AWT ComponentListener handle component event
