---
title: Adding Page Footer
nav: Adding Page Footer
description: Document document = new Document(PageSize.A4, 50, 50, 70, 70);
section: Imported - java2s Archive
order: 1018
source: https://web.archive.org/web/20091011114137/http://www.java2s.com:80/Code/Java/PDF-RTF/AddingPageFooter.htm
---
Adding Page Footer

```java title=Example.java
import java.io.FileOutputStream;
import com.lowagie.text.Document;
import com.lowagie.text.PageSize;
import com.lowagie.text.Paragraph;
import com.lowagie.text.Rectangle;
import com.lowagie.text.pdf.PdfPTable;
import com.lowagie.text.pdf.PdfPageEventHelper;
import com.lowagie.text.pdf.PdfWriter;
public class PageFooterPDF {
  public static void main(String[] args) {
    Document document = new Document(PageSize.A4, 50, 50, 70, 70);
    try {
      PdfWriter writer = PdfWriter.getInstance(document, new FileOutputStream("PageFooterPDF.pdf"));
      document.open();
      document.add(new Paragraph("text"));
      Rectangle page = document.getPageSize();
      PdfPTable foot = new PdfPTable(1);
      foot.addCell("Page 1");
      foot.setTotalWidth(page.width() - document.leftMargin() - document.rightMargin());
      foot.writeSelectedRows(0, -1, document.leftMargin(), document.bottomMargin(),
            writer.getDirectContent());
      document.close();
    } catch (Exception de) {
      de.printStackTrace();
    }
  }
}
```

itext.zip( 1,748 k)
