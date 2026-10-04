---
title: Barcodes 128 (2)
nav: Barcodes 128 (2)
description: Document document = new Document(PageSize.A4, 50, 50, 50, 50);
section: Imported - java2s Archive
order: 1039
source: https://web.archive.org/web/20071201174642/http://www.java2s.com:80/Code/Java/PDF-RTF/Barcodes1282.htm
---
```java title=Example.java
import java.io.FileOutputStream;
import com.lowagie.text.Chunk;
import com.lowagie.text.Document;
import com.lowagie.text.Image;
import com.lowagie.text.PageSize;
import com.lowagie.text.Phrase;
import com.lowagie.text.pdf.Barcode128;
import com.lowagie.text.pdf.Barcode39;
import com.lowagie.text.pdf.PdfContentByte;
import com.lowagie.text.pdf.PdfWriter;
public class Barcodes128 {
  public static void main(String[] args) {
    Document document = new Document(PageSize.A4, 50, 50, 50, 50);
    try {
      PdfWriter writer = PdfWriter.getInstance(document, new FileOutputStream("Barcodes128.pdf"));
      document.open();
      PdfContentByte cb = writer.getDirectContent();
      Barcode128 code128 = new Barcode128();
      code128.setCode("JavaSchool");
      Image image128 = code128.createImageWithBarcode(cb, null, null);
      document.add(new Phrase(new Chunk(image128, 0, 0)));
    } catch (Exception de) {
      de.printStackTrace();
    }
    document.close();
  }
}
```

itext.zip( 1,748 k)
2.  Barcode 128
