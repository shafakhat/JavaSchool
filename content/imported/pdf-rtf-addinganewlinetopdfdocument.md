---
title: Adding a New Line to PDF document
nav: Adding a New Line to PDF d...
description: PdfWriter pdf = PdfWriter.getInstance(document, new FileOutputStream("AddingNewLinePDF.pdf"));
section: Imported - java2s Archive
order: 1001
source: https://web.archive.org/web/20090216142901/http://java2s.com:80/Code/Java/PDF-RTF/AddingaNewLinetoPDFdocument.htm
---
```java title=Example.java
import java.io.FileOutputStream;
import java.io.IOException;
import com.lowagie.text.Anchor;
import com.lowagie.text.Chunk;
import com.lowagie.text.Document;
import com.lowagie.text.DocumentException;
import com.lowagie.text.Paragraph;
import com.lowagie.text.html.HtmlWriter;
import com.lowagie.text.pdf.PdfWriter;
import com.lowagie.text.rtf.RtfWriter2;
public class AddingNewLinePDF {
  public static void main(String[] args) {
    Document document = new Document();
    try {
      PdfWriter pdf = PdfWriter.getInstance(document, new FileOutputStream("AddingNewLinePDF.pdf"));
      RtfWriter2 rtf = RtfWriter2.getInstance(document, new FileOutputStream("AddingNewLine.rtf"));
      HtmlWriter html = HtmlWriter.getInstance(document, new FileOutputStream("AddingNewLine.html"));
      document.open();
      document.add(new Paragraph("Some text"));
      Anchor pdfRef = new Anchor("http:");
      pdfRef.setReference("http:");
      Anchor rtfRef = new Anchor("Link for aFile.rtf.");
      rtfRef.setReference("./aFile.rtf");
      document.add(pdfRef);
      document.add(Chunk.NEWLINE);
      document.add(rtfRef);
    } catch (Exception e) {
      System.err.println(e.getMessage());
    }
    document.close();
  }
}
```

itext.zip( 1,748 k)
