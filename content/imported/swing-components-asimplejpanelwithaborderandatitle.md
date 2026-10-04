---
title: A simple JPanel with a border and a title
nav: A simple JPanel with a bor...
description: * This program is free software; you can redistribute it and/or
section: Imported - java2s Archive
order: 1016
source: https://web.archive.org/web/20111125025810/http://java2s.com/Code/Java/Swing-Components/AsimpleJPanelwithaborderandatitle.htm
---
A simple JPanel with a border and a title

```java title=Example.java
/*
 *  Copyright (C) 2004 Kai Toedter
 *  kai@toedter.com
 *  www.toedter.com
 *
 *  This program is free software; you can redistribute it and/or
 *  modify it under the terms of the GNU Lesser General Public License
 *  as published by the Free Software Foundation; either version 2
 *  of the License, or (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU Lesser General Public License for more details.
 *
 *  You should have received a copy of the GNU Lesser General Public License
 *  along with this program; if not, write to the Free Software
 *  Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
 */
//package com.toedter.components;
import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.GradientPaint;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Paint;
import javax.swing.BorderFactory;
import javax.swing.Icon;
import javax.swing.JComponent;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.border.Border;
/**
 * A simple JPanel with a border and a title
 *
 * @author Kai Toedter
 * @version $LastChangedRevision: 85 $
 * @version $LastChangedDate: 2006-04-28 13:50:52 +0200 (Fr, 28 Apr 2006) $
 */
public class JTitlePanel extends JPanel {
  private static final long serialVersionUID = 9104873267039717087L;
  protected JPanel northPanel;
    protected JLabel label;
    /**
     * Constructs a titled panel.
     *
     * @param title the title
     * @param content the JComponent that contains the content
     * @param outerBorder the outer border
     */
    public JTitlePanel(String title, Icon icon, JComponent content, Border outerBorder) {
        setLayout(new BorderLayout());
        label = new JLabel(title, icon, JLabel.LEADING);
        label.setForeground(Color.WHITE);
        GradientPanel titlePanel = new GradientPanel(Color.BLACK);
        titlePanel.setLayout(new BorderLayout());
        titlePanel.add(label, BorderLayout.WEST);
        int borderOffset = 2;
        if(icon == null) {
          borderOffset += 1;
        }
        titlePanel.setBorder(BorderFactory.createEmptyBorder(borderOffset, 4, borderOffset, 1));
        add(titlePanel, BorderLayout.NORTH);
        JPanel northPanel = new JPanel();
        northPanel.setLayout(new BorderLayout());
        northPanel.add(content,BorderLayout.NORTH);
        northPanel.setBorder(BorderFactory.createEmptyBorder(4, 4, 4, 4));
        add(northPanel, BorderLayout.CENTER);
        if (outerBorder == null) {
            setBorder(BorderFactory.createLineBorder(Color.GRAY));
        } else {
            setBorder(BorderFactory.createCompoundBorder(outerBorder,
                    BorderFactory.createLineBorder(Color.GRAY)));
        }
    }
    public void setTitle(String label, Icon icon) {
      this.label.setText(label);
      this.label.setIcon(icon);
    }
    private static class GradientPanel extends JPanel {
    private static final long serialVersionUID = -6385751027379193053L;
    private GradientPanel(Color background) {
            setBackground(background);
        }
        public void paintComponent(Graphics g) {
            super.paintComponent(g);
            if (isOpaque()) {
                // Color controlColor = UIManager.getColor("control");
                // Color controlColor = new Color(252, 198, 82);
                Color controlColor = new Color(99, 153, 255);
                int width = getWidth();
                int height = getHeight();
                Graphics2D g2 = (Graphics2D) g;
                Paint oldPaint = g2.getPaint();
                g2.setPaint(new GradientPaint(0, 0, getBackground(), width, 0,
                        controlColor));
                g2.fillRect(0, 0, width, height);
                g2.setPaint(oldPaint);
            }
        }
    }
}
```

1.  Yes / No Panel
---  ---
5.  Gradient Panel
6.  Transfer focus from button to button with help of arrows keys.
7.  A JPanel with a textured background.
8.  Time panel shows the current time.
9.  Graph Canvas
10.  A basic panel that displays a small up or down arrow.
11.  HeatMap is a JPanel that displays a 2-dimensional array of data using a selected color gradient scheme.
12.  GradientPanel is a class with a gradient background.
13.  Translucent Panel
14.  Image Panel
15.  The class makes it easy to select a numerical value, possibly from a given range
