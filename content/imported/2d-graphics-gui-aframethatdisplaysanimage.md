---
title: A frame that displays an image
nav: A frame that displays an i...
description: * A frame that displays an image. Create an ImageFrame, then use one
section: Imported - java2s Archive
order: 1018
source: https://web.archive.org/web/20091206070315/http://www.java2s.com:80/Code/Java/2D-Graphics-GUI/Aframethatdisplaysanimage.htm
---
```java title=Example.java
/*
 * @(#)ImageFrame.java    0.90 9/19/00 Adam Doppelt
 */
import java.awt.*;
import java.awt.image.MemoryImageSource;
import java.io.File;
import java.io.IOException;
/**
 * A frame that displays an image. Create an ImageFrame, then use one
 * of the setImage() methods to show the image.
 *
 * @version 0.90 19 Sep 2000
 * @author <a href="http://www.gurge.com/amd/">Adam Doppelt</a>
 */
public class ImageFrame extends Frame {
    int left = -1;
    int top;
    Image image;
    ImageFrame() {
        setLayout(null);
        setSize(100, 100);
    }
    /**
     * Set the image from a file.
     */
    public void setImage(File file) throws IOException {
        // load the image
        Image image = getToolkit().getImage(file.getAbsolutePath());
        // wait for the image to entirely load
        MediaTracker tracker = new MediaTracker(this);
        tracker.addImage(image, 0);
        try {
            tracker.waitForID(0);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        if (tracker.statusID(0, true) != MediaTracker.COMPLETE) {
            throw new IOException("Could not load: " + file + " " +
                                  tracker.statusID(0, true));
        }
        setTitle(file.getName());
        setImage(image);
    }
    /**
     * Set the image from an AWT image object.
     */
    public void setImage(Image image) {
        this.image = image;
        setVisible(true);
    }
    /**
     * Set the image from an indexed color array.
     */
    public void setImage(int palette[], int pixels[][]) {
        int w = pixels.length;
        int h = pixels[0].length;
        int pix[] = new int[w * h];
        // convert to RGB
        for (int x = w; x-- > 0; ) {
            for (int y = h; y-- > 0; ) {
                pix[y * w + x] = palette[pixels[x][y]];
            }
        }
        setImage(w, h, pix);
    }
    /**
     * Set the image from a 2D RGB pixel array.
     */
    public void setImage(int pixels[][]) {
        int w = pixels.length;
        int h = pixels[0].length;
        int pix[] = new int[w * h];
        // convert to RGB
        for (int x = w; x-- > 0; ) {
            for (int y = h; y-- > 0; ) {
                pix[y * w + x] = pixels[x][y];
            }
        }
        setImage(w, h, pix);
    }
    /**
     * Set the image from a 1D RGB pixel array.
     */
    public void setImage(int w, int h, int pix[]) {
        setImage(createImage(new MemoryImageSource(w, h, pix, 0, w)));
    }
    /**
     * Get the image.
     */
    public Image getImage() {
        return image;
    }
    /**
     * Overridden for double buffering.
     */
    public void update(Graphics g) {
        paint(g);
    }
    /**
     * Paint the image.
     */
    public void paint(Graphics g) {
        // the first time through, figure out where to draw the image
        if (left == -1) {
            Insets insets = getInsets();
            left = insets.left;
            top = insets.top;
            setSize(image.getWidth(null)  + left + insets.right,
                    image.getHeight(null) + top  + insets.bottom);
        }
        g.drawImage(image, left, top, this);
    }
    public static void main(String args[]) throws IOException {
        ImageFrame f = new ImageFrame();
        f.setImage(new File(args[0]));
    }
}
```

1.  Image size
---  ---
2.  Image demo
3.  Getting the Color Model of an Image
4.  Filtering the RGB Values in an Image
5.  Create a filter that can modify any of the RGB pixel values in an image.
6.  This filter removes all but the red values in an image
7.  Load and draw image
8.  Paint an Icon
9.  Image Processing: Brightness and Contrast
10.  Image with mouse drag and move event
11.  Image Animation and Thread
12.  Image Color Gray Effect
13.  Image Buffering
14.  Image Effect: Combine
15.  AffineTransform demo
16.  Image Effect: Rotate Image using DataBuffer
17.  Image Effect: Sharpen, blur
18.  Image scale
19.  Image crop
20.  Demonstrating the Drawing of an Image with a Convolve Operation
21.  Demonstrating Use of the Image I/O Library
22.  Adding Image-Dragging Behavior
23.  Sending Image Objects through the Clipboard
24.  Anti Alias
25.  Image Operations
26.  Image Viewer
27.  Get the dimensions of the image; these will be non-negative
28.  Standalone Image Viewer - works with any AWT-supported format
29.  Toolkit.getImage() which works the same in either Applet or Application
30.  Image Processing Test
31.  Image Transfer Test
32.  Double Buffered Image
33.  Graband Fade: displays image and fades to black
34.  Graband Fade with Rasters
35.  Rotate Image 45 Degrees
36.  Convert java.awt.image.BufferedImage to java.awt.Image
37.  Filter image by multiplier its red, green and blue color
38.  Drags within the image
39.  TYPE_INT_RGB and TYPE_INT_ARGB are typically used
40.  Pixels from a buffered image can be modified
41.  Calculation of the mean value of an image with Raster
42.  Use PixelGrabber class to acquire pixel data from an Image object
43.  Flip an image
44.  Rendered Image
45.  Image Panel
46.  Image Utils
47.  Returns an image resource.
48.  Create Gradient Image
49.  Create Gradient Mask
50.  Create Translucent Image
51.  Make Raster Writable
52.  Optimized version of copyData designed to work on Integer packed data with a SinglePixelPackedSampleModel
