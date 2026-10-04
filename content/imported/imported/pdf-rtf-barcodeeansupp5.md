---
title: BarcodeEAN
nav: BarcodeEAN
description: Document document = new Document(PageSize.A4, 50, 50, 50, 50);
section: Imported - java2s Archive
order: 1037
source: https://web.archive.org/web/20071201173844/http://www.java2s.com:80/Code/Java/PDF-RTF/BarcodeEANSUPP5.htm
---
BarcodeEAN: SUPP5

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
public class BarcodesSUPP5 {
  public static void main(String[] args) {
        Document document = new Document(PageSize.A4, 50, 50, 50, 50);
        try {
            PdfWriter writer = PdfWriter.getInstance(document, new FileOutputStream("BarcodesSUPP5.pdf"));
            document.open();
            PdfContentByte cb = writer.getDirectContent();
            BarcodeEAN codeSUPP = new BarcodeEAN();
            codeSUPP.setCodeType(Barcode.SUPP5);
            codeSUPP.setCode("12345");
            codeSUPP.setBaseline(-2);
            Image imagePost = codeSUPP.createImageWithBarcode(cb, null, null);
            document.add(new Phrase(new Chunk(imagePost, 0, 0)));
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
