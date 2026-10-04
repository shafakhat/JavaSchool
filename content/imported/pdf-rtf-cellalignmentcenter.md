---
title: Cell Alignment Center
nav: Cell Alignment Center
description: Document document = new Document(PageSize.A4.rotate(), 10, 10, 10, 10);
section: Imported - java2s Archive
order: 1048
source: https://web.archive.org/web/20080611232848/http://www.java2s.com:80/Code/Java/PDF-RTF/CellAlignmentCenter.htm
---
Cell Alignment Center

```java title=Example.java
import java.io.FileOutputStream;
import com.lowagie.text.Document;
import com.lowagie.text.Element;
import com.lowagie.text.PageSize;
import com.lowagie.text.Paragraph;
import com.lowagie.text.pdf.PdfPCell;
import com.lowagie.text.pdf.PdfPTable;
import com.lowagie.text.pdf.PdfWriter;
public class CellAlignmentCenterPDF {
  public static void main(String[] args) {
    Document document = new Document(PageSize.A4.rotate(), 10, 10, 10, 10);
    try {
      PdfWriter writer = PdfWriter.getInstance(document,  new FileOutputStream("CellAlignmentCenterPDF.pdf"));
      document.open();
      PdfPTable table = new PdfPTable(2);
      PdfPCell cell;
      Paragraph p = new Paragraph("Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text ");
      table.addCell("default alignment");
      cell = new PdfPCell(p);
      cell.setHorizontalAlignment(Element.ALIGN_CENTER);
      table.addCell(cell);
      table.addCell("right alignment");
      document.add(table);
    } catch (Exception de) {
      de.printStackTrace();
    }
    document.close();
  }
}
```

itext.zip( 1,748 k)
