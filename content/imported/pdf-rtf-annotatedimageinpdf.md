---
title: Annotated Image in PDF
nav: Annotated Image in PDF
description: Document document = new Document(PageSize.A4, 50, 50, 50, 50);
section: Imported - java2s Archive
order: 1034
source: https://web.archive.org/web/20100212194406/http://java2s.com/Code/Java/PDF-RTF/AnnotatedImageinPDF.htm
---
```java title=Example.java
import java.io.FileOutputStream;
import com.lowagie.text.Annotation;
import com.lowagie.text.Document;
import com.lowagie.text.Image;
import com.lowagie.text.PageSize;
import com.lowagie.text.pdf.PdfWriter;
public class AnnotatedImagePDF {
  public static void main(String[] args) {
    Document document = new Document(PageSize.A4, 50, 50, 50, 50);
    try {
      PdfWriter.getInstance(document, new FileOutputStream("AnnotatedImagePDF.pdf"));
      document.open();
      Image jpeg = Image.getInstance("logo.png");
      jpeg.setAnnotation(new Annotation("picture", "This is the logo", 0, 0, 0, 0));
      jpeg.setAbsolutePosition(100f, 550f);
      document.add(jpeg);
    } catch (Exception de) {
      de.printStackTrace();
    }
    document.close();
  }
}
```

itext.zip( 1,748 k)
