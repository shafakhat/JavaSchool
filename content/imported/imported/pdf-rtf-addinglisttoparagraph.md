---
title: Adding List to Paragraph
nav: Adding List to Paragraph
description: PdfWriter.getInstance(document, new FileOutputStream("ListsAtoE.pdf"));
section: Imported - java2s Archive
order: 1014
source: https://web.archive.org/web/20071104040916/http://www.java2s.com:80/Code/Java/PDF-RTF/AddingListtoParagraph.htm
---
Adding List to Paragraph

```java title=Example.java
import java.io.FileOutputStream;
import com.lowagie.text.Document;
import com.lowagie.text.List;
import com.lowagie.text.Paragraph;
import com.lowagie.text.html.HtmlWriter;
import com.lowagie.text.pdf.PdfWriter;
public class PDFListsAtoE {
  public static void main(String[] args) {
    Document document = new Document();
    try {
      PdfWriter.getInstance(document, new FileOutputStream("ListsAtoE.pdf"));
      document.open();
      Paragraph paragraph = new Paragraph("A to E:");
      List list = new List(false, 10);
      list.add("A");
      list.add("B");
      list.add("C");
      list.add("D");
      list.add("E");
      paragraph.add(list);
      document.add(paragraph);
    } catch (Exception ioe) {
      System.err.println(ioe.getMessage());
    }
    document.close();
  }
}
```

itext.zip( 1,748 k)
