---
title: Adding PNG image to document
nav: Adding PNG image to document
description: PdfWriter.getInstance(document, new FileOutputStream("ImagesPNGPDF.pdf"));
section: Imported - java2s Archive
order: 1021
source: https://web.archive.org/web/20100212132401/http://java2s.com/Code/Java/PDF-RTF/AddingPNGimagetodocument.htm
---
```java title=Example.java
import java.io.FileOutputStream;
import com.lowagie.text.Document;
import com.lowagie.text.Image;
import com.lowagie.text.Paragraph;
import com.lowagie.text.pdf.PdfWriter;
public class ImagesPNGPDF {
  public static void main(String[] args) {
    Document document = new Document();
    try {
      PdfWriter.getInstance(document, new FileOutputStream("ImagesPNGPDF.pdf"));
      document.open();
      document.add(new Paragraph("load a png image file"));
      Image img = Image.getInstance("logo.png");
      document.add(img);
    } catch (Exception e) {
      System.err.println(e.getMessage());
    }
    document.close();
  }
}
```

itext.zip( 1,748 k)
