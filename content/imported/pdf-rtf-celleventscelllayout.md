---
title: Cell Events
nav: Cell Events
description: Document document = new Document(PageSize.A4, 50, 50, 50, 50);
section: Imported - java2s Archive
order: 1053
source: https://web.archive.org/web/20080829203441/http://www.java2s.com:80/Code/Java/PDF-RTF/CellEventscellLayout.htm
---
Cell Events: cellLayout

```java title=Example.java
import java.io.FileOutputStream;
import com.lowagie.text.Document;
import com.lowagie.text.PageSize;
import com.lowagie.text.Phrase;
import com.lowagie.text.Rectangle;
import com.lowagie.text.pdf.PdfContentByte;
import com.lowagie.text.pdf.PdfPCell;
import com.lowagie.text.pdf.PdfPCellEvent;
import com.lowagie.text.pdf.PdfPTable;
import com.lowagie.text.pdf.PdfWriter;
public class CellEventsPDF {
  public static void main(String[] args) {
    Document document = new Document(PageSize.A4, 50, 50, 50, 50);
    try {
      PdfWriter writer = PdfWriter.getInstance(document, new FileOutputStream("CellEventsPDF.pdf"));
      document.open();
      PdfPTable table = new PdfPTable(1);
      PdfPCell cell = new PdfPCell();
      cell.setCellEvent(new MyCellEvent());
      cell.setPhrase(new Phrase("asdfasdf"));
      table.addCell(cell);
      table.setTotalWidth(300);
      document.add(table);
    } catch (Exception de) {
      de.printStackTrace();
    }
    document.close();
  }
}
class MyCellEvent implements PdfPCellEvent{
  public void cellLayout(PdfPCell cell, Rectangle position,
      PdfContentByte[] canvases) {
    PdfContentByte cb = canvases[PdfPTable.TEXTCANVAS];
    cb.moveTo(position.left(), position.bottom());
    cb.lineTo(position.right(), position.top());
    cb.stroke();
  }
}
```

itext.zip( 1,748 k)
