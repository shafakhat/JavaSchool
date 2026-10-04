---
title: Color TabbedPane Example 2
nav: Color TabbedPane Example 2
description: // Example from http://www.crionics.com/products/opensource/faq/swing_ex/SwingExamples.html
section: Imported - java2s Archive
order: 1039
source: https://web.archive.org/web/20061018145422/http://www.java2s.com/Code/Java/Swing-Components/ColorTabbedPaneExample2.htm
---
Color TabbedPane Example 2

```java title=Example.java
// Example from http://www.crionics.com/products/opensource/faq/swing_ex/SwingExamples.html
/* (swing1.1.1) */
import java.awt.Color;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTabbedPane;
import javax.swing.UIManager;
import javax.swing.plaf.basic.BasicTabbedPaneUI;
/**
 * @version 1.0 08/23/99
 */
public class ColorTabbedPaneExample2 extends JFrame {
  String[] titles = { "blue", "cyan", "green", "yellow", "orange", "pink",
      "red" };
  Color[] colors = { Color.blue, Color.cyan, Color.green, Color.yellow,
      Color.orange, Color.pink, Color.red };
  JTabbedPane tabbedPane;
  public ColorTabbedPaneExample2() {
    super("ColorTabbedPaneExample (basic)");
    tabbedPane = new ColoredTabbedPane();
    for (int i = 0; i < titles.length; i++) {
      tabbedPane.addTab(titles[i], createPane(titles[i], colors[i]));
      tabbedPane.setBackgroundAt(i, colors[i].darker());
    }
    tabbedPane.setSelectedIndex(0);
    getContentPane().add(tabbedPane);
  }
  JPanel createPane(String title, Color color) {
    JPanel panel = new JPanel();
    panel.setBackground(color);
    JLabel label = new JLabel(title);
    label.setOpaque(true);
    label.setBackground(Color.white);
    panel.add(label);
    return panel;
  }
  class ColoredTabbedPane extends JTabbedPane {
    public Color getBackgroundAt(int index) {
      if (index == getSelectedIndex()) {
        return colors[index];
      } else {
        return super.getBackgroundAt(index);
      }
    }
    public void updateUI() {
      setUI(new BasicTabbedPaneUI());
    }
  }
  public static void main(String[] args) {
    JFrame frame = new ColorTabbedPaneExample2();
    frame.addWindowListener(new WindowAdapter() {
      public void windowClosing(WindowEvent e) {
        System.exit(0);
      }
    });
    frame.setSize(360, 100);
    frame.setVisible(true);
  }
}
```

Related examples in the same category
---
2. Mnemonic Tabbed Pane Example
3. Tab Color Example
4. Single Row Tabbed Pane Example 1
5. Single Row Tabbed Pane Example 2
6. Single Row Tabbed Pane Example 4
7. Color TabbedPane Example
8. Color TabbedPane Example 3
