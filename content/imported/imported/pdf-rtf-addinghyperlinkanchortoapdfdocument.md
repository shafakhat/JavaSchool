---
title: Adding Hyperlink anchor to a PDF Document
nav: Adding Hyperlink anchor to...
description: PdfWriter.getInstance(document, new FileOutputStream("AHrefForAWebsitePDF.pdf"));
section: Imported - java2s Archive
order: 1011
source: https://web.archive.org/web/20070328231143/http://www.java2s.com:80/Code/Java/PDF-RTF/AddingHyperlinkanchortoaPDFDocument.htm
---
```java title=Example.java
import java.awt.Color;
import java.io.FileOutputStream;
import java.io.IOException;
import com.lowagie.text.Anchor;
import com.lowagie.text.Chunk;
import com.lowagie.text.Document;
import com.lowagie.text.DocumentException;
import com.lowagie.text.Font;
import com.lowagie.text.FontFactory;
import com.lowagie.text.Paragraph;
import com.lowagie.text.html.HtmlWriter;
import com.lowagie.text.pdf.PdfWriter;
public class AHrefForAWebsitePDF {
  public static void main(String[] args) {
    Document document = new Document();
    try {
      PdfWriter.getInstance(document, new FileOutputStream("AHrefForAWebsitePDF.pdf"));
      HtmlWriter.getInstance(document, new FileOutputStream("AHrefForAWebsite.html"));
      document.open();
      Paragraph paragraph = new Paragraph("Please visit my ");
      Anchor anchor1 = new Anchor("website (external reference)", FontFactory.getFont(FontFactory.HELVETICA, 12, Font.UNDERLINE, new Color(0, 0, 255)));
      anchor1.setReference("http://www.java2s.com");
      paragraph.add(anchor1);
      document.add(paragraph);
    } catch (Exception e) {
      System.err.println(e.getMessage());
    }
    document.close();
  }
}
```

Download: itext.zip ( 1,748 K )
Related examples in the same category
