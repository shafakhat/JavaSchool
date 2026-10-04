---
title: Java ActionEvent get event happened time
nav: Java ActionEvent get event...
description: Imported from the java2s.com archive: Java ActionEvent get event happened time
section: Imported - java2s Archive
order: 1003
source: https://web.archive.org/web/20210102122059/http://www.java2s.com/ref/java/java-actionevent-get-event-happened-time.html
---
- java.awt.event
- java.awt.event ActionEvent ActionListener AdjustmentListener AWTEventListener ComponentListener ContainerListener FocusAdapter FocusEvent FocusListener HierarchyListener InputEvent Event ItemEvent ItemListener KeyAdapter KeyEvent KeyListener MouseAdapter MouseEvent MouseMotionAdapter MouseMotionListener MouseWheelListener WindowAdapter WindowEvent WindowFocusListener WindowStateListener

## Description

```java title=Example.java
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.text.DateFormat;
import java.util.Calendar;
import java.util.Date;
import java.util.Locale;

import javax.swing.JButton;
import javax.swing.JFrame;

publicclass Main {
  publicstaticvoid main(String[] args) {
    JFrame f = newJFrame();
    JButton ok = newJButton("Ok");

    ok.addActionListener(newActionListener() {
      publicvoid actionPerformed(ActionEvent event) {
        Calendar cal = Calendar.getInstance();
        cal.setTimeInMillis(event.getWhen());
        System.out.println(cal.getTime());

        if (event.getID() == ActionEvent.ACTION_PERFORMED)
          System.out.println(" Event Id: ACTION_PERFORMED");

        String source = event.getSource().getClass().getName();
        System.out.println(" Source: " + source);

        int mod = event.getModifiers();
        if ((mod & ActionEvent.ALT_MASK) > 0)
          System.out.println("Alt ");

        if ((mod & ActionEvent.SHIFT_MASK) > 0)
          System.out.println("Shift ");

        if ((mod & ActionEvent.META_MASK) > 0)
          System.out.println("Meta ");

        if ((mod & ActionEvent.CTRL_MASK) > 0)
          System.out.println("Ctrl ");

      }/*fromwww.java2s.com*/
    });

    f.add(ok);

    f.setSize(420, 250);
    f.setLocationRelativeTo(null);
    f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    f.setVisible(true);
  }
}
```

PreviousNext

## Related

- Java ActionEvent compare event source to component instance
- Java ActionEvent get action command
- Java ActionEvent get action id
- Java ActionEvent get modifiers
- Java ActionEvent is alt key pressed
