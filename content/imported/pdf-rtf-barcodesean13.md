---
title: BarcodesEAN 13
nav: BarcodesEAN 13
description: Document document = new Document(PageSize.A4, 50, 50, 50, 50);
section: Imported - java2s Archive
order: 1042
source: https://web.archive.org/web/20071201173849/http://www.java2s.com:80/Code/Java/PDF-RTF/BarcodesEAN13.htm
---
BarcodesEAN 13

```java title=Example.java
import java.io.FileOutputStream;
import com.lowagie.text.Chunk;
import com.lowagie.text.Document;
import com.lowagie.text.Image;
import com.lowagie.text.PageSize;
import com.lowagie.text.Phrase;
import com.lowagie.text.pdf.Barcode;
import com.lowagie.text.pdf.BarcodeEAN;
import com.lowagie.text.pdf.PdfContentByte;
import com.lowagie.text.pdf.PdfWriter;
public class BarcodesEAN13 {
  public static void main(String[] args) {
        Document document = new Document(PageSize.A4, 50, 50, 50, 50);
        try {
            PdfWriter writer = PdfWriter.getInstance(document, new FileOutputStream("BarcodesEAN13.pdf"));
            document.open();
            PdfContentByte cb = writer.getDirectContent();
            BarcodeEAN codeEAN = new BarcodeEAN();
            codeEAN.setCodeType(Barcode.EAN13);
            codeEAN.setCode("1234567812345");
            Image imageEAN = codeEAN.createImageWithBarcode(cb, null, null);
            document.add(new Phrase(new Chunk(imageEAN, 0, 0)));
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
