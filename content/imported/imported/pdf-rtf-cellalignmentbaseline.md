---
title: Cell Alignment Baseline
nav: Cell Alignment Baseline
description: Document document = new Document(PageSize.A4.rotate(), 10, 10, 10, 10);
section: Imported - java2s Archive
order: 1047
source: https://web.archive.org/web/20070901093706/http://www.java2s.com:80/Code/Java/PDF-RTF/CellAlignmentBaseline.htm
---
Cell Alignment Baseline

```java title=Example.java
import java.io.FileOutputStream;
import com.lowagie.text.Document;
import com.lowagie.text.Element;
import com.lowagie.text.PageSize;
import com.lowagie.text.Paragraph;
import com.lowagie.text.pdf.PdfPCell;
import com.lowagie.text.pdf.PdfPTable;
import com.lowagie.text.pdf.PdfWriter;
public class CellAlignmentBaselinePDF {
  public static void main(String[] args) {
    Document document = new Document(PageSize.A4.rotate(), 10, 10, 10, 10);
    try {
      PdfWriter writer = PdfWriter.getInstance(document,  new FileOutputStream("CellAlignmentBaselinePDF.pdf"));
      document.open();
      PdfPTable table = new PdfPTable(2);
      PdfPCell cell;
      table.getDefaultCell().setVerticalAlignment(Element.ALIGN_BASELINE);
      Paragraph p = new Paragraph("Text Text\nText Text Text\nText\nText\nText\nText\nText\nText\nText Text Text\nText Text\nText ");
      table.addCell("default alignment");
      cell = new PdfPCell(p);
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
