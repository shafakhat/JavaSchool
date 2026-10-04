---
title: A program for viewing images
nav: A program for viewing images
description: This program is a part of the companion code for Core Java 8th ed.
section: Imported - java2s Archive
order: 1046
source: https://web.archive.org/web/20101018030853/http://www.java2s.com:80/Code/Java/2D-Graphics-GUI/Aprogramforviewingimages.htm
---
```java title=Example.java
/*
 This program is a part of the companion code for Core Java 8th ed.
 (http://horstmann.com/corejava)
 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.
 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.
 You should have received a copy of the GNU General Public License
 along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
import java.awt.EventQueue;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import javax.swing.ImageIcon;
import javax.swing.JFileChooser;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
/**
 *
 * @version 1.22 2007-05-21
 * @author Cay Horstmann
 */
public class ImageViewer {
  public static void main(String[] args) {
    EventQueue.invokeLater(new Runnable() {
      public void run() {
        JFrame frame = new ImageViewerFrame();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
      }
    });
  }
}
/**
 * A frame with a label to show an image.
 */
class ImageViewerFrame extends JFrame {
  public ImageViewerFrame() {
    setTitle("ImageViewer");
    setSize(DEFAULT_WIDTH, DEFAULT_HEIGHT);
    // use a label to display the images
    label = new JLabel();
    add(label);
    // set up the file chooser
    chooser = new JFileChooser();
    chooser.setCurrentDirectory(new File("."));
    // set up the menu bar
    JMenuBar menuBar = new JMenuBar();
    setJMenuBar(menuBar);
    JMenu menu = new JMenu("File");
    menuBar.add(menu);
    JMenuItem openItem = new JMenuItem("Open");
    menu.add(openItem);
    openItem.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent event) {
        // show file chooser dialog
        int result = chooser.showOpenDialog(null);
        // if file selected, set it as icon of the label
        if (result == JFileChooser.APPROVE_OPTION) {
          String name = chooser.getSelectedFile().getPath();
          label.setIcon(new ImageIcon(name));
        }
      }
    });
    JMenuItem exitItem = new JMenuItem("Exit");
    menu.add(exitItem);
    exitItem.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent event) {
        System.exit(0);
      }
    });
  }
  private JLabel label;
  private JFileChooser chooser;
  private static final int DEFAULT_WIDTH = 300;
  private static final int DEFAULT_HEIGHT = 400;
}
```

1.  Display image supported by ImageIO
---  ---
2.  Print an Image to print directly
3.  List All reader and writer formats supported by ImageIO
4.  Display available ImageReaders and ImageWriters by image format and MIME type
5.  Write an image of a given format
6.  Read an image
7.  Simple, functional ImageReaderSpi used to understand how information
8.  Simple, functional ImageWriterSpi used to understand how information
9.  Example showing how to reset the ordering of ImageReaderSpis in Image I/O
10.  Using mediatracker to pre-load images
11.  Get list of unique supported read formats
12.  Get list of unique supported write formats
13.  Get list of unique MIME types that can be read
14.  Get list of unique MIME types that can be written
15.  Returns true if the specified format name can be read
16.  Returns true if the specified format name can be written
17.  Returns true if the specified file extension can be read
18.  Returns true if the specified file extension can be written
19.  Returns true if the specified mime type can be read
20.  Returns true if the specified mime type can be written
21.  Show ImageIO Info
22.  Write Image with different types
23.  Load the image file from a folder or a jar file: use javax.imageio.ImageIO class to read the image file
24.  Compress and save an image to the disk
25.  Creates a new raster copy
26.  Resizes an image
27.  Creates an image compatible with the current display
28.  Produces a copy of the supplied image
29.  Produces a resized image that is of the given dimensions
30.  Loads an image in a format compatible with the current display
31.  Thumbnail Generator
32.  Saves an image to the disk
33.  Helper class for debugging stuff in Image I/O.
34.  Reading a gif image with ImageIO.read and display it on screen
35.  Read and write image files in the formats that the JDK supports. Multi-file images are supported.
