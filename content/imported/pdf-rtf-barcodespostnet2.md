---
title: BarcodesPostnet 2
nav: BarcodesPostnet 2
description: Document document = new Document(PageSize.A4, 50, 50, 50, 50);
section: Imported - java2s Archive
order: 1045
source: https://web.archive.org/web/20071201173908/http://www.java2s.com:80/Code/Java/PDF-RTF/BarcodesPostnet2.htm
---
```java title=Example.java
import java.io.FileOutputStream;
import com.lowagie.text.Chunk;
import com.lowagie.text.Document;
import com.lowagie.text.Image;
import com.lowagie.text.PageSize;
import com.lowagie.text.Phrase;
import com.lowagie.text.pdf.Barcode39;
import com.lowagie.text.pdf.BarcodePostnet;
import com.lowagie.text.pdf.PdfContentByte;
import com.lowagie.text.pdf.PdfWriter;
public class BarcodesPostnet {
  public static void main(String[] args) {
        Document document = new Document(PageSize.A4, 50, 50, 50, 50);
        try {
            PdfWriter writer = PdfWriter.getInstance(document, new FileOutputStream("BarcodesPostnet.pdf"));
            document.open();
            PdfContentByte cb = writer.getDirectContent();
            BarcodePostnet codePost = new BarcodePostnet();
            codePost.setCode("123451234");
            Image imagePost = codePost.createImageWithBarcode(cb, null, null);
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
