---
title: Controlling the print dialog box type
nav: Controlling the print dial...
description: final PrintRequestAttributeSet attributes = new HashPrintRequestAttributeSet();
section: Imported - java2s Archive
order: 1013
source: https://web.archive.org/web/20130820205858/http://java2s.com/Code/Java/JDK-7/Controllingtheprintdialogboxtype.htm
---
Controlling the print dialog box type

```java title=Example.java
import java.awt.Color;
import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.print.PrinterJob;
import javax.print.attribute.HashPrintRequestAttributeSet;
import javax.print.attribute.PrintRequestAttributeSet;
import javax.print.attribute.standard.DialogTypeSelection;
import javax.swing.JButton;
import javax.swing.JColorChooser;
import javax.swing.JFrame;
public class Test extends JFrame {
  public static void main(String[] args) {
    Test window = new Test();
    window.setVisible(true);
  }
  public Test() {
    this.setSize(200, 100);
    this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    this.setLayout(new FlowLayout());
    JColorChooser.showDialog(this, null, Color.blue);
    JButton printDialogButton = new JButton("Print Dialog");
    printDialogButton.addActionListener(new ActionListener() {
      public void actionPerformed(ActionEvent event) {
        final PrintRequestAttributeSet attributes = new HashPrintRequestAttributeSet();
        attributes.add(DialogTypeSelection.COMMON);
        PrinterJob printJob = PrinterJob.getPrinterJob();
        printJob.printDialog(attributes);
      }
    });
    this.add(printDialogButton);
  }
}
```
