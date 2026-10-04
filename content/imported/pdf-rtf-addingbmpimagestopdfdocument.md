---
title: Adding BMP images to Pdf document
nav: Adding BMP images to Pdf d...
description: PdfWriter.getInstance(document, new FileOutputStream("ImagesBMPPDF.pdf"));
section: Imported - java2s Archive
order: 1004
source: https://web.archive.org/web/20080102042331/http://www.java2s.com:80/Code/Java/PDF-RTF/AddingBMPimagestoPdfdocument.htm
---
Adding BMP images to Pdf document

```java title=Example.java
import java.io.FileOutputStream;
import java.io.IOException;
import com.lowagie.text.Document;
import com.lowagie.text.DocumentException;
import com.lowagie.text.Image;
import com.lowagie.text.Paragraph;
import com.lowagie.text.pdf.PdfWriter;
public class ImagesBMPPDF {
  public static void main(String[] args) {
    Document document = new Document();
    try {
      PdfWriter.getInstance(document, new FileOutputStream("ImagesBMPPDF.pdf"));
      document.open();
      document.add(new Paragraph("load a BMP image file"));
      Image img = Image.getInstance("logo.BMP");
      document.add(img);
    } catch (Exception e) {
      System.err.println(e.getMessage());
    }
    document.close();
  }
}
```

itext.zip( 1,748 k)
