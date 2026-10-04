---
title: Adding Rectangle to a Column
nav: Adding Rectangle to a Column
description: PdfWriter writer = PdfWriter.getInstance(document, new FileOutputStream("AddingRectangleToColumnPDF.pdf"));
section: Imported - java2s Archive
order: 1024
source: https://web.archive.org/web/20080829120746/http://www.java2s.com/Code/Java/PDF-RTF/AddingRectangletoaColumn.htm
---
Adding Rectangle to a Column

```java title=Example.java
import java.io.FileOutputStream;
import com.lowagie.text.Document;
import com.lowagie.text.Element;
import com.lowagie.text.Font;
import com.lowagie.text.Phrase;
import com.lowagie.text.pdf.BaseFont;
import com.lowagie.text.pdf.ColumnText;
import com.lowagie.text.pdf.PdfContentByte;
import com.lowagie.text.pdf.PdfWriter;
public class AddingRectangleToColumnPDF {
  public static void main(String[] args) {
    Document document = new Document();
    try {
      PdfWriter writer = PdfWriter.getInstance(document, new FileOutputStream("AddingRectangleToColumnPDF.pdf"));
      document.open();
      BaseFont bf = BaseFont.createFont(BaseFont.COURIER, BaseFont.CP1252, BaseFont.NOT_EMBEDDED);
      Font font = new Font(bf, 11, Font.NORMAL);
      Phrase col1 = new Phrase(15, "col1", font);
      Phrase col2 = new Phrase(15, "col2", font);
      Phrase col3 = new Phrase(15, "col3", font);
      for (int i = 0; i < 40; i++) {
        col1.add("col 1\n");
        col2.add("col 2\n");
        col3.add("col 3\n");
      }
      PdfContentByte cb = writer.getDirectContent();
      ColumnText ct = new ColumnText(cb);
      ct.setSimpleColumn(col1, 60, 300, 100, 300 + 28 * 15, 15, Element.ALIGN_CENTER);
      ct.go();
      ct.setSimpleColumn(col2, 105, 300, 150, 300 + 28 * 15, 15, Element.ALIGN_RIGHT);
      ct.go();
      cb.rectangle(53, 295, 52, 8 + 28 * 15);
      cb.stroke();
      ct.setSimpleColumn(col3, 160, 300, 500, 300 + 28 * 15, 15, Element.ALIGN_LEFT);
      ct.go();
    } catch (Exception e) {
      System.err.println(e.getMessage());
    }
    document.close();
  }
}
```

itext.zip( 1,748 k)
