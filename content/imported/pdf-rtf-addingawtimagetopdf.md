---
title: Adding AWT Image to PDF
nav: Adding AWT Image to PDF
description: PdfWriter writer = PdfWriter.getInstance(document, new FileOutputStream("AddingAWTImagePDF.pdf"));
section: Imported - java2s Archive
order: 1002
source: https://web.archive.org/web/20070410191429/http://www.java2s.com:80/Code/Java/PDF-RTF/AddingAWTImagetoPDF.htm
---
```java title=Example.java
import java.awt.Toolkit;
import java.io.FileOutputStream;
import com.lowagie.text.Document;
import com.lowagie.text.Image;
import com.lowagie.text.pdf.PdfContentByte;
import com.lowagie.text.pdf.PdfWriter;
public class AddingAWTImagePDF {
  public static void main(String[] args) {
    Document document = new Document();
    try {
      PdfWriter writer = PdfWriter.getInstance(document, new FileOutputStream("AddingAWTImagePDF.pdf"));
      document.open();
      PdfContentByte cb = writer.getDirectContent();
      java.awt.Image awtImage = Toolkit.getDefaultToolkit().createImage("logo.png");
      Image image = Image.getInstance(awtImage, null);
      image.setAbsolutePosition(100, 500);
      cb.addImage(image);
    } catch (Exception e) {
      System.err.println(e.getMessage());
    }
    document.close();
  }
}
```

Download: itext.zip ( 1,748 K )
Related examples in the same category
