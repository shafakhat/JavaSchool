---
title: Adding PNG image to Pdf document
nav: Adding PNG image to Pdf do...
description: PdfWriter.getInstance(document, new FileOutputStream("ImagesBOTTOMPDF.pdf"));
section: Imported - java2s Archive
order: 1022
source: https://web.archive.org/web/20090227122709/http://www.java2s.com:80/Code/Java/PDF-RTF/AddingPNGimagetoPdfdocument.htm
---
```java title=Example.java
import java.io.FileOutputStream;
import com.lowagie.text.Chunk;
import com.lowagie.text.Document;
import com.lowagie.text.Image;
import com.lowagie.text.Phrase;
import com.lowagie.text.pdf.PdfWriter;
public class ImagesBOTTOMPDF {
  public static void main(java.lang.String[] args) {
    Document document = new Document();
    try {
      PdfWriter.getInstance(document, new FileOutputStream("ImagesBOTTOMPDF.pdf"));
      document.open();
      Image imageRight = Image.getInstance("logo.png");
      imageRight.setAlignment(Image.BOTTOM);
      for (int i = 0; i < 100; i++) {
        document.add(new Phrase("Text "));
      }
      document.add(imageRight);
      for (int i = 0; i < 100; i++) {
        document.add(new Phrase("Text "));
      }
    } catch (Exception e) {
      System.err.println(e.getMessage());
    }
    document.close();
  }
}
```

itext.zip( 1,748 k)
