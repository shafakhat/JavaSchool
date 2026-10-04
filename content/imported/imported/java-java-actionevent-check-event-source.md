---
title: Java ActionEvent check event source
nav: Java ActionEvent check eve...
description: JOptionPane.showMessageDialog(Main.this, "You didn't enter anything!", "Moron",
section: Imported - java2s Archive
order: 1030
source: https://web.archive.org/web/20210102122058/http://www.java2s.com/ref/java/java-actionevent-check-event-source.html
---
- java.awt.event
- java.awt.event ActionEvent ActionListener AdjustmentListener AWTEventListener ComponentListener ContainerListener FocusAdapter FocusEvent FocusListener HierarchyListener InputEvent Event ItemEvent ItemListener KeyAdapter KeyEvent KeyListener MouseAdapter MouseEvent MouseMotionAdapter MouseMotionListener MouseWheelListener WindowAdapter WindowEvent WindowFocusListener WindowStateListener

## Description

Java ActionEvent check event source

```java title=Example.java
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextField;

publicclass Main extendsJFrame {
  privateJButton buttonOK = newJButton("OK");
  privateJTextField textName = newJTextField(15);

  public Main() {
    setSize(325, 100);//fromwww.java2s.com
    setTitle("Who Are You?");
    setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

    ButtonListener bl = new ButtonListener();
    JPanel panel1 = newJPanel();
    panel1.add(newJLabel("Enter your name: "));
    panel1.add(textName);
    panel1.add(buttonOK);

    buttonOK.addActionListener(bl);

    add(panel1);
    pack();
    setVisible(true);
  }

  privateclass ButtonListener implementsActionListener {
    publicvoid actionPerformed(ActionEvent e) {
      if (e.getSource() == buttonOK) {
        String name = textName.getText();
        if (name.length() == 0) {
          JOptionPane.showMessageDialog(Main.this, "You didn't enter anything!", "Moron",
              JOptionPane.INFORMATION_MESSAGE);
        } else {
          JOptionPane.showMessageDialog(Main.this, "Good morning " + textName.getText(), "Salutations",
              JOptionPane.INFORMATION_MESSAGE);
        }
        textName.requestFocus();
      }
    }
  }
  publicstaticvoid main(String[] args) {
    new Main();
  }
}
```

PreviousNext

## Related

- Java AWT Toolkit check supported window state
- Java AWT Toolkit add event listener by mask
- Java AWT Clipboard get/set text data
- Java ActionEvent get action command text
- Java ActionEvent get event source
