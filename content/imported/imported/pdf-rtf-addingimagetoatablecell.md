---
title: Adding Image to a Table Cell
nav: Adding Image to a Table Cell
description: PdfWriter.getInstance(document, new FileOutputStream("AddingImageToTableCellPDF.pdf"));
section: Imported - java2s Archive
order: 1012
source: https://web.archive.org/web/20090414062717/http://www.java2s.com:80/Code/Java/PDF-RTF/AddingImagetoaTableCell.htm
---
Adding Image to a Table Cell

```java title=Example.java
import java.io.FileOutputStream;
import com.lowagie.text.Chunk;
import com.lowagie.text.Document;
import com.lowagie.text.Image;
import com.lowagie.text.pdf.PdfPCell;
import com.lowagie.text.pdf.PdfPTable;
import com.lowagie.text.pdf.PdfWriter;
public class AddingImageToTableCellPDF {
  public static void main(String[] args) {
    Document.compress = false;
    Document document = new Document();
    try {
      PdfWriter.getInstance(document, new FileOutputStream("AddingImageToTableCellPDF.pdf"));
      document.open();
      Image img = Image.getInstance("logo.png");
      img.scalePercent(10);
      PdfPTable table = new PdfPTable(3);
      PdfPCell cell = new PdfPCell();
      cell.addElement(new Chunk(img, 5, -5));
      table.addCell("a cell");
      table.addCell(cell);
      table.addCell("a cell");
      document.add(table);
    } catch (Exception e) {
      System.err.println(e.getMessage());
    }
    document.close();
  }
}
```

itext.zip( 1,748 k)
