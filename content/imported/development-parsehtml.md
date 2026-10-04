---
title: Parse HTML
nav: Parse HTML
description: HTMLEditorKit.ParserCallback callback = new ReportAttributes();
section: Imported - java2s Archive
order: 1817
source: https://web.archive.org/web/20140829092116/http://www.java2s.com/Tutorial/Java/0120__Development/ParseHTML.htm
---
```java title=Example.java
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.URL;
import java.util.Enumeration;
import javax.swing.text.AttributeSet;
import javax.swing.text.MutableAttributeSet;
import javax.swing.text.html.HTML;
import javax.swing.text.html.HTMLEditorKit;
public class MainClass {
  public static void main(String[] args) {
    ParserGetter kit = new ParserGetter();
    HTMLEditorKit.Parser parser = kit.getParser();
    HTMLEditorKit.ParserCallback callback = new ReportAttributes();
    try {
      URL u = new URL("http:");
      InputStream in = u.openStream();
      InputStreamReader r = new InputStreamReader(in);
      parser.parse(r, callback, false);
    } catch (IOException e) {
      System.err.println(e);
    }
  }
}
class ReportAttributes extends HTMLEditorKit.ParserCallback {
  public void handleStartTag(HTML.Tag tag, MutableAttributeSet attributes, int position) {
    this.listAttributes(attributes);
  }
  private void listAttributes(AttributeSet attributes) {
    Enumeration e = attributes.getAttributeNames();
    while (e.hasMoreElements()) {
      Object name = e.nextElement();
      Object value = attributes.getAttribute(name);
      if (!attributes.containsAttribute(name.toString(), value)) {
        System.out.println("containsAttribute() fails");
      }
      if (!attributes.isDefined(name.toString())) {
        System.out.println("isDefined() fails");
      }
      System.out.println(name + "=" + value);
    }
  }
  public void handleSimpleTag(HTML.Tag tag, MutableAttributeSet attributes, int position) {
    this.listAttributes(attributes);
  }
}
class ParserGetter extends HTMLEditorKit {
  public HTMLEditorKit.Parser getParser() {
    return super.getParser();
  }
}
```

| 6.31.1. | List Tags |
|---|---|
| 6.31.2. | html parser DTD |
| 6.31.3. | Use javax.swing.text.html.HTMLEditorKit to parse HTML |
| 6.31.4. | extends HTMLEditorKit.ParserCallback |
| 6.31.5. | Parse HTML |
| 6.31.6. | Convert to HTML string |
| 6.31.7. | Escape HTML |
| 6.31.8. | Filter message string for characters that are sensitive in HTML |
| 6.31.9. | Filter the specified message string for characters that are sensitive in HTML |
| 6.31.10. | HTML color names |
| 6.31.11. | Text To HTML |
| 6.31.12. | Unescape HTML |
| 6.31.13. | Utility methods for dealing with HTML |
| 6.31.14. | insert HTML block dynamically |
| 6.31.15. | A collection of all character entites defined in the HTML4 standard. |
| 6.31.16. | Decode an HTML color string like '#F567BA;' into a Color |
