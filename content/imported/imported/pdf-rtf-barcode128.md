---
title: Barcode 128
nav: Barcode 128
description: PdfWriter writer = PdfWriter.getInstance(document, new FileOutputStream("Barcode128.pdf"));
section: Imported - java2s Archive
order: 1036
source: https://web.archive.org/web/20071130181805/http://www.java2s.com:80/Code/Java/PDF-RTF/Barcode128.htm
---
```java title=Example.java
import java.awt.Color;
import java.io.FileOutputStream;
import com.lowagie.text.Chunk;
import com.lowagie.text.Document;
import com.lowagie.text.Element;
import com.lowagie.text.Image;
import com.lowagie.text.Phrase;
import com.lowagie.text.Rectangle;
import com.lowagie.text.pdf.Barcode128;
import com.lowagie.text.pdf.PdfContentByte;
import com.lowagie.text.pdf.PdfPCell;
import com.lowagie.text.pdf.PdfPTable;
import com.lowagie.text.pdf.PdfWriter;
public class Barcode128Demo {
  public static void main(String[] args) {
    Document document = new Document();
    try {
      PdfWriter writer = PdfWriter.getInstance(document, new FileOutputStream("Barcode128.pdf"));
      document.open();
      PdfContentByte cb = writer.getDirectContent();
      String code402 = "123456789012345" + Barcode128.FNC1;
      String code90 = "www.java2s.com" + Barcode128.FNC1;
      String code421 = "123456";
      String data = code402 + code90 + code421;
      Barcode128 shipBarCode = new Barcode128();
      shipBarCode.setX(0.75f);
      shipBarCode.setN(1.5f);
      shipBarCode.setChecksumText(true);
      shipBarCode.setGenerateChecksum(true);
      shipBarCode.setSize(10f);
      shipBarCode.setTextAlignment(Element.ALIGN_CENTER);
      shipBarCode.setBaseline(10f);
      shipBarCode.setCode(data);
      shipBarCode.setBarHeight(50f);
      Image imgShipBarCode = shipBarCode.createImageWithBarcode(cb, Color.black, Color.blue);
      document.add(imgShipBarCode);
    } catch (Exception e) {
      e.printStackTrace();
    }
    document.close();
  }
}
```

itext.zip( 1,748 k)
