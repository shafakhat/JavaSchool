---
title: Color TabbedPane Example
nav: Color TabbedPane Example
description: // Example from http://www.crionics.com/products/opensource/faq/swing_ex/SwingExamples.html
section: Imported - java2s Archive
order: 1038
source: https://web.archive.org/web/20060903005004/http://www.java2s.com:80/Code/Java/Swing-Components/ColorTabbedPaneExample.htm
---
Color TabbedPane Example

```java title=Example.java
// Example from http://www.crionics.com/products/opensource/faq/swing_ex/SwingExamples.html
/* (swing1.1.1) */
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Rectangle;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTabbedPane;
import javax.swing.UIManager;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;
import javax.swing.plaf.metal.MetalTabbedPaneUI;
/**
 * @version 1.0 08/23/99
 */
public class ColorTabbedPaneExample extends JFrame {
  String[] titles = { "blue", "cyan", "green", "yellow", "orange", "pink",
      "red" };
  Color[] colors = { Color.blue, Color.cyan, Color.green, Color.yellow,
      Color.orange, Color.pink, Color.red };
  JTabbedPane tabbedPane;
  public ColorTabbedPaneExample() {
    super("ColorTabbedPaneExample (Metal)");
    UIManager.put("TabbedPane.selected", colors[0]);
    tabbedPane = new JTabbedPane() {
      public void updateUI() {
        setUI(new ColoredTabbedPaneUI());
      }
    };
    for (int i = 0; i < titles.length; i++) {
      tabbedPane.addTab(titles[i], createPane(titles[i], colors[i]));
      tabbedPane.setBackgroundAt(i, colors[i].darker());
    }
    tabbedPane.setSelectedIndex(0);
    tabbedPane.addChangeListener(new ChangeListener() {
      public void stateChanged(ChangeEvent e) {
        int i = tabbedPane.getSelectedIndex();
        ((ColoredTabbedPaneUI) tabbedPane.getUI())
            .setSelectedTabBackground(colors[i]);
        tabbedPane.revalidate();
        tabbedPane.repaint();
      }
    });
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
  class ColoredTabbedPaneUI extends MetalTabbedPaneUI {
    public void setSelectedTabBackground(Color color) {
      selectColor = color;
    }
    protected void paintFocusIndicator(Graphics g, int tabPlacement,
        Rectangle[] rects, int tabIndex, Rectangle iconRect,
        Rectangle textRect, boolean isSelected) {
    }
  }
  public static void main(String[] args) {
    JFrame frame = new ColorTabbedPaneExample();
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
1. Swing Windows (Eclipse) like TabbedPanel
2. Mnemonic Tabbed Pane Example
3. Tab Color Example
4. Single Row Tabbed Pane Example 1
5. Single Row Tabbed Pane Example 2
6. Single Row Tabbed Pane Example 4
7. Color TabbedPane Example 2
8. Color TabbedPane Example 3
