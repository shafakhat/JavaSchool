---
title: Adding Image-Dragging Behavior
nav: Adding Image-Dragging Beha...
description: Adding Image-Dragging Behavior : Java examples (example source code) » 2D Graphics GUI » Image
section: Imported - java2s Archive
order: 1012
source: https://web.archive.org/web/20060514223114/http://www.java2s.com:80/Code/Java/2D-Graphics-GUI/AddingImageDraggingBehavior.htm
---
Adding Image-Dragging Behavior : Java examples (example source code) » 2D Graphics GUI » Image

```java title=Example.java
import java.awt.BorderLayout;
import java.awt.Container;
import java.awt.Image;
import java.awt.datatransfer.Clipboard;
import java.awt.datatransfer.DataFlavor;
import java.awt.datatransfer.Transferable;
import java.awt.datatransfer.UnsupportedFlavorException;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.io.IOException;
import javax.swing.Icon;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JComponent;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextField;
import javax.swing.TransferHandler;
public class DragImage {
  public static void main(String args[]) {
    JFrame frame = new JFrame("Clip Image");
    Container contentPane = frame.getContentPane();
    final Clipboard clipboard = frame.getToolkit().getSystemClipboard();
    Icon icon = new ImageIcon("jaeger.jpg");
    final JLabel label = new JLabel(icon);
    label.setTransferHandler(new ImageSelection());
    MouseListener mouseListener = new MouseAdapter() {
      public void mousePressed(MouseEvent e) {
        JComponent comp = (JComponent) e.getSource();
        TransferHandler handler = comp.getTransferHandler();
        handler.exportAsDrag(comp, e, TransferHandler.COPY);
      }
    };
    label.addMouseListener(mouseListener);
    JScrollPane pane = new JScrollPane(label);
    contentPane.add(pane, BorderLayout.CENTER);
    JButton copy = new JButton("Copy");
    copy.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent e) {
        TransferHandler handler = label.getTransferHandler();
        handler.exportToClipboard(label, clipboard,
            TransferHandler.COPY);
      }
    });
    JButton clear = new JButton("Clear");
    clear.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent actionEvent) {
        label.setIcon(null);
      }
    });
    clear.setTransferHandler(new TransferHandler("text"));
    mouseListener = new MouseAdapter() {
      public void mousePressed(MouseEvent e) {
        JComponent comp = (JComponent) e.getSource();
        TransferHandler handler = comp.getTransferHandler();
        handler.exportAsDrag(comp, e, TransferHandler.COPY);
      }
    };
    clear.addMouseListener(mouseListener);
    JButton paste = new JButton("Paste");
    paste.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent actionEvent) {
        Transferable clipData = clipboard.getContents(clipboard);
        if (clipData != null) {
          if (clipData.isDataFlavorSupported(DataFlavor.imageFlavor)) {
            TransferHandler handler = label.getTransferHandler();
            handler.importData(label, clipData);
          }
        }
      }
    });
    JPanel p = new JPanel();
    p.add(copy);
    p.add(clear);
    p.add(paste);
    contentPane.add(p, BorderLayout.SOUTH);
    JTextField tf = new JTextField();
    tf.setDragEnabled(true);
    contentPane.add(tf, BorderLayout.NORTH);
    frame.setSize(300, 300);
    frame.show();
  }
}
class ImageSelection extends TransferHandler implements Transferable {
  private static final DataFlavor flavors[] = { DataFlavor.imageFlavor };
  private JLabel source;
  private Image image;
  public int getSourceActions(JComponent c) {
    return TransferHandler.COPY;
  }
  public boolean canImport(JComponent comp, DataFlavor flavor[]) {
    if (!(comp instanceof JLabel)) {
      return false;
    }
    for (int i = 0, n = flavor.length; i < n; i++) {
      for (int j = 0, m = flavors.length; j < m; j++) {
        if (flavor[i].equals(flavors[j])) {
          return true;
        }
      }
    }
    return false;
  }
  public Transferable createTransferable(JComponent comp) {
    // Clear
    source = null;
    image = null;
    if (comp instanceof JLabel) {
      JLabel label = (JLabel) comp;
      Icon icon = label.getIcon();
      if (icon instanceof ImageIcon) {
        image = ((ImageIcon) icon).getImage();
        source = label;
        return this;
      }
    }
    return null;
  }
  public boolean importData(JComponent comp, Transferable t) {
    if (comp instanceof JLabel) {
      JLabel label = (JLabel) comp;
      if (t.isDataFlavorSupported(flavors[0])) {
        try {
          image = (Image) t.getTransferData(flavors[0]);
          ImageIcon icon = new ImageIcon(image);
          label.setIcon(icon);
          return true;
        } catch (UnsupportedFlavorException ignored) {
        } catch (IOException ignored) {
        }
      }
    }
    return false;
  }
  // Transferable
  public Object getTransferData(DataFlavor flavor) {
    if (isDataFlavorSupported(flavor)) {
      return image;
    }
    return null;
  }
  public DataFlavor[] getTransferDataFlavors() {
    return flavors;
  }
  public boolean isDataFlavorSupported(DataFlavor flavor) {
    return flavor.equals(DataFlavor.imageFlavor);
  }
}
```

Related examples in the same category
---
1. Image size
2. Image demo
3. Paint an Icon
4. Image Processing: Brightness and Contrast
5. Image with mouse drag and move event
6. Image Animation and Thread
7. Image Color Gray Effect
8. Image Buffering
9. Image Effect: Combine
10. AffineTransform demo
11. Image Effect: Rotate Image using DataBuffer
12. Image Effect: Sharpen, blur
13. Image scale
14. Image crop
15. Demonstrating the Drawing of an Image with a Convolve Operation
16. Demonstrating Use of the Image I/O Library
17. Sending Image Objects through the Clipboard
18. Anti Alias
19. Image Operations
20. Image Viewer
21. Standalone Image Viewer - works with any AWT-supported format
22. Toolkit.getImage() which works the same in either Applet or Application
23. Image Processing Test
24. Image Transfer Test
25. Double Buffered Image
26. Graband Fade: displays image and fades to black
27. Graband Fade with Rasters
28. Rotate Image 45 Degrees
29. Convert java.awt.image.BufferedImage to java.awt.Image
30. Filter image by multiplier its red, green and blue color
31. Drags within the image
