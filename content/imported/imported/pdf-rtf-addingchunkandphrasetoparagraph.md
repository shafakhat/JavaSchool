---
title: Adding Chunk and Phrase to Paragraph
nav: Adding Chunk and Phrase to...
description: PdfWriter.getInstance(document, new FileOutputStream("ParagraphsPDF.pdf"));
section: Imported - java2s Archive
order: 1007
source: https://web.archive.org/web/20100212120825/http://java2s.com/Code/Java/PDF-RTF/AddingChunkandPhrasetoParagraph.htm
---
```java title=Example.java
import java.io.FileOutputStream;
import java.io.IOException;
import com.lowagie.text.Chunk;
import com.lowagie.text.Document;
import com.lowagie.text.DocumentException;
import com.lowagie.text.FontFactory;
import com.lowagie.text.Paragraph;
import com.lowagie.text.Phrase;
import com.lowagie.text.pdf.PdfWriter;
public class ParagraphsPDF {
  public static void main(String[] args) {
    Document document = new Document();
    try {
      PdfWriter.getInstance(document, new FileOutputStream("ParagraphsPDF.pdf"));
      document.open();
      Paragraph p1 = new Paragraph(new Chunk("This is my first paragraph. ", FontFactory.getFont(FontFactory.HELVETICA, 10)));
      p1.add("The default leading is 1.5 times the fontsize. ");
      p1.add(new Chunk("new chunks "));
      p1.add(new Phrase("new phrases. "));
      document.add(p1);
    } catch (Exception ioe) {
      System.err.println(ioe.getMessage());
    }
    document.close();
  }
}
```

itext.zip( 1,748 k)
2.  Adding List to Paragraph
