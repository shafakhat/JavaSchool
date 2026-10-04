---
title: Adding PNG to table cell
nav: Adding PNG to table cell
description: PdfWriter.getInstance(document, new FileOutputStream("ImageTableCellPDF.pdf"));
section: Imported - java2s Archive
order: 1023
source: https://web.archive.org/web/20090422124811/http://www.java2s.com:80/Code/Java/PDF-RTF/AddingPNGtotablecell.htm
---
Adding PNG to table cell

```java title=Example.java
import java.io.FileOutputStream;
import com.lowagie.text.Document;
import com.lowagie.text.Image;
import com.lowagie.text.pdf.PdfPCell;
import com.lowagie.text.pdf.PdfPTable;
import com.lowagie.text.pdf.PdfWriter;
public class ImageTableCellPDF {
  public static void main(String[] args) {
    Document document = new Document();
    try {
      PdfWriter.getInstance(document, new FileOutputStream("ImageTableCellPDF.pdf"));
      document.open();
      Image image = Image.getInstance("logo.png");
      PdfPTable table = new PdfPTable(2);
      table.addCell("cell");
      table.addCell(image);
      table.addCell("cell");
      table.addCell(new PdfPCell(image, true));
      table.addCell("This three");
      table.addCell(new PdfPCell(image, false));
      document.add(table);
    } catch (Exception e) {
      System.err.println(e.getMessage());
    }
    document.close();
  }
}
```

itext.zip( 1,748 k)
