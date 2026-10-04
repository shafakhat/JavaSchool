---
title: Adding Gif image to Pdf document
nav: Adding Gif image to Pdf do...
description: PdfWriter.getInstance(document, new FileOutputStream("ImagesGIFPDF.pdf"));
section: Imported - java2s Archive
order: 1010
source: https://web.archive.org/web/20071106044640/http://www.java2s.com:80/Code/Java/PDF-RTF/AddingGifimagetoPdfdocument.htm
---
```java title=Example.java
import java.io.FileOutputStream;
import java.io.IOException;
import com.lowagie.text.Document;
import com.lowagie.text.DocumentException;
import com.lowagie.text.Image;
import com.lowagie.text.Paragraph;
import com.lowagie.text.pdf.PdfWriter;
public class ImagesGIFPDF {
  public static void main(String[] args) {
    Document document = new Document();
    try {
      PdfWriter.getInstance(document, new FileOutputStream("ImagesGIFPDF.pdf"));
      document.open();
      document.add(new Paragraph("load a gif image file"));
      Image img = Image.getInstance("logo.gif");
      document.add(img);
    } catch (Exception e) {
      System.err.println(e.getMessage());
    }
    document.close();
  }
}
```

itext.zip( 1,748 k)
