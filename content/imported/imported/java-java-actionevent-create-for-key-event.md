---
title: Java ActionEvent create for key event
nav: Java ActionEvent create fo...
description: ActionEvent actionEvent = newActionEvent(this, ActionEvent.ACTION_PERFORMED, keyText);
section: Imported - java2s Archive
order: 1032
source: https://web.archive.org/web/20210102122100/http://www.java2s.com/ref/java/java-actionevent-create-for-key-event.html
---
- java.awt.event
- java.awt.event ActionEvent ActionListener AdjustmentListener AWTEventListener ComponentListener ContainerListener FocusAdapter FocusEvent FocusListener HierarchyListener InputEvent Event ItemEvent ItemListener KeyAdapter KeyEvent KeyListener MouseAdapter MouseEvent MouseMotionAdapter MouseMotionListener MouseWheelListener WindowAdapter WindowEvent WindowFocusListener WindowStateListener

## Description

Java ActionEvent create for key event

```java title=Example.java
import java.awt.AWTEventMulticaster;
import java.awt.BorderLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;

import javax.swing.JComponent;
import javax.swing.JFrame;
import javax.swing.JTextField;

publicclass Main extendsJComponent {
   privateActionListener actionListenerList = null;

   public Main() {
      KeyListener internalKeyListener = newKeyAdapter() {
         publicvoid keyPressed(KeyEvent keyEvent) {
            if (actionListenerList != null) {
               int keyCode = keyEvent.getKeyCode();
               String keyText = KeyEvent.getKeyText(keyCode);
               ActionEvent actionEvent = newActionEvent(this, ActionEvent.ACTION_PERFORMED, keyText);
               actionListenerList.actionPerformed(actionEvent);
            }/*fromwww.java2s.com*/
         }
      };
      MouseListener internalMouseListener = newMouseAdapter() {
         publicvoid mousePressed(MouseEvent mouseEvent) {
            requestFocusInWindow();
         }
      };
      addKeyListener(internalKeyListener);
      addMouseListener(internalMouseListener);
   }

   publicvoid addActionListener(ActionListener actionListener) {
      actionListenerList = AWTEventMulticaster.add(actionListenerList, actionListener);
   }

   publicvoid removeActionListener(ActionListener actionListener) {
      actionListenerList = AWTEventMulticaster.remove(actionListenerList, actionListener);
   }

   publicboolean isFocusable() {
      return true;
   }

   publicstaticvoid main(String[] a) {
      JFrame frame = newJFrame("Key Text Sample");
      frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      Main keyTextComponent = new Main();
      finalJTextField textField = newJTextField();
      ActionListener actionListener = newActionListener() {
         publicvoid actionPerformed(ActionEvent actionEvent) {
            String keyText = actionEvent.getActionCommand();
            textField.setText(keyText);
         }
      };
      keyTextComponent.addActionListener(actionListener);
      frame.add(keyTextComponent, BorderLayout.CENTER);
      textField.setText("Press keyboard after clicking the above blank area");
      frame.add(textField, BorderLayout.SOUTH);
      frame.setSize(300, 200);
      frame.setVisible(true);
   }
}
```

PreviousNext

## Related

- Java ActionEvent is control key pressed
- Java ActionEvent is meta key pressed
- Java ActionEvent is shift key pressed
- Java ActionListener implement
- Java ActionListener set JFrame background via action command
