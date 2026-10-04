---
title: BarcodePostnet
nav: BarcodePostnet
description: Document document = new Document(PageSize.A4, 50, 50, 50, 50);
section: Imported - java2s Archive
order: 1038
source: https://web.archive.org/web/20071201174637/http://www.java2s.com:80/Code/Java/PDF-RTF/BarcodePostnet.htm
---
BarcodePostnet

```java title=Example.java
import java.io.FileOutputStream;
import com.lowagie.text.Chunk;
import com.lowagie.text.Document;
import com.lowagie.text.Image;
import com.lowagie.text.PageSize;
import com.lowagie.text.Phrase;
import com.lowagie.text.pdf.Barcode;
import com.lowagie.text.pdf.BarcodePostnet;
import com.lowagie.text.pdf.PdfContentByte;
import com.lowagie.text.pdf.PdfWriter;
public class BarcodesPLANET {
  public static void main(String[] args) {
        Document document = new Document(PageSize.A4, 50, 50, 50, 50);
        try {
            PdfWriter writer = PdfWriter.getInstance(document, new FileOutputStream("BarcodesPLANET.pdf"));
            document.open();
            PdfContentByte cb = writer.getDirectContent();
            BarcodePostnet codePlanet = new BarcodePostnet();
            codePlanet.setCode("50201402356");
            codePlanet.setCodeType(Barcode.PLANET);
            Image imagePlanet = codePlanet.createImageWithBarcode(cb, null, null);
            document.add(new Phrase(new Chunk(imagePlanet, 0, 0)));
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
