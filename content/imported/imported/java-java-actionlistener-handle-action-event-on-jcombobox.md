---
title: Java ActionListener handle action event on JComboBox
nav: Java ActionListener handle...
description: Imported from the java2s.com archive: Java ActionListener handle action event on JComboBox
section: Imported - java2s Archive
order: 1011
source: https://web.archive.org/web/20210102122101/http://www.java2s.com/ref/java/java-actionlistener-handle-action-event-on-jcombobox.html
---
- java.awt.event
- java.awt.event ActionEvent ActionListener AdjustmentListener AWTEventListener ComponentListener ContainerListener FocusAdapter FocusEvent FocusListener HierarchyListener InputEvent Event ItemEvent ItemListener KeyAdapter KeyEvent KeyListener MouseAdapter MouseEvent MouseMotionAdapter MouseMotionListener MouseWheelListener WindowAdapter WindowEvent WindowFocusListener WindowStateListener

## Description

Java ActionListener handle action event on JComboBox

```java title=Example.java
import java.awt.FlowLayout;

import javax.swing.ImageIcon;
import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;

class Demo extendsJPanel {
   JLabel jlab = newJLabel();

   public Demo() {

      JComboBox<String> jcb;

      String options[] = { "CSS", "HTML", "Java", "Javascript" };

      setLayout(newFlowLayout());

      jcb = newJComboBox<String>(options);
      add(jcb);//www.java2s.com

      jcb.addActionListener(e -> {
         String s = (String) jcb.getSelectedItem();
         jlab.setText(s);
      });
      // Create a label and add it to the content pane.
      jlab.setText("not selection");
      add(jlab);
   }
}

publicclass Main {
   publicstaticvoid main(String[] args) {
      JFrame application = newJFrame();
      application.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      application.add(new Demo());
      application.setSize(250, 250);
      application.setVisible(true);
   }
}
```

PreviousNext

## Related

- Java ActionListener handle events from different components
- Java ActionListener add more than one action listener to JButton
- Java ActionListener remove action listener from component
- Java ActionListener handle enter key pressed event for JTextField
- Java AWT AdjustmentListener handle adjustment event
