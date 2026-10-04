---
title: AffineTransformation in PDF
nav: AffineTransformation in PDF
description: PdfWriter writer = PdfWriter.getInstance(document, new FileOutputStream("AffineTransformationPDF.pdf"));
section: Imported - java2s Archive
order: 1031
source: https://web.archive.org/web/20080131104444/http://www.java2s.com:80/Code/Java/PDF-RTF/AffineTransformationinPDF.htm
---
AffineTransformation in PDF

```java title=Example.java
import java.awt.geom.AffineTransform;
import java.io.FileOutputStream;
import com.lowagie.text.Document;
import com.lowagie.text.PageSize;
import com.lowagie.text.pdf.PdfContentByte;
import com.lowagie.text.pdf.PdfWriter;
public class AffineTransformationPDF {
  public static void main(String[] args) {
    Document document = new Document(PageSize.A4);
    try {
      PdfWriter writer = PdfWriter.getInstance(document, new FileOutputStream("AffineTransformationPDF.pdf"));
      document.open();
      PdfContentByte cb = writer.getDirectContent();
      cb.transform(AffineTransform.getScaleInstance(1.2, 0.75));
      cb.moveTo(216, 720);
      cb.lineTo(360, 360);
      cb.lineTo(360, 504);
      cb.lineTo(72, 144);
      cb.lineTo(144, 288);
      cb.stroke();
    } catch (Exception e) {
      System.err.println(e.getMessage());
    }
    document.close();
  }
}
```

itext.zip( 1,748 k)
