---
title: Annotated Image HyperLink
nav: Annotated Image HyperLink
description: Document document = new Document(PageSize.A4, 50, 50, 50, 50);
section: Imported - java2s Archive
order: 1033
source: https://web.archive.org/web/20100212194419/http://java2s.com/Code/Java/PDF-RTF/AnnotatedImageHyperLink.htm
---
```java title=Example.java
import java.io.FileOutputStream;
import com.lowagie.text.Annotation;
import com.lowagie.text.Document;
import com.lowagie.text.Image;
import com.lowagie.text.PageSize;
import com.lowagie.text.pdf.PdfWriter;
public class AnnotatedImageHyperLink {
  public static void main(String[] args) {
    Document document = new Document(PageSize.A4, 50, 50, 50, 50);
    try {
      PdfWriter writer = PdfWriter.getInstance(document, new FileOutputStream("AnnotatedImageHyperLink.pdf"));
      document.open();
      Image png = Image.getInstance("logo.png");
      png.setAnnotation(new Annotation(0, 0, 0, 0, "http://www.java2s.com"));
      png.setAbsolutePosition(100f, 550f);
      document.add(png);
    } catch (Exception de) {
      de.printStackTrace();
    }
    document.close();
  }
}
```

itext.zip( 1,748 k)
