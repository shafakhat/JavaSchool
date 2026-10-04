---
title: BarcodesInter25
nav: BarcodesInter25
description: Document document = new Document(PageSize.A4, 50, 50, 50, 50);
section: Imported - java2s Archive
order: 1044
source: https://web.archive.org/web/20071201173906/http://www.java2s.com:80/Code/Java/PDF-RTF/BarcodesInter25.htm
---
```java title=Example.java
import java.io.FileOutputStream;
import com.lowagie.text.Chunk;
import com.lowagie.text.Document;
import com.lowagie.text.Image;
import com.lowagie.text.PageSize;
import com.lowagie.text.Phrase;
import com.lowagie.text.pdf.Barcode39;
import com.lowagie.text.pdf.BarcodeInter25;
import com.lowagie.text.pdf.PdfContentByte;
import com.lowagie.text.pdf.PdfWriter;
public class BarcodesInter25 {
  public static void main(String[] args) {
        Document document = new Document(PageSize.A4, 50, 50, 50, 50);
        try {
            PdfWriter writer = PdfWriter.getInstance(document, new FileOutputStream("BarcodesInter25.pdf"));
            document.open();
            PdfContentByte cb = writer.getDirectContent();
            BarcodeInter25 code25 = new BarcodeInter25();
            code25.setGenerateChecksum(true);
            code25.setCode("99-1234567890-001");
            Image image25 = code25.createImageWithBarcode(cb, null, null);
            document.add(new Phrase(new Chunk(image25, 0, 0)));
        }
        catch (Exception de) {
            de.printStackTrace();
        }
        document.close();
  }
}
```

itext.zip( 1,748 k)
2.  Barcode 128
