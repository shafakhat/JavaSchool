---
title: Java Tutorial - Java EventQueue .invokeAndWait (Runnable runnable)
nav: Java Tutorial - Java Event...
description: EventQueue.invokeAndWait(Runnable runnable) has the following syntax.
section: Imported - java2s Archive
order: 1022
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/EventQueue/Java_EventQueue_invokeAndWait_Runnable_runnable_.htm
---
### Syntax

EventQueue.invokeAndWait(Runnable runnable) has the following syntax.

```java title=Example.java
publicstaticvoid invokeAndWait(Runnable runnable)    throws InterruptedException ,     InvocationTargetException
```

### Example

In the following code shows how to use EventQueue.invokeAndWait(Runnable runnable) method.

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

BasicStrokeBorderLayoutCardLayoutColorCursorDesktopDesktopManagerDisplayModeEventQueueFlowLayoutFocusTraversalPolicyFontFontMetricsGradientPaintGraphicsGraphics2DGraphicsConfigurationGraphicsDeviceGraphicsEnvironmentGridBagConstraintsGridBagLayoutGridLayoutImageItemSelectableKeyboardFocusManagerLayoutManagerLayoutManager2PointRectangleRobotShapeSplashScreenSystemColorSystemTrayTexturePaintTrayIconToolkitTransparency
