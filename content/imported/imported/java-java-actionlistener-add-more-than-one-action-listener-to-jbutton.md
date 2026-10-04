---
title: Java ActionListener add more than one action listener to JButton
nav: Java ActionListener add mo...
description: Java ActionListener add more than one action listener to JButton
section: Imported - java2s Archive
order: 1010
source: https://web.archive.org/web/20210102122101/http://www.java2s.com/ref/java/java-actionlistener-add-more-than-one-action-listener-to-jbutton.html
---
- java.awt.event
- java.awt.event ActionEvent ActionListener AdjustmentListener AWTEventListener ComponentListener ContainerListener FocusAdapter FocusEvent FocusListener HierarchyListener InputEvent Event ItemEvent ItemListener KeyAdapter KeyEvent KeyListener MouseAdapter MouseEvent MouseMotionAdapter MouseMotionListener MouseWheelListener WindowAdapter WindowEvent WindowFocusListener WindowStateListener

## Description

```java title=Example.java
import java.awt.BorderLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JSpinner;

publicclass Main {
  JLabel statusbar = newJLabel("0");
  JSpinner spinner = newJSpinner();
  JButton add = newJButton("+");
  staticint count = 0;

  class ButtonListener1 implementsActionListener {
    publicvoid actionPerformed(ActionEvent e) {
      Integerval = (Integer) spinner.getValue();
      spinner.setValue(++val);
    }//fromwww.java2s.com
  }

  class ButtonListener2 implementsActionListener {
    publicvoid actionPerformed(ActionEvent e) {
      statusbar.setText(Integer.toString(++count));
    }
  }

  public Main() {
    JPanel panel = newJPanel();

    add.addActionListener(new ButtonListener1());
    add.addActionListener(new ButtonListener2());

    panel.add(add);
    panel.add(spinner);
    JFrame f = newJFrame();
    f.add(panel);
    f.add(statusbar, BorderLayout.SOUTH);

    f.setSize(300, 200);
    f.setLocationRelativeTo(null);
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

- Java ActionListener implement
- Java ActionListener set JFrame background via action command
- Java ActionListener handle events from different components
- Java ActionListener remove action listener from component
- Java ActionListener handle action event on JComboBox
