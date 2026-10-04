---
title: Cell Border Colors With Background
nav: Cell Border Colors With Ba...
description: PdfWriter writer = PdfWriter.getInstance(document, new FileOutputStream("CellBorderColorsWidthBackgroundPDF.pdf"));
section: Imported - java2s Archive
order: 1052
source: https://web.archive.org/web/20070117161621/http://www.java2s.com:80/Code/Java/PDF-RTF/CellBorderColorsWithBackground.htm
---
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
public class CellBorderColorsWidthBackgroundPDF {
  public static void main(String[] args) {
    Document document = new Document(PageSize.A4);
    try {
      PdfWriter writer = PdfWriter.getInstance(document,  new FileOutputStream("CellBorderColorsWidthBackgroundPDF.pdf"));
      document.open();
      PdfPTable table = new PdfPTable(1);
      PdfPCell cell = new PdfPCell(new Paragraph("blue"));
      cell.setBorder(Rectangle.TOP);
      cell.setUseBorderPadding(true);
      cell.setBorderWidthTop(5f);
      cell.setBorderColorTop(Color.cyan);
      cell.setBackgroundColor(Color.blue);
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
