---
title: Text To HTML
nav: Text To HTML
description: This library is free software; you can redistribute it and/or
section: Imported - java2s Archive
order: 1834
source: https://web.archive.org/web/20140829092316/http://www.java2s.com/Tutorial/Java/0120__Development/TextToHTML.htm
---
```java title=Example.java
/*
    GNU LESSER GENERAL PUBLIC LICENSE
    Copyright (C) 2006 The XAMJ Project
    This library is free software; you can redistribute it and/or
    modify it under the terms of the GNU Lesser General Public
    License as published by the Free Software Foundation; either
    version 2.1 of the License, or (at your option) any later version.
    This library is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
    Lesser General Public License for more details.
    You should have received a copy of the GNU Lesser General Public
    License along with this library; if not, write to the Free Software
    Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
    Contact info: lobochief@users.sourceforge.net
*/
public class Html {
  public static String textToHTML(String text) {
    if(text == null) {
      return null;
    }
    int length = text.length();
    boolean prevSlashR = false;
    StringBuffer out = new StringBuffer();
    for(int i = 0; i < length; i++) {
      char ch = text.charAt(i);
      switch(ch) {
      case '\r':
        if(prevSlashR) {
          out.append("<br>");
        }
        prevSlashR = true;
        break;
      case '\n':
        prevSlashR = false;
        out.append("<br>");
        break;
      case '"':
        if(prevSlashR) {
          out.append("<br>");
          prevSlashR = false;
        }
        out.append("&quot;");
        break;
      case '<':
        if(prevSlashR) {
          out.append("<br>");
          prevSlashR = false;
        }
        out.append("&lt;");
        break;
      case '>':
        if(prevSlashR) {
          out.append("<br>");
          prevSlashR = false;
        }
        out.append("&gt;");
        break;
      case '&':
        if(prevSlashR) {
          out.append("<br>");
          prevSlashR = false;
        }
        out.append("&amp;");
        break;
      default:
        if(prevSlashR) {
          out.append("<br>");
          prevSlashR = false;
        }
        out.append(ch);
        break;
      }
    }
    return out.toString();
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
