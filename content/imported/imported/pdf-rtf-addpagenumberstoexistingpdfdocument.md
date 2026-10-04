---
title: Add Page Numbers to Existing PDF document
nav: Add Page Numbers to Existi...
description: PdfStamper stamp = new PdfStamper(reader, new FileOutputStream("AddPageNumbersToExistingPageNumberPDF.pdf"));
section: Imported - java2s Archive
order: 1029
source: https://web.archive.org/web/20070831234951/http://www.java2s.com:80/Code/Java/PDF-RTF/AddPageNumberstoExistingPDFdocument.htm
---
```java title=Example.java
import java.io.FileOutputStream;
import com.lowagie.text.Element;
import com.lowagie.text.pdf.BaseFont;
import com.lowagie.text.pdf.PdfContentByte;
import com.lowagie.text.pdf.PdfReader;
import com.lowagie.text.pdf.PdfStamper;
public class AddPageNumbersToExistingPageNumberPDF {
  public static void main(String[] args) {
    try {
      PdfReader reader = new PdfReader("YourOwnPDF.pdf");
      int n = reader.getNumberOfPages();
      PdfStamper stamp = new PdfStamper(reader, new FileOutputStream("AddPageNumbersToExistingPageNumberPDF.pdf"));
      int i = 0;
      PdfContentByte over;
      BaseFont bf = BaseFont.createFont(BaseFont.HELVETICA, BaseFont.WINANSI, BaseFont.EMBEDDED);
      while (i < n) {
        i++;
        over = stamp.getOverContent(i);
        over.beginText();
        over.setFontAndSize(bf, 18);
        over.setTextMatrix(30, 30);
        over.showText("page " + i);
        over.setFontAndSize(bf, 32);
        over.showTextAligned(Element.ALIGN_LEFT, "DUPLICATE", 230, 430, 45);
        over.endText();
      }
      stamp.close();
    } catch (Exception de) {
      de.printStackTrace();
    }
  }
}
```

itext.zip( 1,748 k)
1.  Reads the pages of an existing PDF file and puts 2 pages from the existing doc into one of the new doc
2.  Reading Your Own PDF File
