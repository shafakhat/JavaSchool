---
title: Eliminating race Conditions using Swing Components : Java examples (example source code) » Threads » Swing Thread
nav: Eliminating race Condition...
description: Eliminating race Conditions using Swing Components : Java examples (example source code) » Threads » Swing Thread
section: Imported - java2s Archive
order: 1052
source: https://web.archive.org/web/20060505234047/http://www.java2s.com:80/Code/Java/Threads/EliminatingraceConditionsusingSwingComponents.htm
---
Eliminating race Conditions using Swing Components : Java examples (example source code) » Threads » Swing Thread

Eliminating race Conditions using Swing Components

```java title=Example.java
// : c14:InvokeLaterFrame.java
// Eliminating race Conditions using Swing Components.
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
import java.awt.BorderLayout;
import java.awt.Container;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import javax.swing.JFrame;
import javax.swing.JTextField;
import javax.swing.SwingUtilities;
public class InvokeLaterFrame extends JFrame {
  private JTextField statusField = new JTextField("Initial Value");
  public InvokeLaterFrame() {
    Container cp = getContentPane();
    cp.add(statusField, BorderLayout.NORTH);
    addWindowListener(new WindowAdapter() {
      public void windowOpened(WindowEvent e) {
        try { // Simulate initialization overhead
          Thread.sleep(2000);
        } catch (InterruptedException ex) {
          throw new RuntimeException(ex);
        }
        statusField.setText("Initialization complete");
      }
    });
  }
  public static void main(String[] args) {
    final InvokeLaterFrame ilf = new InvokeLaterFrame();
    run(ilf, 150, 60);
    // Use invokeAndWait() to synchronize output to prompt:
    // SwingUtilities.invokeAndWait(new Runnable() {
    SwingUtilities.invokeLater(new Runnable() {
      public void run() {
        ilf.statusField.setText("Application ready");
      }
    });
    System.out.println("Done");
  }
  public static void run(JFrame frame, int width, int height) {
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setSize(width, height);
    frame.setVisible(true);
  }
} ///:~
```

Related examples in the same category
---
1. GUI clock
2. Race Conditions using Swing Components
3. Using the Runnable interface
4. Write your Beans this way so they can run in a multithreaded environment
5. User interface responsiveness
6. InvokeExample: Swing and thread
7. Counter: Swing and thread
8. Thread accuracy: Swing and threads
9. Swing and thread: invoke and wait
10. Swing and threads: invoke later
11. Swing and threads: slide
12. Swing and threads: scroll text
13. Animation: Swing and thread
14. Swing and Thread for length operation
15. Swing and Thread: cancel a lengthy operation
16. Swing and Thread: repaint
17. Swing Thread Test
18. Thread and Swing 1
19. Thread and Swing 2
20. Thread and Swing 3
21. Swing Type Tester 10
