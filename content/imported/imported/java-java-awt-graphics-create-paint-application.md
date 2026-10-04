---
title: Java AWT Graphics create paint application
nav: Java AWT Graphics create p...
description: }//www.java2s.compublic SimplePaintPanel(Set<Point> blackPixels) {
section: Imported
order: 20118
source: http://www.java2s.com/ref/java/java-awt-graphics-create-paint-application.html
---
- java.awt
- java.awt AWTEvent BasicStroke BorderLayout CardLayout Color Component Container Dimension EventQueue FileDialog FlowLayout FocusTraversalPolicy Font FontMetrics GradientPaint Graphics Graphics2D GraphicsDevice GridBagConstraints GridBagLayout GridLayout Image Insets ItemSelectable KeyboardFocusManager KeyEventDispatcher LayoutManager2 LinearGradientPaint Point RadialGradientPaint Rectangle TexturePaint Toolkit

## Introduction

The following code creates a paint application

```java title=Example.java
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.Point;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.Collection;
import java.util.HashSet;
import java.util.Set;

import javax.imageio.ImageIO;
import javax.swing.JFileChooser;
import javax.swing.JFrame;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JPanel;
import javax.swing.SwingUtilities;

class SimplePaintPanel extendsJPanel {
   privatefinalSet<Point> blackPixels = newHashSet<Point>();
   privatefinalint brushSize;

   privateint mouseButtonDown = 0;

   public SimplePaintPanel() {
      this(5, newHashSet<Point>());
   }//www.java2s.compublic SimplePaintPanel(Set<Point> blackPixels) {
      this(5, blackPixels);
   }

   public SimplePaintPanel(int brushSize, Set<Point> blackPixels) {
      this.setPreferredSize(newDimension(300, 300));
      this.brushSize = brushSize;
      this.blackPixels.addAll(blackPixels);
      final SimplePaintPanel self = this;

      MouseAdapter mouseAdapter = newMouseAdapter() {
         @Overridepublicvoid mouseDragged(MouseEvent ev) {
            if (mouseButtonDown == 1)
               addPixels(getPixelsAround(ev.getPoint()));
            elseif (mouseButtonDown == 3)
               removePixels(getPixelsAround(ev.getPoint()));
         }

         @Overridepublicvoid mousePressed(MouseEvent ev) {
            self.mouseButtonDown = ev.getButton();
         }
      };
      this.addMouseMotionListener(mouseAdapter);
      this.addMouseListener(mouseAdapter);

   }

   publicvoid paint(Graphics g) {
      int w = this.getWidth();
      int h = this.getHeight();
      g.setColor(Color.white);
      g.fillRect(0, 0, w, h);
      g.setColor(Color.black);
      for (Point point : blackPixels)
         g.drawRect(point.x, point.y, 1, 1);

   }

   publicvoid clear() {
      this.blackPixels.clear();
      this.invalidate();
      this.repaint();
   }

   publicvoid addPixels(Collection<? extendsPoint> blackPixels) {
      this.blackPixels.addAll(blackPixels);
      this.invalidate();
      this.repaint();
   }

   publicvoid removePixels(Collection<? extendsPoint> blackPixels) {
      this.blackPixels.removeAll(blackPixels);
      this.invalidate();
      this.repaint();
   }

   publicboolean isPixel(Point blackPixel) {
      returnthis.blackPixels.contains(blackPixel);
   }

   privateCollection<? extendsPoint> getPixelsAround(Point point) {
      Set<Point> points = newHashSet<>();
      for (int x = point.x - brushSize; x < point.x + brushSize; x++)
         for (int y = point.y - brushSize; y < point.y + brushSize; y++)
            points.add(newPoint(x, y));
      return points;
   }
}

publicclass Main extendsJFrameimplementsActionListener {
   privatefinalString ACTION_NEW = "New Image";
   privatefinalString ACTION_LOAD = "Load Image";
   privatefinalString ACTION_SAVE = "Save Image";

   privatefinal SimplePaintPanel paintPanel = new SimplePaintPanel();

   public Main() {
      super();
      setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      setTitle("Simple Paint");

      initMenu();
      this.getContentPane().add(paintPanel);

      pack();
      setVisible(true);
   }

   privatevoid initMenu() {
      JMenuBar menuBar = newJMenuBar();
      JMenu menu = newJMenu("File");
      JMenuItem mnuNew = newJMenuItem(ACTION_NEW);
      JMenuItem mnuLoad = newJMenuItem(ACTION_LOAD);
      JMenuItem mnuSave = newJMenuItem(ACTION_SAVE);
      mnuNew.setActionCommand(ACTION_NEW);
      mnuLoad.setActionCommand(ACTION_LOAD);
      mnuSave.setActionCommand(ACTION_SAVE);
      mnuNew.addActionListener(this);
      mnuLoad.addActionListener(this);
      mnuSave.addActionListener(this);
      menu.add(mnuNew);
      menu.add(mnuLoad);
      menu.add(mnuSave);
      menuBar.add(menu);
      this.setJMenuBar(menuBar);
   }

   @Overridepublicvoid actionPerformed(ActionEvent ev) {
      switch (ev.getActionCommand()) {
      case ACTION_NEW:
         paintPanel.clear();
         break;
      case ACTION_LOAD:
         doLoadImage();
         break;
      case ACTION_SAVE:
         doSaveImage();
         break;
      }
   }

   privatevoid doSaveImage() {
      JFileChooser fileChooser = newJFileChooser();
      fileChooser.setFileSelectionMode(JFileChooser.FILES_ONLY);
      int result = fileChooser.showSaveDialog(this);
      if (result != JFileChooser.APPROVE_OPTION)
         return;
      File saveFile = fileChooser.getSelectedFile();
      if (!saveFile.getAbsolutePath().toLowerCase().endsWith(".png"))
         saveFile = newFile(saveFile.getAbsolutePath() + ".png");
      BufferedImage image = newBufferedImage(paintPanel.getSize().width, paintPanel.getSize().height,
            BufferedImage.TYPE_INT_RGB);
      for (int x = 0; x < image.getWidth(); x++) {
         for (int y = 0; y < image.getHeight(); y++) {
            image.setRGB(x, y, Color.white.getRGB());
            if (paintPanel.isPixel(newPoint(x, y))) {
               image.setRGB(x, y, Color.black.getRGB());
            }
         }
      }
      try {
         ImageIO.write(image, "png", saveFile);
      } catch (IOException e) {
         return;
      }
   }

   privatevoid doLoadImage() {
      JFileChooser fileChooser = newJFileChooser();
      fileChooser.setFileSelectionMode(JFileChooser.FILES_ONLY);
      int result = fileChooser.showOpenDialog(this);
      if (result != JFileChooser.APPROVE_OPTION)
         return;
      BufferedImage image;
      File openFile = fileChooser.getSelectedFile();
      try (FileInputStream fis = newFileInputStream(openFile)) {
         image = ImageIO.read(fis);
      } catch (IOException e) {
         return;
      }
      if (image == null)
         return;
      paintPanel.clear();
      Set<Point> blackPixels = newHashSet<Point>();
      for (int x = 0; x < image.getWidth(); x++) {
         for (int y = 0; y < image.getHeight(); y++) {
            Color c = newColor(image.getRGB(x, y));
            if ((c.getBlue() < 128 || c.getRed() < 128 || c.getGreen() < 128) && c.getAlpha() == 255) {
               blackPixels.add(newPoint(x, y));
            }
         }
      }
      paintPanel.addPixels(blackPixels);
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

- Java AWT Graphics paint mode
- Java AWT Graphics set font
- Java AWT Graphics set new drawing color
- Java AWT Graphics2D class
- Java AWT Graphics2D clear rectangle
