---
title: Java Swing Tutorial - Java EventQueue .invokeLater (Runnable runnable)
nav: Java Swing Tutorial - Java...
description: EventQueue.invokeLater(Runnable runnable) has the following syntax.
section: Imported - java2s Archive
order: 1021
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/EventQueue/0180__EventQueue.invokeLater_Runnable_runnable_.htm
---
```java title=Example.java
Back to EventQueue  ↑
```

## Syntax

EventQueue.invokeLater(Runnable runnable) has the following syntax.

```java title=Example.java
publicstaticvoid invokeLater(Runnable runnable)
```

## Example

In the following code shows how to use EventQueue.invokeLater(Runnable runnable) method.

```java title=Example.java
import java.awt.EventQueue;
import javax.swing.JFrame;
publicclass Main {
   publicstaticvoid main(String[] args)
   {
      EventQueue.invokeLater(new Runnable()
         {
            publicvoid run()
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

- Back to EventQueue ↑
