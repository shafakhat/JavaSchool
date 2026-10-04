---
title: Java AWT FocusEvent is temporary
nav: Java AWT FocusEvent is tem...
description: Imported from java2s.com: Java AWT FocusEvent is temporary
section: Imported
order: 20094
source: http://www.java2s.com/ref/java/java-awt-focusevent-is-temporary.html
---
- java.awt.event
- java.awt.event ActionEvent ActionListener AdjustmentListener AWTEventListener ComponentListener ContainerListener FocusAdapter FocusEvent FocusListener HierarchyListener InputEvent Event ItemEvent ItemListener KeyAdapter KeyEvent KeyListener MouseAdapter MouseEvent MouseMotionAdapter MouseMotionListener MouseWheelListener WindowAdapter WindowEvent WindowFocusListener WindowStateListener

## Description

Java AWT FocusEvent is temporary

```java title=Example.java
import java.awt.FlowLayout;
import java.awt.event.FocusAdapter;
import java.awt.event.FocusEvent;

import javax.swing.JFrame;
import javax.swing.JTextField;
import javax.swing.text.JTextComponent;

publicclass Main {
  publicstaticvoid main(String[] argv) throwsException {
    JTextField component = newJTextField(10);
    JTextField component1 = newJTextField(10);
    component.addFocusListener(new MyFocusListener());
    component1.addFocusListener(new MyFocusListener());
    JFrame f = newJFrame();
    f.setLayout(newFlowLayout());
    f.add(component1);/*fromwww.java2s.com*/
    f.add(component);
    f.pack();
    f.setVisible(true);

  }
}
class MyFocusListener extendsFocusAdapter {
  boolean showingDialog = false;

  publicvoid focusGained(FocusEvent evt) {
    finalJTextComponent c = (JTextComponent) evt.getSource();
    String s = c.getText();

    for (int i = 0; i < s.length(); i++) {
      if (!Character.isDigit(s.charAt(i))) {
        c.setSelectionStart(i);
        c.setSelectionEnd(i);
        break;
      }
    }
  }

  publicvoid focusLost(FocusEvent evt) {
    finalJTextComponent c = (JTextComponent) evt.getSource();
    String s = c.getText();

    if (evt.isTemporary()) {
      return;
    }
    for (int i = 0; i < s.length(); i++) {
      if (!Character.isDigit(s.charAt(i))) {
        System.out.println("must only contain digits");
        c.requestFocus();
        break;
      }
    }
  }
}
```

PreviousNext

## Related

- Java AWT ComponentListener handle component event
- Java AWT ContainerListener handle container event
- Java FocusAdapter handle focus event
- Java AWT FocusEvent get opposite focus component
- Java FocusListener get component gained focus
