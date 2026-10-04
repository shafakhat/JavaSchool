---
title: Another Line Break Demo
nav: Another Line Break Demo
description: attribString.addAttribute(TextAttribute.FOREGROUND, Color.blue, 0, text
section: Imported - java2s Archive
order: 1042
source: https://web.archive.org/web/20061018121110/http://www.java2s.com/Code/Java/2D-Graphics-GUI/AnotherLineBreakDemo.htm
---
Another Line Break Demo

```java title=Example.java
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.awt.font.FontRenderContext;
import java.awt.font.LineBreakMeasurer;
import java.awt.font.TextAttribute;
import java.awt.font.TextLayout;
import java.text.AttributedCharacterIterator;
import java.text.AttributedString;
import javax.swing.JFrame;
import javax.swing.JPanel;
public class LineBreakerPanel extends JPanel {
  String text = "This is a long string of Java 2D text "
      + "that can wrap futher to new rows when the "
      + "user reduces the width of this window!!! ";
  AttributedString attribString;
  AttributedCharacterIterator attribCharIterator;
  public LineBreakerPanel() {
    setBackground(Color.white);
    setSize(350, 400);
    attribString = new AttributedString(text);
    attribString.addAttribute(TextAttribute.FOREGROUND, Color.blue, 0, text
        .length()); // Start and end indexes.
    Font font = new Font("sanserif", Font.ITALIC, 20);
    attribString.addAttribute(TextAttribute.FONT, font, 0, text.length());
  }
  public void paintComponent(Graphics g) {
    super.paintComponent(g);
    Graphics2D g2 = (Graphics2D) g;
    attribCharIterator = attribString.getIterator();
    FontRenderContext frc = new FontRenderContext(null, false, false);
    LineBreakMeasurer lbm = new LineBreakMeasurer(attribCharIterator, frc);
    int x = 10, y = 20; // Left and top margins
    int w = getWidth(), h = getHeight(); // Window dimensions
    float wrappingWidth = w - 15;
    while (lbm.getPosition() < text.length()) {
      TextLayout layout = lbm.nextLayout(wrappingWidth);
      y += layout.getAscent();
      layout.draw(g2, x, y);
      y += layout.getDescent() + layout.getLeading();
    }
  }
  public static void main(String arg[]) {
    JFrame frame = new JFrame();
    frame.addWindowListener(new WindowAdapter() {
      public void windowClosing(WindowEvent e) {
        System.exit(0);
      }
    });
    frame.getContentPane().add("Center", new LineBreakerPanel());
    frame.pack();
    frame.setSize(new Dimension(350, 400));
    frame.setVisible(true);
  }
}
```

Related examples in the same category
---
2. Unicode: test layout
3. Unicode display
4. Line break for textlayout
5. Mouse hit and textlayout
6. TextLayout demo
7. Draw text along a curve
8. TextHitInfo Demo: tell you which is the letter you are clicking
9. TextAttribute: Underline and strike through
10. TextAttribute: color and font
11. Hightlight text by drag and selection
12. LineMetrics: the metrics to layout characters along a line
13. Paragraph Layout
14. Caret action
15. Caret and TextLayout
16. A display of text, formatted by us instead of by AWT/Swing
