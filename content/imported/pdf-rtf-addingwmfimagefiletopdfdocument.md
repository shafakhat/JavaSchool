---
title: Adding WMF image file to Pdf document
nav: Adding WMF image file to P...
description: PdfWriter.getInstance(document, new FileOutputStream("ImagesWMFPDF.pdf"));
section: Imported - java2s Archive
order: 1028
source: https://web.archive.org/web/20071104162545/http://www.java2s.com:80/Code/Java/PDF-RTF/AddingWMFimagefiletoPdfdocument.htm
---
Adding WMF image file to Pdf document

```java title=Example.java
import java.io.FileOutputStream;
import com.lowagie.text.Document;
import com.lowagie.text.Image;
import com.lowagie.text.Paragraph;
import com.lowagie.text.pdf.PdfWriter;
public class ImagesWMFPDF {
  public static void main(String[] args) {
    Document document = new Document();
    try {
      PdfWriter.getInstance(document, new FileOutputStream("ImagesWMFPDF.pdf"));
      document.open();
      document.add(new Paragraph("load a WMF image file"));
      Image img = Image.getInstance("logo.WMF");
      document.add(img);
    } catch (Exception e) {
      System.err.println(e.getMessage());
    }
    document.close();
  }
}
```

itext.zip( 1,748 k)
