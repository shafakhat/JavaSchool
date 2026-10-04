---
title: Barcodes 39
nav: Barcodes 39
description: Document document = new Document(PageSize.A4, 50, 50, 50, 50);
section: Imported - java2s Archive
order: 1040
source: https://web.archive.org/web/20071201174303/http://www.java2s.com:80/Code/Java/PDF-RTF/Barcodes39.htm
---
Barcodes 39

```java title=Example.java
import java.io.FileOutputStream;
import com.lowagie.text.Chunk;
import com.lowagie.text.Document;
import com.lowagie.text.Image;
import com.lowagie.text.PageSize;
import com.lowagie.text.Phrase;
import com.lowagie.text.pdf.Barcode39;
import com.lowagie.text.pdf.PdfContentByte;
import com.lowagie.text.pdf.PdfWriter;
public class Barcodes39 {
  public static void main(String[] args) {
        Document document = new Document(PageSize.A4, 50, 50, 50, 50);
        try {
            PdfWriter writer = PdfWriter.getInstance(document, new FileOutputStream("Barcodes39.pdf"));
            document.open();
            PdfContentByte cb = writer.getDirectContent();
            Barcode39 code39 = new Barcode39();
            code39.setCode("CODE39-1234567890");
            code39.setStartStopText(false);
            Image image39 = code39.createImageWithBarcode(cb, null, null);
            document.add(new Phrase(new Chunk(image39, 0, 0)));
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
