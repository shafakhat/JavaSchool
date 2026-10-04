---
title: Another print demo
nav: Another print demo
description: Another print demo : Java examples (example source code) » 2D Graphics GUI » Print
section: Imported - java2s Archive
order: 1043
source: https://web.archive.org/web/20060513094501/http://www.java2s.com/Code/Java/2D-Graphics-GUI/Anotherprintdemo.htm
---
Another print demo : Java examples (example source code) » 2D Graphics GUI » Print

```java title=Example.java
import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Container;
import java.awt.Font;
import java.awt.FontMetrics;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.awt.print.PageFormat;
import java.awt.print.Printable;
import java.awt.print.PrinterException;
import java.awt.print.PrinterJob;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
public class AnotherPrintDemo extends JFrame {
  DrawingCanvas canvas;
  JButton setUpButton = new JButton("Page Setup");
  JButton printButton = new JButton("Print");
  JButton cancelButton = new JButton("Cancel");
  public AnotherPrintDemo() {
    super();
    Container container = getContentPane();
    canvas = new DrawingCanvas();
    container.add(canvas);
    JPanel panel = new JPanel(new GridLayout(1, 3));
    ButtonListener buttonListener = new ButtonListener();
    setUpButton.addActionListener(buttonListener);
    panel.add(setUpButton);
    printButton.addActionListener(buttonListener);
    panel.add(printButton);
    cancelButton.addActionListener(buttonListener);
    panel.add(cancelButton);
    container.add(BorderLayout.SOUTH, panel);
    addWindowListener(new WindowAdapter() {
      public void windowClosing(WindowEvent e) {
        System.exit(0);
      }
    });
    setSize(650, 275);
    setVisible(true);
  }
  class ButtonListener implements ActionListener {
    PrinterJob printJob;
    PageFormat pageFormat;
    PrintableCanvas printableCanvas;
    ButtonListener() {
      printJob = PrinterJob.getPrinterJob();
      pageFormat = printJob.defaultPage();
    }
    public void actionPerformed(ActionEvent e) {
      JButton tempButton = (JButton) e.getSource();
      if (tempButton.equals(setUpButton)) {
        pageFormat = printJob.pageDialog(pageFormat);
        printJob.validatePage(pageFormat);
      } else if (tempButton.equals(printButton)) {
        printableCanvas = new PrintableCanvas(pageFormat);
        printJob.setPrintable(printableCanvas);
        boolean ok = printJob.printDialog();
        if (ok) {
          try {
            printJob.print();
          } catch (Exception pe) {
            System.out.println("Printing Exception Occured!");
            pe.printStackTrace();
          }
        }
      } else if (tempButton.equals(cancelButton)) {
        printJob.cancel();
      }
    }
  }
  public static void main(String arg[]) {
    new AnotherPrintDemo();
  }
}
class DrawingCanvas extends JPanel {
  Font font;
  FontMetrics fontMetrics;
  int w, h;
  DrawingCanvas() {
    setBackground(Color.white);
    setSize(400, 275);
    w = this.getWidth();
    h = this.getHeight();
    font = new Font("Dialog", Font.BOLD, 50);
    fontMetrics = getFontMetrics(font);
  }
  public void paintComponent(Graphics g) {
    super.paintComponent(g);
    Graphics2D g2D = (Graphics2D) g;
    paintContent(g2D, w, h);
  }
  public void paintContent(Graphics2D g2D, int w, int h) {
    g2D.setFont(font);
        (float) (0.5 * h - 1.25 * fontMetrics.getHeight()));
  }
}
class PrintableCanvas implements Printable {
  DrawingCanvas canvas;
  PageFormat pageFormat;
  public PrintableCanvas(PageFormat pf) {
    pageFormat = pf;
  }
  public int print(Graphics g, PageFormat pageFormat, int pageIndex)
      throws PrinterException {
    if (pageIndex >= 1) {
      return Printable.NO_SUCH_PAGE;
    }
    Graphics2D g2D = (Graphics2D) g;
    canvas = new DrawingCanvas();
    canvas.paintContent(g2D, (int) pageFormat.getImageableWidth(),
        (int) pageFormat.getImageableHeight());
    // successful printing of the page
    return Printable.PAGE_EXISTS;
  }
}
```

Related examples in the same category
---
1. Simplest SWT Print Example
2. Print in Java 2: PrinterJob
3. Print in Java: page format and document
4. Print in Java: Multi page
5. Print in Java 5
6. Print in Java 6
7. Simple Book for printing
8. Shapes Print
9. Display the print dialog and print
10. Print the printable area outline
11. Print the text file and print preview them
12. Printable demo
13. Print Swing components
14. Book
15. Book demo
16. Printing the Combined-Java 1.2-and-1.4 Way
17. Printing the Java 1.4 Way
18. Prompting for a Printer
19. Printing the Java 1.1 Way
20. Scribble
21. Printable Document
22. PrintFile -- Print a file named on the command line
23. Print to the standard output
24. PrintPanel is the base for an open-ended series of classes
25. Print Demo: Book
26. Print Test
27. Pageable Text
28. Printable Component
