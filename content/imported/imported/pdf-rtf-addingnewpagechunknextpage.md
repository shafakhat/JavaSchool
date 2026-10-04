---
title: Adding
nav: Adding
description: PdfWriter writer = PdfWriter.getInstance(document, new FileOutputStream("NewPageChunkNEXTPAGEPDF.pdf"));
section: Imported - java2s Archive
order: 1017
source: https://web.archive.org/web/20080808093802/http://www.java2s.com:80/Code/Java/PDF-RTF/AddingNewPageChunkNEXTPAGE.htm
---
Adding: NewPage, Chunk.NEXTPAGE

```java title=Example.java
import java.io.FileOutputStream;
import com.lowagie.text.Chunk;
import com.lowagie.text.Document;
import com.lowagie.text.Paragraph;
import com.lowagie.text.pdf.PdfWriter;
public class NewPageChunkNEXTPAGEPDF {
  public static void main(String[] args) {
    Document document = new Document();
    try {
      PdfWriter writer = PdfWriter.getInstance(document, new FileOutputStream("NewPageChunkNEXTPAGEPDF.pdf"));
      document.open();
      document.add(new Paragraph("A"));
      document.newPage();
      document.add(new Paragraph("B"));
      document.newPage();
      document.add(Chunk.NEXTPAGE);
      document.add(new Paragraph("C"));
    } catch (Exception ioe) {
      System.err.println(ioe.getMessage());
    }
    document.close();
  }
}
```

itext.zip( 1,748 k)
