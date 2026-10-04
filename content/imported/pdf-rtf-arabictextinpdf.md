---
title: Arabic Text in PDF
nav: Arabic Text in PDF
description: Document document = new Document(PageSize.A4, 50, 50, 50, 50);
section: Imported - java2s Archive
order: 1035
source: https://web.archive.org/web/20071020032246/http://java2s.com:80/Code/Java/PDF-RTF/ArabicTextinPDF.htm
---
```java title=Example.java
import java.io.FileOutputStream;
import com.lowagie.text.Document;
import com.lowagie.text.PageSize;
import com.lowagie.text.pdf.PdfContentByte;
import com.lowagie.text.pdf.PdfWriter;
public class ArabicTextPDF {
  public static void main(String[] args) {
    Document document = new Document(PageSize.A4, 50, 50, 50, 50);
    try {
      PdfWriter writer = PdfWriter.getInstance(document, new FileOutputStream("ArabicTextPDF.pdf"));
      document.open();
      java.awt.Font font = new java.awt.Font("arial", 0, 18);
      PdfContentByte cb = writer.getDirectContent();
      java.awt.Graphics2D g2 = cb.createGraphicsShapes(PageSize.A4.width(), PageSize.A4.height());
      g2.setFont(font);
      g2.drawString("\u0634\u0627\u062f\u062c\u0645\u0647\u0648\u0645\u0646", 100, 100);
      g2.dispose();
      document.close();
    } catch (Exception de) {
      de.printStackTrace();
    }
  }
}
```

itext.zip( 1,748 k)
