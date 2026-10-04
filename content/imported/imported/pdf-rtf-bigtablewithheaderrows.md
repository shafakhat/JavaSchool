---
title: Big Table With Header Rows
nav: Big Table With Header Rows
description: Document document = new Document(PageSize.A4.rotate(), 10, 10, 10, 10);
section: Imported - java2s Archive
order: 1046
source: https://web.archive.org/web/20071130085318/http://www.java2s.com:80/Code/Java/PDF-RTF/BigTableWithHeaderRows.htm
---
```java title=Example.java
import java.io.FileOutputStream;
import com.lowagie.text.Document;
import com.lowagie.text.Element;
import com.lowagie.text.PageSize;
import com.lowagie.text.pdf.PdfPTable;
import com.lowagie.text.pdf.PdfWriter;
public class BigTableWithHeaderRowsPDF {
  public static void main(String[] args) {
    Document document = new Document(PageSize.A4.rotate(), 10, 10, 10, 10);
    try {
      PdfWriter.getInstance(document,  new FileOutputStream("BigTableWithHeaderRowsPDF.pdf"));
      document.open();
      int NumColumns = 12;
      PdfPTable datatable = new PdfPTable(NumColumns);
      int headerwidths[] = { 9, 4, 8, 10, 8, 11, 9, 7, 9, 10, 4, 10 }; // percentage
      datatable.setWidths(headerwidths);
      for(int i=0;i<headerwidths.length;i++){
        datatable.addCell("Header "+ i);
      }
      datatable.setHeaderRows(1);
      datatable.getDefaultCell().setBorderWidth(1);
      for (int i = 1; i < 1000; i++) {
        if (i % 2 == 1) {
          datatable.getDefaultCell().setGrayFill(0.9f);
        }
        for (int x = 0; x < NumColumns; x++) {
          datatable.addCell("data");
        }
        if (i % 2 == 1) {
          datatable.getDefaultCell().setGrayFill(1);
        }
      }
      document.add(datatable);
    } catch (Exception de) {
      de.printStackTrace();
    }
    document.close();
  }
}
```

itext.zip( 1,748 k)
