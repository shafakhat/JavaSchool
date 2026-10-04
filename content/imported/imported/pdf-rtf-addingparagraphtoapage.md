---
title: Adding Paragraph to a Page
nav: Adding Paragraph to a Page
description: PdfWriter.getInstance(document, new FileOutputStream("AddingParagraphToAPagePDF.pdf"));
section: Imported - java2s Archive
order: 1020
source: https://web.archive.org/web/20100212120752/http://java2s.com/Code/Java/PDF-RTF/AddingParagraphtoaPage.htm
---
Adding Paragraph to a Page

```java title=Example.java
import java.io.FileOutputStream;
import java.io.IOException;
import com.lowagie.text.Document;
import com.lowagie.text.DocumentException;
import com.lowagie.text.PageSize;
import com.lowagie.text.Paragraph;
import com.lowagie.text.pdf.PdfWriter;
public class AddingParagraphToAPagePDF {
  public static void main(String[] args) {
    Document document = new Document();
    try {
      PdfWriter.getInstance(document, new FileOutputStream("AddingParagraphToAPagePDF.pdf"));
      document.open();
      document.add(new Paragraph("First Page."));
      document.setPageSize(PageSize.A3);
      document.newPage();
      document.add(new Paragraph("This PageSize is A3."));
    } catch (Exception e) {
      System.err.println(e.getMessage());
    }
    document.close();
  }
}
```

itext.zip( 1,748 k)
2.  Adding List to Paragraph
