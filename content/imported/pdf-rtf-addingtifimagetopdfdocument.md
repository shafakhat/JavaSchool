---
title: Adding Tif image to Pdf Document
nav: Adding Tif image to Pdf Do...
description: PdfWriter.getInstance(document, new FileOutputStream("ImagesTIFPDF.pdf"));
section: Imported - java2s Archive
order: 1026
source: https://web.archive.org/web/20071018071930/http://java2s.com:80/Code/Java/PDF-RTF/AddingTifimagetoPdfDocument.htm
---
```java title=Example.java
import java.io.FileOutputStream;
import java.io.IOException;
import com.lowagie.text.Document;
import com.lowagie.text.DocumentException;
import com.lowagie.text.Image;
import com.lowagie.text.Paragraph;
import com.lowagie.text.pdf.PdfWriter;
public class ImagesTIFPDF {
  public static void main(String[] args) {
    Document document = new Document();
    try {
      PdfWriter.getInstance(document, new FileOutputStream("ImagesTIFPDF.pdf"));
      document.open();
      document.add(new Paragraph("load a tif image file"));
      Image img = Image.getInstance("logo.tif");
      document.add(img);
    } catch (Exception e) {
      System.err.println(e.getMessage());
    }
    document.close();
  }
}
```

itext.zip( 1,748 k)
