---
title: html parser DTD
nav: html parser DTD
description: Imported from the java2s.com archive: html parser DTD
section: Imported - java2s Archive
order: 1821
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0120__Development/htmlparserDTD.htm
---
```java title=Example.java
import java.io.IOException;
import javax.swing.text.html.parser.DTD;
public class MainClass {
  public static void main(String[] args) {
    try {
      DTD d1 = DTD.getDTD("html");
      for (int i = 0; i < 14; i++) {
        System.out.println(d1.getElement(i).getName());
      }
    } catch (IOException e) {
      System.err.println(e);
      e.printStackTrace();
    }
  }
}
java title=Example.java
#pcdata
html
meta
base
isindex
head
body
applet
param
p
title
style
link
script
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
