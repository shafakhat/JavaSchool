---
title: Adding Page Header
nav: Adding Page Header
description: Document document = new Document(PageSize.A4, 50, 50, 70, 70);
section: Imported - java2s Archive
order: 1019
source: https://web.archive.org/web/20091010110609/http://www.java2s.com:80/Code/Java/PDF-RTF/AddingPageHeader.htm
---
Adding Page Header

```java title=Example.java
import java.io.FileOutputStream;
import com.lowagie.text.Document;
import com.lowagie.text.PageSize;
import com.lowagie.text.Paragraph;
import com.lowagie.text.Rectangle;
import com.lowagie.text.pdf.PdfPTable;
import com.lowagie.text.pdf.PdfPageEventHelper;
import com.lowagie.text.pdf.PdfWriter;
public class PageHeaderPDF {
  public static void main(String[] args) {
    Document document = new Document(PageSize.A4, 50, 50, 70, 70);
    try {
      PdfWriter writer = PdfWriter.getInstance(document, new FileOutputStream("PageHeaderPDF.pdf"));
      document.open();
      document.add(new Paragraph("text"));
      Rectangle page = document.getPageSize();
      PdfPTable head = new PdfPTable(1);
        head.addCell("Page 1");
      head.setTotalWidth(page.width() - document.leftMargin() - document.rightMargin());
      head.writeSelectedRows(0, -1, document.leftMargin(), page.height() - document.topMargin()
          + head.getTotalHeight(), writer.getDirectContent());
      document.close();
    } catch (Exception de) {
      de.printStackTrace();
    }
  }
}
```

itext.zip( 1,748 k)
