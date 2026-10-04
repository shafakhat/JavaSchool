---
title: Adding watermark to an image
nav: Adding watermark to an image
description: public static final Font DEFAULT_FONT = new Font("Arial", Font.BOLD, 18);
section: Imported - java2s Archive
order: 1013
source: https://web.archive.org/web/20110928152202/http://www.java2s.com:80/Code/Java/2D-Graphics-GUI/Addingwatermarktoanimage.htm
---
Adding watermark to an image

```java title=Example.java
import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.image.BufferedImage;
import java.io.File;
import javax.imageio.ImageIO;
public class WaterMark {
    public static final String DEFAULT_FORMAT = "jpg";
    public static final Color DEFAULT_COLOR = Color.LIGHT_GRAY;
    public static final Font DEFAULT_FONT = new Font("Arial", Font.BOLD, 18);
    public static String makeWaterMark(String fileName, String ctx)
        throws Exception {
        try {
            String dest = execute(ctx + "/" + fileName,"dest","Water", DEFAULT_COLOR, DEFAULT_FONT);
            return dest.substring(ctx.length());
        } catch (Exception ex) {
            return fileName;
        }
    }
    public static String execute(String src, String dest, String text,
        Color color, Font font) throws Exception {
        BufferedImage srcImage = ImageIO.read(new File(src));
        int width = srcImage.getWidth(null);
        int height = srcImage.getHeight(null);
        BufferedImage destImage = new BufferedImage(width, height,
                BufferedImage.TYPE_INT_RGB);
        Graphics g = destImage.getGraphics();
        g.drawImage(srcImage, 0, 0, width, height, null);
        g.setColor(color);
        g.setFont(font);
        g.fillRect(0, 0, 50, 50);
        g.drawString(text, width / 5, height - 10);
        g.dispose();
        ImageIO.write(destImage, DEFAULT_FORMAT, new File("dest.jpg"));
        return dest;
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
30.  Double Buffered Image
31.  Graband Fade: displays image and fades to black
32.  Graband Fade with Rasters
33.  Rotate Image 45 Degrees
34.  Convert java.awt.image.BufferedImage to java.awt.Image
35.  Filter image by multiplier its red, green and blue color
36.  Drags within the image
37.  TYPE_INT_RGB and TYPE_INT_ARGB are typically used
38.  Pixels from a buffered image can be modified
39.  Calculation of the mean value of an image with Raster
40.  Use PixelGrabber class to acquire pixel data from an Image object
41.  Flip an image
42.  Rendered Image
43.  Image Panel
44.  Image Utils
45.  Returns an image resource.
46.  Create Gradient Image
47.  Create Gradient Mask
48.  Create Translucent Image
49.  Make Raster Writable
50.  A frame that displays an image
51.  Optimized version of copyData designed to work on Integer packed data with a SinglePixelPackedSampleModel
52.  Various image processing operations.
53.  This program demonstrates the transfer of images between a Java application and the system clipboard.
54.  Scales down an image into a box of maxSideLenght x maxSideLength.
55.  Scale Image
56.  Crop Image
57.  Fit Image
58.  Converts a java.awt.Image into an array of pixels
59.  Creates a scaled copy of the source image.
60.  Provides useful methods for converting images from one colour depth to another.
61.  Reads an image in a file and creates a thumbnail in another file.
62.  Make image Transparency
63.  Clips the input image to the specified shape
64.  Image Sorter frame
65.  Returns an ImageIcon, or null if the path was invalid.
66.  Create new image from source image
67.  check if image supported
68.  Get supported image format
69.  get image thumbnail
70.  get image orientation type
71.  get fixing preview image
