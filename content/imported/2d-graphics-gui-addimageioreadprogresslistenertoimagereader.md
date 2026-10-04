---
title: Add Image IO Read Progress Listener to ImageReader
nav: Add Image IO Read Progress...
description: FileInputStream fileInputStream = new FileInputStream("a.gif");
section: Imported - java2s Archive
order: 1011
source: https://web.archive.org/web/20090531065540/http://www.java2s.com:80/Code/Java/2D-Graphics-GUI/AddImageIOReadProgressListenertoImageReader.htm
---
```java title=Example.java
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.FileInputStream;
import java.util.Iterator;
import javax.imageio.ImageIO;
import javax.imageio.ImageReader;
import javax.imageio.ImageWriter;
import javax.imageio.event.IIOReadProgressListener;
import javax.imageio.stream.ImageInputStream;
import javax.imageio.stream.ImageOutputStream;
public class Main{
  static public void main(String args[]) throws Exception {
    FileInputStream fileInputStream = new FileInputStream("a.gif");
    Iterator readers = ImageIO.getImageReadersBySuffix("GIF");
    ImageReader imageReader = (ImageReader) readers.next();
    ImageInputStream imageInputStream = ImageIO.createImageInputStream(fileInputStream);
    imageReader.setInput(imageInputStream, false);
    imageReader.addIIOReadProgressListener(new MyIIOReadProgressListener());
    BufferedImage image = imageReader.read(0);
    Iterator imageWriters = ImageIO.getImageWritersBySuffix("JPG");
    ImageWriter imageWriter = (ImageWriter) imageWriters.next();
    File file = new File("b.JPG");
    ImageOutputStream ios = ImageIO.createImageOutputStream(file);
    imageWriter.setOutput(ios);
    imageWriter.write(image);
  }
}
class MyIIOReadProgressListener implements IIOReadProgressListener{
  public void imageComplete(ImageReader source) {
    System.out.println("image complete " + source);
  }
  public void imageProgress(ImageReader source, float percentageDone) {
    System.out.println("image progress " + source + ": " + percentageDone + "%");
  }
  public void imageStarted(ImageReader source, int imageIndex) {
    System.out.println("image #" + imageIndex + " started " + source);
  }
  public void readAborted(ImageReader source) {
    System.out.println("read aborted " + source);
  }
  public void sequenceComplete(ImageReader source) {
    System.out.println("sequence complete " + source);
  }
  public void sequenceStarted(ImageReader source, int minIndex) {
    System.out.println("sequence started " + source + ": " + minIndex);
  }
  public void thumbnailComplete(ImageReader source) {
    System.out.println("thumbnail complete " + source);
  }
  public void thumbnailProgress(ImageReader source, float percentageDone) {
    System.out.println("thumbnail started " + source + ": " + percentageDone + "%");
  }
  public void thumbnailStarted(ImageReader source, int imageIndex, int thumbnailIndex) {
    System.out.println("thumbnail progress " + source + ", " + thumbnailIndex + " of "
        + imageIndex);
  }
}
```

1.  Show Image with ImageReader
---  ---
2.  Read an Image from a file
3.  Read an Image from inputStream
4.  Read an Image from URL
5.  Determining the Format of an Image in a File
6.  Detect the file type of the input stream prior to reading the image
7.  List the image formats that can be read and written
