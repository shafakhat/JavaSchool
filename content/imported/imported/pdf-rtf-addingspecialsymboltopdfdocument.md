---
title: Adding Special Symbol to Pdf document
nav: Adding Special Symbol to P...
description: PdfWriter.getInstance(document, new FileOutputStream("SpecialSymbolPDF.pdf"));
section: Imported - java2s Archive
order: 1025
source: https://web.archive.org/web/20071020034557/http://java2s.com:80/Code/Java/PDF-RTF/AddingSpecialSymboltoPdfdocument.htm
---
Adding Special Symbol to Pdf document

```java title=Example.java
import java.io.FileOutputStream;
import java.io.IOException;
import com.lowagie.text.Document;
import com.lowagie.text.DocumentException;
import com.lowagie.text.Phrase;
import com.lowagie.text.pdf.PdfWriter;
public class SpecialSymbolPDF {
  public static void main(String[] args) {
    Document document = new Document();
    try {
      PdfWriter.getInstance(document, new FileOutputStream("SpecialSymbolPDF.pdf"));
      document.open();
      for (int i = 913; i < 970; i++) {
        document.add(Phrase.getInstance(" " + i + ": " + (char) i));
      }
    } catch (DocumentException de) {
      System.err.println(de.getMessage());
    } catch (IOException ioe) {
      System.err.println(ioe.getMessage());
    }
    document.close();
  }
}
```

itext.zip( 1,748 k)
