---
title: Java ActionListener set JFrame background via action command
nav: Java ActionListener set JF...
description: Imported from the java2s.com archive: Java ActionListener set JFrame background via action command
section: Imported - java2s Archive
order: 1015
source: https://web.archive.org/web/20210102122101/http://www.java2s.com/ref/java/java-actionlistener-set-jframe-background-via-action-command.html
---
- java.awt.event
- java.awt.event ActionEvent ActionListener AdjustmentListener AWTEventListener ComponentListener ContainerListener FocusAdapter FocusEvent FocusListener HierarchyListener InputEvent Event ItemEvent ItemListener KeyAdapter KeyEvent KeyListener MouseAdapter MouseEvent MouseMotionAdapter MouseMotionListener MouseWheelListener WindowAdapter WindowEvent WindowFocusListener WindowStateListener

## Description

```java title=Example.java
import java.awt.Color;
import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.SwingUtilities;
publicclass Main extendsJFrameimplementsActionListener {
   privatefinalString ACTION_ON = "LIGHT ON";
   privatefinalString ACTION_OFF = "LIGHT OFF";
   privatefinalString ACTION_CYCLE = "CYCLE COLOR";
   privatefinalColor[] COLORS = newColor[]{
         Color.white,
         Color.green,
         Color.red,
         Color.yellow,
         Color.orange,
         Color.pink
   };
   privateint currentColor = 0;
   privateboolean isLightOn = false;
   public Main() {
      setTitle("Disco Light Party Frame");
      setLayout(newFlowLayout());
      setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      JButton btnOffOn = newJButton("Lights On");
      JButton btnColor = newJButton("Cycle Color");
      btnOffOn.setActionCommand(ACTION_ON);
      btnColor.setActionCommand(ACTION_CYCLE);
      btnOffOn.addActionListener(this);
      btnColor.addActionListener(this);
      getContentPane().add(btnOffOn);
      getContentPane().add(btnColor);
      pack();
      setVisible(true);
   }
   @Overridepublicvoid actionPerformed(ActionEvent ev) {
      String action = ev.getActionCommand();
      System.err.println("Got action "+action);
      switch (action) {
      case ACTION_ON:
         isLightOn = true;
         getContentPane().setBackground(COLORS[currentColor]);
         ((JButton) ev.getSource()).setText("Lights Off");
         ((JButton) ev.getSource()).setActionCommand(ACTION_OFF);
         break;
      case ACTION_OFF:
         isLightOn = false;
         getContentPane().setBackground(Color.black);
         ((JButton) ev.getSource()).setText("Lights On");
         ((JButton) ev.getSource()).setActionCommand(ACTION_ON);
         break;
      case ACTION_CYCLE:
         if (isLightOn)
            getContentPane().setBackground(COLORS[++currentColor
               % COLORS.length]);
         break;
      }
   }
   publicstaticvoid main(String[] args) {
      SwingUtilities.invokeLater(newRunnable() {
         publicvoid run() {
            new Main();
      }
      });
   }
}
```

PreviousNext

## Related

- Java ActionEvent is shift key pressed
- Java ActionEvent create for key event
- Java ActionListener implement
- Java ActionListener handle events from different components
- Java ActionListener add more than one action listener to JButton
