---
title: Java ActionEvent get event source
nav: Java ActionEvent get event...
description: Imported from the java2s.com archive: Java ActionEvent get event source
section: Imported - java2s Archive
order: 1004
source: https://web.archive.org/web/20210102122059/http://www.java2s.com/ref/java/java-actionevent-get-event-source.html
---
- java.awt.event
- java.awt.event ActionEvent ActionListener AdjustmentListener AWTEventListener ComponentListener ContainerListener FocusAdapter FocusEvent FocusListener HierarchyListener InputEvent Event ItemEvent ItemListener KeyAdapter KeyEvent KeyListener MouseAdapter MouseEvent MouseMotionAdapter MouseMotionListener MouseWheelListener WindowAdapter WindowEvent WindowFocusListener WindowStateListener

## Description

```java title=Example.java
import java.awt.FlowLayout;

import javax.swing.JButton;
import javax.swing.JFrame;

publicclass Main extendsJFrame {
  public Main() {
    super("JButton");

    setDefaultCloseOperation(EXIT_ON_CLOSE);
    setLayout(newFlowLayout());

    /*fromwww.java2s.com*/JButton bn = newJButton("Close");
    bn.addActionListener(e->{
      System.out.println(e.getSource() == bn);
    });

    getContentPane().add(bn);
  }

  publicstaticvoid main(String[] args) {
    Main frame = new Main();
    frame.pack();
    frame.setVisible(true);
  }
}
```

```java title=Example.java
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;

publicclass Main {
  publicstaticvoid main(String[] args) {
    JPanel panel = newJPanel();

    JButton close = newJButton("Close");
    close.addActionListener(new ButtonListener());

    JButton open = newJButton("Open");
    open.addActionListener(new ButtonListener());

    JButton find = newJButton("Find");
    find.addActionListener(new ButtonListener());

    JButton save = newJButton("Save");
    save.addActionListener(new ButtonListener());

    panel.add(close);/*www.java2s.com*/
    panel.add(open);
    panel.add(find);
    panel.add(save);
    JFrame f = newJFrame();
    f.add(panel);
    f.setSize(400, 300);
    f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    f.setVisible(true);
  }
}

class ButtonListener implementsActionListener {
  publicvoid actionPerformed(ActionEvent e) {
    JButton o = (JButton) e.getSource();
    String label = o.getText();
    System.out.println(label + " button clicked");
  }
}
```

PreviousNext

## Related

- Java AWT Clipboard get/set text data
- Java ActionEvent check event source
- Java ActionEvent get action command text
- Java ActionEvent cast event source to JButton
- Java ActionEvent compare event source to component instance
