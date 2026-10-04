---
title: Adding Bookmarks for PDF document
nav: Adding Bookmarks for PDF d...
description: public void onParagraph(PdfWriter writer, Document document, float position) {
section: Imported - java2s Archive
order: 1005
source: https://web.archive.org/web/20070505041602/http://www.java2s.com:80/Code/Java/PDF-RTF/AddingBookmarksforPDFdocument.htm
---
```java title=Example.java
import java.io.FileOutputStream;
import com.lowagie.text.Document;
import com.lowagie.text.Font;
import com.lowagie.text.PageSize;
import com.lowagie.text.Paragraph;
import com.lowagie.text.pdf.PdfContentByte;
import com.lowagie.text.pdf.PdfDestination;
import com.lowagie.text.pdf.PdfOutline;
import com.lowagie.text.pdf.PdfPageEventHelper;
import com.lowagie.text.pdf.PdfWriter;
public class BookmarksPDF extends PdfPageEventHelper {
  public void onParagraph(PdfWriter writer, Document document, float position) {
    PdfContentByte cb = writer.getDirectContent();
    new PdfOutline(cb.getRootOutline(), new PdfDestination(PdfDestination.FITH, position), "paragraph at position: " +position);
  }
  public static void main(String[] args) {
    Document document = new Document(PageSize.A6);
    try {
      PdfWriter writer = PdfWriter.getInstance(document, new FileOutputStream("BookmarksPDF.pdf"));
      writer.setViewerPreferences(PdfWriter.PageModeUseOutlines);
      document.open();
      writer.setPageEvent(new BookmarksPDF());
      document.add(new Paragraph("Text", new Font(Font.HELVETICA, 12)));
      document.newPage();
      document.add(new Paragraph("Text Text", new Font(Font.HELVETICA, 24)));
      document.newPage();
      document.add(new Paragraph("Text Text Text", new Font(Font.HELVETICA, 36)));
      document.newPage();
      document.add(new Paragraph("Text Text Text Text", new Font(Font.HELVETICA, 48)));
    } catch (Exception de) {
      de.printStackTrace();
    }
    document.close();
  }
}
```

Download: itext.zip ( 1,748 K )
Related examples in the same category
