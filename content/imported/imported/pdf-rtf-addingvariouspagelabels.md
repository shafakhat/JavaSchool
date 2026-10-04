---
title: Adding various Page labels
nav: Adding various Page labels
description: PdfWriter writer = PdfWriter.getInstance(document, new FileOutputStream("PageLabelsPDF.pdf"));
section: Imported - java2s Archive
order: 1027
source: https://web.archive.org/web/20080102040815/http://www.java2s.com:80/Code/Java/PDF-RTF/AddingvariousPagelabels.htm
---
Adding various Page labels

```java title=Example.java
import java.io.FileOutputStream;
import java.io.IOException;
import com.lowagie.text.Document;
import com.lowagie.text.DocumentException;
import com.lowagie.text.Paragraph;
import com.lowagie.text.pdf.PdfPageLabels;
import com.lowagie.text.pdf.PdfWriter;
public class PageLabelsPDF {
  public static void main(String[] args) {
    Document document = new Document();
    try {
      PdfWriter writer = PdfWriter.getInstance(document, new FileOutputStream("PageLabelsPDF.pdf"));
      writer.setViewerPreferences(PdfWriter.PageModeUseThumbs);
      document.open();
      PdfPageLabels pageLabels = new PdfPageLabels();
      pageLabels.addPageLabel(1, PdfPageLabels.LOWERCASE_ROMAN_NUMERALS);
      pageLabels.addPageLabel(2, PdfPageLabels.UPPERCASE_LETTERS);
      pageLabels.addPageLabel(3, PdfPageLabels.LOWERCASE_LETTERS);
      pageLabels.addPageLabel(4, PdfPageLabels.UPPERCASE_ROMAN_NUMERALS);
      pageLabels.addPageLabel(5, PdfPageLabels.DECIMAL_ARABIC_NUMERALS);
      pageLabels.addPageLabel(8, PdfPageLabels.DECIMAL_ARABIC_NUMERALS, "A-", 8);
      writer.setPageLabels(pageLabels);
      for (int i = 1; i <= 10; ++i) {
        document.add(new Paragraph("Page " + i));
        document.newPage();
      }
    } catch (Exception e) {
      System.err.println(e.getMessage());
    }
    document.close();
  }
}
```

itext.zip( 1,748 k)
