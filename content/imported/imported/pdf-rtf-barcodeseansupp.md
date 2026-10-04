---
title: BarcodesEAN SUPP
nav: BarcodesEAN SUPP
description: Document document = new Document(PageSize.A4, 50, 50, 50, 50);
section: Imported - java2s Archive
order: 1043
source: https://web.archive.org/web/20071201173857/http://www.java2s.com:80/Code/Java/PDF-RTF/BarcodesEANSUPP.htm
---
```java title=Example.java
import java.awt.Color;
import java.io.FileOutputStream;
import com.lowagie.text.Chunk;
import com.lowagie.text.Document;
import com.lowagie.text.Image;
import com.lowagie.text.PageSize;
import com.lowagie.text.Phrase;
import com.lowagie.text.pdf.Barcode;
import com.lowagie.text.pdf.BarcodeEAN;
import com.lowagie.text.pdf.BarcodeEANSUPP;
import com.lowagie.text.pdf.PdfContentByte;
import com.lowagie.text.pdf.PdfWriter;
public class BarcodesEANSUPP {
  public static void main(String[] args) {
        Document document = new Document(PageSize.A4, 50, 50, 50, 50);
        try {
            PdfWriter writer = PdfWriter.getInstance(document, new FileOutputStream("BarcodesEANSUPP.pdf"));
            document.open();
            PdfContentByte cb = writer.getDirectContent();
            BarcodeEAN codeEAN = new BarcodeEAN();
            codeEAN.setCodeType(Barcode.EAN13);
            codeEAN.setCode("9780123412344");
            BarcodeEAN codeSUPP = new BarcodeEAN();
            codeSUPP.setCodeType(Barcode.SUPP5);
            codeSUPP.setCode("12345");
            codeSUPP.setBaseline(-2);
            BarcodeEANSUPP eanSupp = new BarcodeEANSUPP(codeEAN, codeSUPP);
            Image imageEANSUPP = eanSupp.createImageWithBarcode(cb, null, Color.blue);
            document.add(new Phrase(new Chunk(imageEANSUPP, 0, 0)));
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
