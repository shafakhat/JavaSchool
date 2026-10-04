---
title: Bevel Text
nav: Bevel Text
description: public class Java2sBevelText extends JComponent implements SwingConstants {
section: Imported - java2s Archive
order: 1021
source: https://web.archive.org/web/20081223094837/http://www.java2s.com:80/Code/Java/Swing-Components/BevelText.htm
---
```java title=Example.java
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Insets;
import java.awt.Rectangle;
import java.awt.RenderingHints;
import java.awt.font.FontRenderContext;
import java.awt.geom.Rectangle2D;
import javax.swing.JComponent;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.SwingConstants;
import javax.swing.UIManager;
import javax.swing.border.Border;
import javax.swing.plaf.ColorUIResource;
import javax.swing.plaf.FontUIResource;
public class Java2sBevelText extends JComponent implements SwingConstants {
  RenderingLabel leftShadeLabel = new RenderingLabel();
  RenderingLabel contentLabel = new RenderingLabel();
  RenderingLabel rightShadeLabel = new RenderingLabel();
  boolean raisedBevel= true;
  int depthX = 1;
  int depthY = 1;
  RenderingHints renderingHints;
  String text  = "Java2s";
  Color foregroundColor;
  Color defaultForeground = new Color(132, 132, 204);
  Font font = new FontUIResource(Font.decode("Dialog-Plain-28"));;
  public Java2sBevelText() {
    setLayout(null);
    add(contentLabel);
    add(leftShadeLabel);
    add(rightShadeLabel);
    reSize();
    setToolTipText(getToolTipText());
    setFont(font);
    setBackground(getBackground());
    setForeground(getForeground());
    setText(getText());
    setSize(getPreferredSize());
    setEnabled(isEnabled());
    setOpaque(isOpaque());
    setHorizontalAlignment(0);
    renderingHints = new RenderingHints(RenderingHints.KEY_TEXT_ANTIALIASING, RenderingHints.VALUE_TEXT_ANTIALIAS_ON);
    renderingHints.put(RenderingHints.KEY_FRACTIONALMETRICS, RenderingHints.VALUE_FRACTIONALMETRICS_ON);
  }
  public Java2sBevelText(String s) {
    this();
    setText(s);
    setSize(getPreferredSize());
  }
  public void setToolTipText(String s) {
    super.setToolTipText(s);
    leftShadeLabel.setToolTipText(s);
    contentLabel.setToolTipText(s);
    rightShadeLabel.setToolTipText(s);
  }
  public void updateUI() {
    super.updateUI();
    leftShadeLabel.updateUI();
    contentLabel.updateUI();
    rightShadeLabel.updateUI();
    setBackground(getBackground());
    setForeground(getForeground());
    setFont(font);
  }
  public void setRaisedBevel(boolean flag) {
    raisedBevel = flag;
    setForeground(getForeground());
  }
  public boolean isRaisedBevel() {
    return raisedBevel;
  }
  public void setDepthX(int depth) {
    depthX = depth;
    setSize(getSize());
  }
  public int getDepthX() {
    return depthX;
  }
  public void setDepthY(int depth) {
    depthY = depth;
    setSize(getSize());
  }
  public int getDepthY() {
    return depthY;
  }
  public Color getBackground() {
    return super.getBackground();
  }
  public void setBackground(Color newColor) {
    Color backgroundColor = newColor;
    if (backgroundColor == null || (backgroundColor instanceof ColorUIResource))
      backgroundColor = UIManager.getColor("control");
    super.setBackground(backgroundColor);
  }
  public Color getForeground() {
    return foregroundColor;
  }
  public void setForeground(Color newColor) {
    foregroundColor = newColor;
    if (foregroundColor == null || (foregroundColor instanceof ColorUIResource)) {
      foregroundColor = new ColorUIResource(defaultForeground);
      newColor = defaultForeground;
    }
    contentLabel.setForeground(newColor);
    if (raisedBevel) {
      leftShadeLabel.setForeground(Color.white);
      rightShadeLabel.setForeground(newColor.darker().darker().darker());
    } else {
      leftShadeLabel.setForeground(newColor.darker().darker().darker());
      rightShadeLabel.setForeground(Color.white);
    }
  }
  public Font getFont() {
    if (font == null || (font instanceof FontUIResource))
      font = new FontUIResource(Font.decode("Dialog-Plain-28"));
    return font;
  }
  public void setFont(Font newFont) {
    font = newFont;
    leftShadeLabel.setFont(font);
    contentLabel.setFont(font);
    rightShadeLabel.setFont(font);
  }
  public void setEnabled(boolean enabled) {
    super.setEnabled(enabled);
    leftShadeLabel.setEnabled(enabled);
    contentLabel.setEnabled(enabled);
    rightShadeLabel.setEnabled(enabled);
  }
  public void setOpaque(boolean flag) {
    super.setOpaque(flag);
    leftShadeLabel.setOpaque(false);
    contentLabel.setOpaque(false);
    rightShadeLabel.setOpaque(false);
    updateUI();
  }
  public void setVisible(boolean isVisible) {
    super.setVisible(isVisible);
    leftShadeLabel.setVisible(isVisible);
    contentLabel.setVisible(isVisible);
    rightShadeLabel.setVisible(isVisible);
  }
  public void setText(String s) {
    text = s;
    leftShadeLabel.setText(s);
    contentLabel.setText(s);
    rightShadeLabel.setText(s);
  }
  public String getText() {
    return text;
  }
  public Dimension getPreferredSize() {
    JLabel jlabel = new JLabel();
    jlabel.setFont(getFont());
    jlabel.setBorder(getBorder());
    if (renderingHints == null) {
      jlabel.setText(getText() + "m");
      Dimension dimension = jlabel.getPreferredSize();
      dimension.width += depthX * 2;
      dimension.height += depthY * 2;
      return dimension;
    } else {
      Dimension dimension1 = jlabel.getPreferredSize();
      dimension1.width += depthX * 2;
      dimension1.height += depthY * 2;
      boolean flag = true;
      boolean flag1 = true;
      FontRenderContext fontrendercontext = new FontRenderContext(null, flag, flag1);
      dimension1.width += getFont().getStringBounds(getText() + "m", fontrendercontext).getWidth();
      Rectangle2D rectangle2d = getFont().getMaxCharBounds(fontrendercontext);
      dimension1.height += rectangle2d.getHeight();
      return dimension1;
    }
  }
  public Dimension getMinimumSize() {
    return getPreferredSize();
  }
  public void setBorder(Border border) {
    super.setBorder(border);
    setSize(getSize());
  }
  private void reSize() {
    Insets insets = new Insets(0, 0, 0, 0);
    Border border = getBorder();
    if (border != null)
      insets = border.getBorderInsets(this);
    leftShadeLabel.setLocation(insets.top, insets.left);
    contentLabel.setLocation(insets.top + depthX, insets.left + depthY);
    rightShadeLabel.setLocation(insets.top + depthX * 2, insets.left + depthY * 2);
  }
  public void setBounds(int x, int y, int width, int height) {
    super.setBounds(x, y, width, height);
    reSize();
    Insets insets = new Insets(0, 0, 0, 0);
    Border border = getBorder();
    if (border != null)
      insets = border.getBorderInsets(this);
    int w = width - depthX * 2 - insets.left - insets.right;
    int h = height - depthY * 2 - insets.top - insets.bottom;
    leftShadeLabel.setSize(w, h);
    contentLabel.setSize(w, h);
    rightShadeLabel.setSize(w, h);
  }
  public void setBounds(Rectangle rectangle) {
    setBounds(rectangle.x, rectangle.y, rectangle.width, rectangle.height);
  }
  public void setSize(int w, int h) {
    super.setSize(w, h);
    reSize();
    Insets insets = new Insets(0, 0, 0, 0);
    Border border = getBorder();
    if (border != null)
      insets = border.getBorderInsets(this);
    int width = w - depthX * 2 - insets.left - insets.right;
    int height = h - depthY * 2 - insets.top - insets.bottom;
    leftShadeLabel.setSize(width, height);
    contentLabel.setSize(width, height);
    rightShadeLabel.setSize(width, height);
  }
  public void setSize(Dimension dimension) {
    setSize(dimension.width, dimension.height);
  }
  public final void paintInterface(Graphics g1) {
    if (isOpaque()) {
      g1.setColor(getBackground());
      g1.fillRect(0, 0, getWidth(), getHeight());
    }
    super.paint(g1);
  }
  public void setHorizontalAlignment(int i) {
    leftShadeLabel.setHorizontalAlignment(i);
    contentLabel.setHorizontalAlignment(i);
    rightShadeLabel.setHorizontalAlignment(i);
  }
  public int getHorizontalAlignment() {
    return leftShadeLabel.getHorizontalAlignment();
  }
  public void setVerticalAlignment(int i) {
    leftShadeLabel.setVerticalAlignment(i);
    contentLabel.setVerticalAlignment(i);
    rightShadeLabel.setVerticalAlignment(i);
  }
  public int getVerticalAlignment() {
    return leftShadeLabel.getVerticalAlignment();
  }
  private void setHorizontalTextPosition(int i) {
    leftShadeLabel.setHorizontalTextPosition(i);
    contentLabel.setHorizontalTextPosition(i);
    rightShadeLabel.setHorizontalTextPosition(i);
  }
  private int getHorizontalTextPosition() {
    return leftShadeLabel.getHorizontalTextPosition();
  }
  private void setVerticalTextPosition(int i) {
    if (rightShadeLabel != null) {
      leftShadeLabel.setVerticalTextPosition(i);
      contentLabel.setVerticalTextPosition(i);
      rightShadeLabel.setVerticalTextPosition(i);
    }
  }
  class RenderingLabel extends JLabel {
    public void paint(Graphics g1) {
      if (renderingHints != null && (g1 instanceof Graphics2D)) {
        Graphics2D graphics2d = (Graphics2D) g1;
        graphics2d.setRenderingHints(renderingHints);
      }
      super.paint(g1);
    }
  }
  private int getVerticalTextPosition() {
    return leftShadeLabel.getVerticalTextPosition();
  }
  public static void main(String[] args) {
    JFrame f = new JFrame();
    Java2sBevelText j = new Java2sBevelText();
    j.setForeground(Color.RED);
    f.getContentPane().add(j, "Center");
    f.setSize(400, 600);
    f.setVisible(true);
  }
}
```

1.  MultiLine Label
---  ---
2.  Label with large font and ANTIALIAS paint
3.  Label 3D
