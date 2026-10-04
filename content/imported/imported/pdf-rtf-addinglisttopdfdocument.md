---
title: Adding list to Pdf document
nav: Adding list to Pdf document
description: HtmlWriter.getInstance(document, new FileOutputStream("HTMLListsAtoEPDF.html"));
section: Imported - java2s Archive
order: 1015
source: https://web.archive.org/web/20080121105238/http://www.java2s.com:80/Code/Java/PDF-RTF/AddinglisttoPdfdocument.htm
---
Adding list to Pdf document

```java title=Example.java
import java.io.FileOutputStream;
import com.lowagie.text.Document;
import com.lowagie.text.List;
import com.lowagie.text.Paragraph;
import com.lowagie.text.html.HtmlWriter;
public class HTMLListsAtoEPDF {
  public static void main(String[] args) {
    Document document = new Document();
    try {
      HtmlWriter.getInstance(document, new FileOutputStream("HTMLListsAtoEPDF.html"));
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
4.  Lists with Different Font PDF and HTML
