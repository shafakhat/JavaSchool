---
title: A button which paints on it one or more scaled arrows in one of the cardinal directions
nav: A button which paints on i...
description: A button which paints on it one or more scaled arrows in one of the cardinal directions
section: Imported - java2s Archive
order: 1001
source: https://web.archive.org/web/20100211100011/http://java2s.com/Code/Java/Swing-Components/Abuttonwhichpaintsonitoneormorescaledarrowsinoneofthecardinaldirections.htm
---
```java title=Example.java
//Revised from greef ui;
import java.awt.BorderLayout;
import java.awt.Component;
import java.awt.Graphics;
import javax.swing.Icon;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTable;
import javax.swing.SwingConstants;
import javax.swing.table.DefaultTableCellRenderer;
import javax.swing.table.DefaultTableModel;
import javax.swing.table.TableColumnModel;
/**
 * @author Adrian BER
 */
public class ArrowIcon implements Icon {
    /** The cardinal direction of the arrow(s). */
    private int direction;
    /** The number of arrows. */
    private int arrowCount;
    /** The arrow size. */
    private int arrowSize;
    public ArrowIcon(int direction, int arrowCount, int arrowSize) {
        this.direction = direction;
        this.arrowCount = arrowCount;
        this.arrowSize = arrowSize;
    }
    /** Returns the cardinal direction of the arrow(s).
     * @see #setDirection(int)
     */
    public int getDirection() {
        return direction;
    }
    /** Sets the cardinal direction of the arrow(s).
     * @param direction the direction of the arrow(s), can be SwingConstants.NORTH,
     * SwingConstants.SOUTH, SwingConstants.WEST or SwingConstants.EAST
     * @see #getDirection()
     */
    public void setDirection(int direction) {
        this.direction = direction;
    }
    /** Returns the number of arrows. */
    public int getArrowCount() {
        return arrowCount;
    }
    /** Sets the number of arrows. */
    public void setArrowCount(int arrowCount) {
        this.arrowCount = arrowCount;
    }
    /** Returns the arrow size. */
    public int getArrowSize() {
        return arrowSize;
    }
    /** Sets the arrow size. */
    public void setArrowSize(int arrowSize) {
        this.arrowSize = arrowSize;
    }
    public void paintIcon(Component c, Graphics g, int x, int y) {
        // paint the arrows
        int w = getIconWidth();
        int h = getIconHeight();
        for (int i = 0; i < arrowCount; i++) {
            paintArrow(g,
                    (x + w - arrowSize * (direction == SwingConstants.EAST
                            || direction == SwingConstants.WEST ? arrowCount : 1)) / 2
                            + arrowSize * (direction == SwingConstants.EAST
                            || direction == SwingConstants.WEST ? i : 0),
                    (y + h - arrowSize * (direction == SwingConstants.EAST
                            || direction == SwingConstants.WEST ? 1 : arrowCount)) / 2
                            + arrowSize * (direction == SwingConstants.EAST
                            || direction == SwingConstants.WEST ? 0 : i)
                    );
        }
    }
    public int getIconWidth() {
        return arrowSize * (direction == SwingConstants.EAST
                || direction == SwingConstants.WEST ? arrowCount : 3);
    }
    public int getIconHeight() {
        return arrowSize * (direction == SwingConstants.NORTH
                || direction == SwingConstants.SOUTH ? arrowCount : 3);
    }
    private void paintArrow(Graphics g, int x, int y) {
        int mid, i, j;
        j = 0;
        arrowSize = Math.max(arrowSize, 2);
        mid = (arrowSize / 2) - 1;
        g.translate(x, y);
        switch (direction) {
            case SwingConstants.NORTH:
                for (i = 0; i < arrowSize; i++) {
                    g.drawLine(mid - i, i, mid + i, i);
                }
                break;
            case SwingConstants.SOUTH:
                j = 0;
                for (i = arrowSize - 1; i >= 0; i--) {
                    g.drawLine(mid - i, j, mid + i, j);
                    j++;
                }
                break;
            case SwingConstants.WEST:
                for (i = 0; i < arrowSize; i++) {
                    g.drawLine(i, mid - i, i, mid + i);
                }
                break;
            case SwingConstants.EAST:
                j = 0;
                for (i = arrowSize - 1; i >= 0; i--) {
                    g.drawLine(j, mid - i, j, mid + i);
                    j++;
                }
                break;
        }
        g.translate(-x, -y);
    }
}
```

1.  Arrow Button
