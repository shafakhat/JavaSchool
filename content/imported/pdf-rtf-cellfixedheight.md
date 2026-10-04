---
title: Cell Fixed Height
nav: Cell Fixed Height
description: PdfWriter writer = PdfWriter.getInstance(document, new FileOutputStream("CellFixedHeightPDF.pdf"));
section: Imported - java2s Archive
order: 1054
source: https://web.archive.org/web/20071020033729/http://java2s.com:80/Code/Java/PDF-RTF/CellFixedHeight.htm
---
```java title=Example.java
import java.io.FileOutputStream;
import com.lowagie.text.Document;
import com.lowagie.text.PageSize;
import com.lowagie.text.Paragraph;
import com.lowagie.text.pdf.PdfPCell;
import com.lowagie.text.pdf.PdfPTable;
import com.lowagie.text.pdf.PdfWriter;
public class CellFixedHeightPDF {
  public static void main(String[] args) {
    Document document = new Document(PageSize.A4);
    try {
      PdfWriter writer = PdfWriter.getInstance(document,  new FileOutputStream("CellFixedHeightPDF.pdf"));
      document.open();
      PdfPTable table = new PdfPTable(2);
      PdfPCell cell = new PdfPCell(new Paragraph("Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text "));
      table.addCell("wrap");
      cell.setNoWrap(false);
      table.addCell(cell);
      table.addCell("no wrap");
      cell.setFixedHeight(50f);
      cell.setNoWrap(true);
      table.addCell(cell);
      document.add(table);
    } catch (Exception de) {
      de.printStackTrace();
    }
    document.close();
  }
}
```

itext.zip( 1,748 k)
