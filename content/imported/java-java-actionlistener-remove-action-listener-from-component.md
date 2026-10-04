---
title: Java ActionListener remove action listener from component
nav: Java ActionListener remove...
description: Imported from the java2s.com archive: Java ActionListener remove action listener from component
section: Imported - java2s Archive
order: 1014
source: https://web.archive.org/web/20210102122101/http://www.java2s.com/ref/java/java-actionlistener-remove-action-listener-from-component.html
---
- java.awt.event
- java.awt.event ActionEvent ActionListener AdjustmentListener AWTEventListener ComponentListener ContainerListener FocusAdapter FocusEvent FocusListener HierarchyListener InputEvent Event ItemEvent ItemListener KeyAdapter KeyEvent KeyListener MouseAdapter MouseEvent MouseMotionAdapter MouseMotionListener MouseWheelListener WindowAdapter WindowEvent WindowFocusListener WindowStateListener

## Description

```java title=Example.java
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.ItemEvent;
import java.awt.event.ItemListener;
import javax.swing.JButton;
import javax.swing.JCheckBox;
import javax.swing.JFrame;
import javax.swing.JPanel;
publicclass Main {
   JButton add = newJButton("+");
   JCheckBox active = newJCheckBox("Active listener");
   ButtonListener buttonlistener = new ButtonListener();
   int count = 0;
   class ButtonListener implementsActionListener {
      publicvoid actionPerformed(ActionEvent e) {
         System.out.println(++count);
      }
   }
   public Main() {
      JPanel panel = newJPanel();
      active.addItemListener(newItemListener() {
         publicvoid itemStateChanged(ItemEvent event) {
            if (active.isSelected()) {
               add.addActionListener(buttonlistener);
            } else {
               add.removeActionListener(buttonlistener);
            }
         }
      });
      panel.add(add);
      panel.add(active);
      JFrame f = newJFrame();
      f.add(panel);
      f.setSize(310, 200);
      f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      f.setVisible(true);
   }
   publicstaticvoid main(String[] args) {
      new Main();
   }
}
```

PreviousNext

## Related

- Java ActionListener set JFrame background via action command
- Java ActionListener handle events from different components
- Java ActionListener add more than one action listener to JButton
- Java ActionListener handle action event on JComboBox
- Java ActionListener handle enter key pressed event for JTextField
