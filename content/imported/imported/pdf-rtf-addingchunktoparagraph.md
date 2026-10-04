---
title: Adding Chunk to Paragraph
nav: Adding Chunk to Paragraph
description: PdfWriter writer = PdfWriter.getInstance(document, new FileOutputStream("AddingChunkToParagraphPDF.pdf"));
section: Imported - java2s Archive
order: 1009
source: https://web.archive.org/web/20100212120840/http://java2s.com/Code/Java/PDF-RTF/AddingChunktoParagraph.htm
---
```java title=Example.java
import java.io.FileOutputStream;
import com.lowagie.text.Chunk;
import com.lowagie.text.Document;
import com.lowagie.text.Font;
import com.lowagie.text.Paragraph;
import com.lowagie.text.pdf.PdfWriter;
public class AddingChunkToParagraphPDF {
  public static void main(String[] args) {
    try {
      Document document = new Document();
      PdfWriter writer = PdfWriter.getInstance(document, new FileOutputStream("AddingChunkToParagraphPDF.pdf"));
      document.open();
      Paragraph p = new Paragraph();
      p.add(new Chunk("Font.TIMES_ROMAN", new Font(Font.TIMES_ROMAN, 12)));
      document.add(new Paragraph(p));
      document.close();
    } catch (Exception de) {
      de.printStackTrace();
    }
  }
}
```

itext.zip( 1,748 k)
2.  Adding List to Paragraph
