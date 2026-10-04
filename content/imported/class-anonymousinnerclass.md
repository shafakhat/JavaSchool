---
title: Anonymous inner class
nav: Anonymous inner class
description: Imported from the java2s.com archive: Anonymous inner class
section: Imported - java2s Archive
order: 1132
source: https://web.archive.org/web/20090531211831/http://www.java2s.com:80/Code/Java/Class/Anonymousinnerclass.htm
---
Anonymous inner class

```java title=Example.java
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JButton;
import javax.swing.JFrame;
public class SimpleEvent {
  public static void main(String[] args) {
    JButton close = new JButton("Close");
    close.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent event) {
        System.exit(0);
      }
    });
    JFrame f = new JFrame();
    f.add(close);
    f.setSize(300, 200);
    f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    f.setVisible(true);
  }
}
```

1.  an example of a simple anonymous class
---  ---
2.  Tick Tock with an Anonymous Class
3.  Access inner class from outside
