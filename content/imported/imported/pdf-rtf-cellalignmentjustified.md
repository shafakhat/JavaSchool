---
title: Cell Alignment Justified
nav: Cell Alignment Justified
description: Document document = new Document(PageSize.A4.rotate(), 10, 10, 10, 10);
section: Imported - java2s Archive
order: 1049
source: https://web.archive.org/web/20080612153657/http://www.java2s.com:80/Code/Java/PDF-RTF/CellAlignmentJustified.htm
---
Cell Alignment Justified

```java title=Example.java
import java.io.FileOutputStream;
import com.lowagie.text.Document;
import com.lowagie.text.Element;
import com.lowagie.text.PageSize;
import com.lowagie.text.Paragraph;
import com.lowagie.text.pdf.PdfPCell;
import com.lowagie.text.pdf.PdfPTable;
import com.lowagie.text.pdf.PdfWriter;
public class CellAlignmentJustifiedPDF {
  public static void main(String[] args) {
    Document document = new Document(PageSize.A4.rotate(), 10, 10, 10, 10);
    try {
      PdfWriter writer = PdfWriter.getInstance(document,  new FileOutputStream("CellAlignmentJustifiedPDF.pdf"));
      document.open();
      PdfPTable table = new PdfPTable(2);
      PdfPCell cell;
      Paragraph p = new Paragraph("Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text Text ");
      table.addCell("default alignment");
      cell = new PdfPCell(p);
      cell.setHorizontalAlignment(Element.ALIGN_JUSTIFIED);
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
