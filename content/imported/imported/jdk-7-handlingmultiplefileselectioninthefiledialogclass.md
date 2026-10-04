---
title: Handling multiple file selection in the FileDialog class
nav: Handling multiple file sel...
description: final FileDialog fileDialog = new FileDialog(this, "FileDialog");
section: Imported - java2s Archive
order: 1080
source: https://web.archive.org/web/20130223095414/http://www.java2s.com:80/Code/Java/JDK-7/HandlingmultiplefileselectionintheFileDialogclass.htm
---
```java title=Example.java
import java.awt.FileDialog;
import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import javax.swing.JButton;
import javax.swing.JFrame;
public class Test extends JFrame {
  public static void main(String[] args) {
    Test window = new Test();
    window.setVisible(true);
  }
  public Test() {
    this.setSize(200, 100);
    this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    final FileDialog fileDialog = new FileDialog(this, "FileDialog");
    fileDialog.setMultipleMode(true);
    JButton fileDialogButton = new JButton("File Dialog");
    fileDialogButton.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent event) {
        fileDialog.setVisible(true);
        File files[] = fileDialog.getFiles();
        for (File file : files) {
          System.out.println("File: " + file.getName());
        }
      }
    });
    this.add(fileDialogButton);
  }
}
```

1.  Creating a varying gradient translucent window
---  ---
2.  Managing the Opacity of a Window
3.  Managing the Shape of a Window
4.  Managing Window types
5.  Mixing heavyweight and lightweight components
6.  New border types in Java 7:RaisedSoftBevelBorder
7.  New border types in Java 7:LineBorder width
8.  New border types in Java 7:LoweredSoftBevelBorder
9.  BorderFactory.createSoftBevelBorder(BevelBorder.LOWERED)
10.  BorderFactory.createSoftBevelBorder(BevelBorder.LOWERED, Color.lightGray, Color.yellow)
11.  Using the new JLayer Decorator for a password field
12.  Managing extra mouse buttons and high resolution mouse wheels
13.  Using the NumericShaper.Range enumeration to support the display of digits
