---
title: A filter that translates to gray. Each of the red, green, and blue levels becomes the mean intensity.
nav: A filter that translates t...
description: A filter that translates to gray. Each of the red, green, and blue levels becomes the mean intensity.
section: Imported - java2s Archive
order: 1017
source: https://web.archive.org/web/20090210132123/http://www.java2s.com:80/Code/Java/2D-Graphics-GUI/AfilterthattranslatestograyEachoftheredgreenandbluelevelsbecomesthemeanintensity.htm
---
```java title=Example.java
import java.applet.Applet;
import java.awt.Button;
import java.awt.Graphics;
import java.awt.Image;
import java.awt.MediaTracker;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.image.FilteredImageSource;
import java.awt.image.ImageProducer;
import java.awt.image.RGBImageFilter;
public class MainClass extends Applet implements ActionListener {
  private Image originalImage, filteredImage;
  private Button btn = new Button("FILTER");
  private GrayFilter cropFilter = new GrayFilter();
  public void init() {
    originalImage = getImage(getDocumentBase(), "emily.gif");
    MediaTracker tracker = new MediaTracker(this);
    tracker.addImage(originalImage, 0);
    try {
      tracker.waitForAll();
    } catch (Exception e) {
    }
    filteredImage = originalImage;
    btn.addActionListener(this);
    add(btn);
  }
  public void actionPerformed(ActionEvent ev) {
    filter();
    repaint();
  }
  private void filter() {
    ImageProducer producer = originalImage.getSource();
    producer = new FilteredImageSource(producer, cropFilter);
    filteredImage = createImage(producer);
  }
  public void paint(Graphics g) {
    g.drawImage(originalImage, 10, 50, this);
    g.drawImage(filteredImage, 271, 50, this);
  }
}
class GrayFilter extends RGBImageFilter {
  int nCalls;
  public GrayFilter() {
    canFilterIndexColorModel = true;
  }
  public void setFast(boolean fast) {
    canFilterIndexColorModel = fast;
  }
  public int filterRGB(int x, int y, int rgb) {
    int red = (rgb & 0x00ff0000) >> 16;
    int green = (rgb & 0x0000ff00) >> 8;
    int blue = (rgb & 0x000000ff);
    int mean = (red + green + blue) / 3;
    return 0xff000000 | mean << 16 | mean << 8 | mean;
  }
}
```

1.  A filter class which translates moderately white pixels to green.
