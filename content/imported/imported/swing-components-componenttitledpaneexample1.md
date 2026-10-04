---
title: Component TitledPane Example 1
nav: Component TitledPane Examp...
description: Component TitledPane Example 1 : Java examples (example source code) » Swing Components » Border
section: Imported - java2s Archive
order: 1049
source: https://web.archive.org/web/20060513085112/http://www.java2s.com/Code/Java/Swing-Components/ComponentTitledPaneExample1.htm
---
Component TitledPane Example 1 : Java examples (example source code) » Swing Components » Border

Component TitledPane Example 1

```java title=Example.java
// Example from http://www.crionics.com/products/opensource/faq/swing_ex/SwingExamples.html
import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Component;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.GridLayout;
import java.awt.Insets;
import java.awt.Rectangle;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import javax.swing.ButtonGroup;
import javax.swing.JComponent;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JRadioButton;
import javax.swing.UIManager;
import javax.swing.border.Border;
import javax.swing.border.TitledBorder;
/**
 * @version 1.0 08/12/99
 */
public class CompTitledPaneExample1 extends JFrame {
  String title = "<html>Title ("
      + "<font color=\"#ffffff\"><i>JLabel</i></font>" + ")";
  public CompTitledPaneExample1() {
    super("CompTitledPaneExample1");
    JLabel titleLabel = new JLabel(title);
    CompTitledPane p1 = new CompTitledPane(titleLabel);
    JPanel p = p1.getContentPane();
    p.setLayout(new BorderLayout());
    p.add(new SwitchPanel(p1), BorderLayout.CENTER);
    getContentPane().add(p1, BorderLayout.CENTER);
  }
  class SwitchPanel extends JPanel implements ActionListener {
    String[] posStr = { "", "ABOVE_TOP", "TOP", "BELOW_TOP",
        "ABOVE_BOTTOM", "BOTTOM", "BELOW_BOTTOM" };
    String[] jusStr = { "", "LEFT", "CENTER", "RIGHT" };
    TitledBorder border;
    CompTitledPane panel;
    SwitchPanel(CompTitledPane panel) {
      this.panel = panel;
      this.border = (TitledBorder) panel.getBorder();
      add(createPanel("Position", posStr, 2));
      add(createPanel("Justification", jusStr, 1));
    }
    JPanel createPanel(String str, String[] strs, int selectPos) {
      JPanel p = new JPanel();
      p.setLayout(new GridLayout(strs.length, 1));
      p.add(new JLabel(str));
      ButtonGroup g = new ButtonGroup();
      for (int i = 1; i < strs.length; i++) {
        JRadioButton b = new JRadioButton(strs[i]);
        if (i == selectPos) {
          b.setSelected(true);
        }
        p.add(b);
        g.add(b);
        b.addActionListener(this);
      }
      return p;
    }
    public void actionPerformed(ActionEvent e) {
      JRadioButton b = (JRadioButton) e.getSource();
      String label = b.getText();
      for (int i = 1; i < posStr.length; i++) {
        if (label.equals(posStr[i])) {
          border.setTitlePosition(i);
          panel.revalidate();
          panel.repaint();
          return;
        }
      }
      for (int i = 1; i < jusStr.length; i++) {
        if (label.equals(jusStr[i])) {
          border.setTitleJustification(i);
          panel.revalidate();
          panel.repaint();
          return;
        }
      }
    }
  }
  public static void main(String args[]) {
    try {
        UIManager.setLookAndFeel("com.sun.java.swing.plaf.windows.WindowsLookAndFeel");
    } catch (Exception evt) {}
    CompTitledPaneExample1 frame = new CompTitledPaneExample1();
    frame.addWindowListener(new WindowAdapter() {
      public void windowClosing(WindowEvent e) {
        System.exit(0);
      }
    });
    frame.setSize(280, 230);
    frame.setVisible(true);
  }
}
/**
 * @version 1.0 08/12/99
 */
class CompTitledPane extends JPanel {
  protected CompTitledBorder border;
  protected JComponent component;
  protected JPanel panel;
  protected boolean transmittingAllowed;
  protected StateTransmitter transmitter;
  public CompTitledPane() {
    this(new JLabel("Title"));
    // debug
    // JLabel label = (JLabel)getTitleComponent();
    // label.setOpaque(true);
    // label.setBackground(Color.yellow);
  }
  public CompTitledPane(JComponent component) {
    this.component = component;
    border = new CompTitledBorder(component);
    setBorder(border);
    panel = new JPanel();
    setLayout(null);
    add(component);
    add(panel);
    transmittingAllowed = false;
    transmitter = null;
  }
  public JComponent getTitleComponent() {
    return component;
  }
  public void setTitleComponent(JComponent newComponent) {
    remove(component);
    add(newComponent);
    border.setTitleComponent(newComponent);
    component = newComponent;
  }
  public JPanel getContentPane() {
    return panel;
  }
  public void doLayout() {
    Insets insets = getInsets();
    Rectangle rect = getBounds();
    rect.x = 0;
    rect.y = 0;
    Rectangle compR = border.getComponentRect(rect, insets);
    component.setBounds(compR);
    rect.x += insets.left;
    rect.y += insets.top;
    rect.width -= insets.left + insets.right;
    rect.height -= insets.top + insets.bottom;
    panel.setBounds(rect);
  }
  public void setTransmittingAllowed(boolean enable) {
    transmittingAllowed = enable;
  }
  public boolean getTransmittingAllowed() {
    return transmittingAllowed;
  }
  public void setTransmitter(StateTransmitter transmitter) {
    this.transmitter = transmitter;
  }
  public StateTransmitter getTransmitter() {
    return transmitter;
  }
  public void setEnabled(boolean enable) {
    super.setEnabled(enable);
    if (transmittingAllowed && transmitter != null) {
      transmitter.setChildrenEnabled(enable);
    }
  }
}
interface StateTransmitter {
  public void setChildrenEnabled(boolean enable);
}
class CompTitledBorder extends TitledBorder {
  protected JComponent component;
  public CompTitledBorder(JComponent component) {
    this(null, component, LEFT, TOP);
  }
  public CompTitledBorder(Border border) {
    this(border, null, LEFT, TOP);
  }
  public CompTitledBorder(Border border, JComponent component) {
    this(border, component, LEFT, TOP);
  }
  public CompTitledBorder(Border border, JComponent component,
      int titleJustification, int titlePosition) {
    super(border, null, titleJustification, titlePosition, null, null);
    this.component = component;
    if (border == null) {
      this.border = super.getBorder();
    }
  }
  public void paintBorder(Component c, Graphics g, int x, int y, int width,
      int height) {
    Rectangle borderR = new Rectangle(x + EDGE_SPACING, y + EDGE_SPACING,
        width - (EDGE_SPACING * 2), height - (EDGE_SPACING * 2));
    Insets borderInsets;
    if (border != null) {
      borderInsets = border.getBorderInsets(c);
    } else {
      borderInsets = new Insets(0, 0, 0, 0);
    }
    Rectangle rect = new Rectangle(x, y, width, height);
    Insets insets = getBorderInsets(c);
    Rectangle compR = getComponentRect(rect, insets);
    int diff;
    switch (titlePosition) {
    case ABOVE_TOP:
      diff = compR.height + TEXT_SPACING;
      borderR.y += diff;
      borderR.height -= diff;
      break;
    case TOP:
    case DEFAULT_POSITION:  diff = insets.top / 2 - borderInsets.top - EDGE_SPACING;
      borderR.y += diff;
      borderR.height -= diff;
      break;
    case BELOW_TOP:
    case ABOVE_BOTTOM:
      break;
    case BOTTOM:
      diff = insets.bottom / 2 - borderInsets.bottom - EDGE_SPACING;
      borderR.height -= diff;
      break;
    case BELOW_BOTTOM:
      diff = compR.height + TEXT_SPACING;
      borderR.height -= diff;
      break;
    }
    border.paintBorder(c, g, borderR.x, borderR.y, borderR.width,
        borderR.height);
    Color col = g.getColor();
    g.setColor(c.getBackground());
    g.fillRect(compR.x, compR.y, compR.width, compR.height);
    g.setColor(col);
    component.repaint();
  }
  public Insets getBorderInsets(Component c, Insets insets) {
    Insets borderInsets;
    if (border != null) {
      borderInsets = border.getBorderInsets(c);
    } else {
      borderInsets = new Insets(0, 0, 0, 0);
    }
    insets.top = EDGE_SPACING + TEXT_SPACING + borderInsets.top;
    insets.right = EDGE_SPACING + TEXT_SPACING + borderInsets.right;
    insets.bottom = EDGE_SPACING + TEXT_SPACING + borderInsets.bottom;
    insets.left = EDGE_SPACING + TEXT_SPACING + borderInsets.left;
    if (c == null || component == null) {
      return insets;
    }
    int compHeight = 0;
    if (component != null) {
      compHeight = component.getPreferredSize().height;
    }
    switch (titlePosition) {
    case ABOVE_TOP:
      insets.top += compHeight + TEXT_SPACING;
      break;
    case TOP:
    case DEFAULT_POSITION:
      insets.top += Math.max(compHeight, borderInsets.top)
          - borderInsets.top;
      break;
    case BELOW_TOP:
      insets.top += compHeight + TEXT_SPACING;
      break;
    case ABOVE_BOTTOM:
      insets.bottom += compHeight + TEXT_SPACING;
      break;
    case BOTTOM:
      insets.bottom += Math.max(compHeight, borderInsets.bottom)
          - borderInsets.bottom;
      break;
    case BELOW_BOTTOM:
      insets.bottom += compHeight + TEXT_SPACING;
      break;
    }
    return insets;
  }
  public JComponent getTitleComponent() {
    return component;
  }
  public void setTitleComponent(JComponent component) {
    this.component = component;
  }
  public Rectangle getComponentRect(Rectangle rect, Insets borderInsets) {
    Dimension compD = component.getPreferredSize();
    Rectangle compR = new Rectangle(0, 0, compD.width, compD.height);
    switch (titlePosition) {
    case ABOVE_TOP:
      compR.y = EDGE_SPACING;
      break;
    case TOP:
    case DEFAULT_POSITION:
      compR.y = EDGE_SPACING
          + (borderInsets.top - EDGE_SPACING - TEXT_SPACING - compD.height)
          / 2;
      break;
    case BELOW_TOP:
      compR.y = borderInsets.top - compD.height - TEXT_SPACING;
      break;
    case ABOVE_BOTTOM:
      compR.y = rect.height - borderInsets.bottom + TEXT_SPACING;
      break;
    case BOTTOM:
      compR.y = rect.height
          - borderInsets.bottom
          + TEXT_SPACING
          + (borderInsets.bottom - EDGE_SPACING - TEXT_SPACING - compD.height)
          / 2;
      break;
    case BELOW_BOTTOM:
      compR.y = rect.height - compD.height - EDGE_SPACING;
      break;
    }
    switch (titleJustification) {
    case LEFT:
    case DEFAULT_JUSTIFICATION:
      compR.x = TEXT_INSET_H + borderInsets.left;
      break;
    case RIGHT:
      compR.x = rect.width - borderInsets.right - TEXT_INSET_H
          - compR.width;
      break;
    case CENTER:
      compR.x = (rect.width - compR.width) / 2;
      break;
    }
    return compR;
  }
}
```

Related examples in the same category
---
1. Add decorators to swing component
2. DropDown Shadow Border
3. Shadows for Button
4. Shadows for Image
5. Shadows for Panel
6. Shadows for Label
7. Swing transparent component
8. Shadows for TextField
9. Shadows for ComboBox
10. Shadows for TextArea
11. Shadows for List
12. Component TitledPane Example 2
13. Component TitledPane Example 3
