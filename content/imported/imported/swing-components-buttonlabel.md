---
title: Button Label
nav: Button Label
description: setPreferredSize(new Dimension(metrics.stringWidth(getText()), height));
section: Imported - java2s Archive
order: 1027
source: https://web.archive.org/web/20111125080011/http://java2s.com/Code/Java/Swing-Components/ButtonLabel.htm
---
Button Label

```java title=Example.java
//package com.towel.swing;
import java.awt.Color;
import java.awt.Cursor;
import java.awt.Dimension;
import java.awt.FontMetrics;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import javax.swing.AbstractButton;
import javax.swing.UIManager;
public class ButtonLabel extends AbstractButton {
  private String text;
  private int height;
  public ButtonLabel(String text) {
    setText(text);
    addMouseListener(new MouseClick());
  }
  @Override
  public void paintComponent(Graphics g) {
    try {
      Graphics2D g2d = (Graphics2D) g.create();
      g2d.setFont(UIManager.getFont("TitledBorder.font"));
      g2d.setColor(getColor());
      g2d.drawString(text, 0, (height + 6) / 2);
      g2d.dispose();
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
  public String getText() {
    return text;
  }
  public void setText(String text) {
    this.text = text;
    updateSize();
  }
  private void updateSize() {
    FontMetrics metrics = getFontMetrics(UIManager
        .getFont("TitledBorder.font"));
    height = metrics.getHeight();
    setPreferredSize(new Dimension(metrics.stringWidth(getText()), height));
  }
  private class MouseClick extends MouseAdapter {
    @Override
    public void mouseClicked(MouseEvent evnt) {
      for (ActionListener listener : getActionListeners())
        listener.actionPerformed(new ActionEvent(ButtonLabel.this, 0,
            ""));
    }
    @Override
    public void mouseEntered(MouseEvent evnt) {
      if (getActionListeners().length == 0)
        return;
      setCursor(new Cursor(Cursor.HAND_CURSOR));
    }
    @Override
    public void mouseExited(MouseEvent evnt) {
      setCursor(new Cursor(Cursor.DEFAULT_CURSOR));
    }
  }
  private Color getColor() {
    return UIManager.getColor("TitledBorder.titleColor");
  }
}
```

1.  MultiLine Label
---  ---
2.  Multi Line Label extends JComponent
3.  Multi Line Label extends JPanel
4.  Link Label
5.  Vertical Label UI
6.  Label with large font and ANTIALIAS paint
7.  Label 3D
8.  URL Label
9.  Hyperlink Label
10.  Bevel Text
11.  A JLabel that can be underlined, implements Scrollable
12.  Gradient Label
13.  Hyperlink Label 2
14.  Computes a reasonable set of labels for a data interval and number of labels.
15.  Multi-label Label
16.  Shadow Label
