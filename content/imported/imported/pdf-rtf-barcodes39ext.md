---
title: Barcodes 39 Ext
nav: Barcodes 39 Ext
description: Document document = new Document(PageSize.A4, 50, 50, 50, 50);
section: Imported - java2s Archive
order: 1041
source: https://web.archive.org/web/20071201174647/http://www.java2s.com:80/Code/Java/PDF-RTF/Barcodes39Ext.htm
---
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
public class Barcodes39Ext {
  public static void main(String[] args) {
        Document document = new Document(PageSize.A4, 50, 50, 50, 50);
        try {
            PdfWriter writer = PdfWriter.getInstance(document, new FileOutputStream("Barcodes39Ext.pdf"));
            document.open();
            PdfContentByte cb = writer.getDirectContent();
            Barcode39 code39 = new Barcode39();
            code39.setCode("www.java2s.com");
            code39.setStartStopText(false);
            code39.setExtended(true);
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
