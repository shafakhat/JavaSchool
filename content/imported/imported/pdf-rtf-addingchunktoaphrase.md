---
title: Adding Chunk to a Phrase
nav: Adding Chunk to a Phrase
description: PdfWriter.getInstance(document, new FileOutputStream("PhraseInaChunkPDF.pdf"));
section: Imported - java2s Archive
order: 1008
source: https://web.archive.org/web/20100213224453/http://java2s.com/Code/Java/PDF-RTF/AddingChunktoaPhrase.htm
---
Adding Chunk to a Phrase

```java title=Example.java
import java.io.FileOutputStream;
import com.lowagie.text.Chunk;
import com.lowagie.text.Document;
import com.lowagie.text.Phrase;
import com.lowagie.text.pdf.PdfWriter;
public class PhraseInaChunkPDF {
  public static void main(String[] args) {
    Document document = new Document();
    try {
      PdfWriter.getInstance(document, new FileOutputStream("PhraseInaChunkPDF.pdf"));
      document.open();
      Phrase phrase = new Phrase(new Chunk("this is a phrase in a chunk\n"));
      document.add(phrase);
    } catch (Exception ioe) {
      System.err.println(ioe.getMessage());
    }
    document.close();
  }
}
```

itext.zip( 1,748 k)
3.  Phrase with Several Chunks and Different Fonts
