---
title: Cell Border Colors
nav: Cell Border Colors
description: PdfWriter writer = PdfWriter.getInstance(document, new FileOutputStream("CellBorderColorsPDF.pdf"));
section: Imported - java2s Archive
order: 1051
source: https://web.archive.org/web/20070117154808/http://www.java2s.com:80/Code/Java/PDF-RTF/CellBorderColors.htm
---
Cell Border Colors

```java title=Example.java
import java.awt.Color;
import java.io.FileOutputStream;
import com.lowagie.text.Document;
import com.lowagie.text.PageSize;
import com.lowagie.text.Paragraph;
import com.lowagie.text.Rectangle;
import com.lowagie.text.pdf.PdfPCell;
import com.lowagie.text.pdf.PdfPTable;
import com.lowagie.text.pdf.PdfWriter;
public class CellBorderColorsPDF {
  public static void main(String[] args) {
    Document document = new Document(PageSize.A4);
    try {
      PdfWriter writer = PdfWriter.getInstance(document,  new FileOutputStream("CellBorderColorsPDF.pdf"));
      document.open();
      PdfPTable table = new PdfPTable(1);
      PdfPCell  cell = new PdfPCell(new Paragraph("test colors:"));
      table.addCell(cell);
      cell = new PdfPCell(new Paragraph("red"));
      cell.setBorder(Rectangle.NO_BORDER);
      cell.setBackgroundColor(Color.red);
      table.addCell(cell);
      cell = new PdfPCell(new Paragraph("green"));
      cell.setBorder(Rectangle.BOTTOM);
      cell.setBorderColorBottom(Color.magenta);
      cell.setBorderWidthBottom(10f);
      cell.setBackgroundColor(Color.green);
      table.addCell(cell);
      document.add(table);
    } catch (Exception de) {
      de.printStackTrace();
    }
    document.close();
  }
}
```

Download: itext.zip ( 1,748 K )
Related examples in the same category
