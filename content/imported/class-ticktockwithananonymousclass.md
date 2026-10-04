---
title: Tick Tock with an Anonymous Class
nav: Tick Tock with an Anonymou...
description: JOptionPane.showMessageDialog(null, "Click OK to exit program");
section: Imported - java2s Archive
order: 1094
source: https://web.archive.org/web/20090531215018/http://www.java2s.com:80/Code/Java/Class/TickTockwithanAnonymousClass.htm
---
Tick Tock with an Anonymous Class

```java title=Example.java
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JOptionPane;
import javax.swing.Timer;
public class MainClass {
  private String tickMessage = "Tick...";
  private String tockMessage = "Tock...";
  public static void main(String[] args) {
    TickTockAnonymous t = new TickTockAnonymous();
    t.go();
  }
  private void go() {
    Timer t = new Timer(1000, new ActionListener() {
      private boolean tick = true;
      public void actionPerformed(ActionEvent event) {
        if (tick) {
          System.out.println(tickMessage);
        } else {
          System.out.println(tockMessage);
        }
        tick = !tick;
      }
    });
    t.start();
    JOptionPane.showMessageDialog(null, "Click OK to exit program");
    System.exit(0);
  }
}
```

1.  an example of a simple anonymous class
---  ---
2.  Access inner class from outside
3.  Anonymous inner class
