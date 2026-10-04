---
title: Adding More than One Chunk to PDF document
nav: Adding More than One Chunk...
description: PdfWriter.getInstance(document, new FileOutputStream("AddingMorethanOneChunkPDF.pdf"));
section: Imported - java2s Archive
order: 1016
source: https://web.archive.org/web/20071230035222/http://www.java2s.com:80/Code/Java/PDF-RTF/AddingMorethanOneChunktoPDFdocument.htm
---
Adding More than One Chunk to PDF document

```java title=Example.java
import java.awt.Color;
import java.io.FileOutputStream;
import java.io.IOException;
import com.lowagie.text.Chunk;
import com.lowagie.text.Document;
import com.lowagie.text.DocumentException;
import com.lowagie.text.pdf.PdfContentByte;
import com.lowagie.text.pdf.PdfWriter;
public class AddingMorethanOneChunkPDF {
  public static void main(String[] args) {
    Document document = new Document();
    try {
      PdfWriter.getInstance(document,  new FileOutputStream("AddingMorethanOneChunkPDF.pdf"));
      document.open();
      Chunk test = new Chunk("some text");
      float subscript = -8.0f;
      test.setTextRise(subscript);
      test.setUnderline(new Color(0xFF, 0x00, 0x00), 3.0f, 0.0f, -5.0f + subscript, 0.0f, PdfContentByte.LINE_CAP_ROUND);
      document.add(test);
      Chunk test1 = new Chunk("another text");
      document.add(test1);
    } catch (Exception e) {
      System.err.println(e.getMessage());
    }
    document.close();
  }
}
```

itext.zip( 1,748 k)
