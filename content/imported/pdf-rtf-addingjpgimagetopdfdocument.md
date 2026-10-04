---
title: Adding JPG image to Pdf document
nav: Adding JPG image to Pdf do...
description: PdfWriter.getInstance(document, new FileOutputStream("ImagesJPGPDF.pdf"));
section: Imported - java2s Archive
order: 1013
source: https://web.archive.org/web/20080102042336/http://www.java2s.com:80/Code/Java/PDF-RTF/AddingJPGimagetoPdfdocument.htm
---
```java title=Example.java
import java.io.FileOutputStream;
import com.lowagie.text.Document;
import com.lowagie.text.Image;
import com.lowagie.text.Paragraph;
import com.lowagie.text.pdf.PdfWriter;
public class ImagesJPGPDF {
  public static void main(String[] args) {
    Document document = new Document();
    try {
      PdfWriter.getInstance(document, new FileOutputStream("ImagesJPGPDF.pdf"));
      document.open();
      document.add(new Paragraph("load a jpg image file"));
      Image jpg = Image.getInstance("logo.jpg");
      document.add(jpg);
    } catch (Exception e) {
      System.err.println(e.getMessage());
    }
    document.close();
  }
}
```

itext.zip( 1,748 k)
