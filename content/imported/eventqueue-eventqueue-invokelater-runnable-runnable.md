---
title: Java Swing Tutorial - Java EventQueue .invokeLater (Runnable runnable)
nav: Java Swing Tutorial - Java...
description: EventQueue.invokeLater(Runnable runnable) has the following syntax.
section: Imported - java2s Archive
order: 1005
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/EventQueue/0180__EventQueue.invokeLater_Runnable_runnable_.htm
---
## Syntax

EventQueue.invokeLater(Runnable runnable) has the following syntax.

```java title=Example.java
public static void invokeLater(Runnable runnable)
```

## Example

In the following code shows how to use EventQueue.invokeLater(Runnable runnable) method.

```java title=Example.java
import java.awt.EventQueue;
import javax.swing.JFrame;
public class Main {
   public static void main(String[] args)
   {
      EventQueue.invokeLater(new Runnable()
         {
            public void run()
            {
               JFrame frame = new ImageProcessingFrame();
               frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
               frame.setVisible(true);
            }
         });
   }
}
class ImageProcessingFrame extends JFrame
{
   public ImageProcessingFrame()
   {
      setTitle("ImageProcessingTest");
      setSize(200, 200);
   }
}
```
