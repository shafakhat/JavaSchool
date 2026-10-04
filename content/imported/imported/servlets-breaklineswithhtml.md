---
title: break Lines with HTML
nav: break Lines with HTML
description: public static final String breakLinesHTML(String s, int width) {
section: Imported - java2s Archive
order: 1009
source: https://web.archive.org/web/20091006130310/http://www.java2s.com:80/Code/Java/Servlets/breakLineswithHTML.htm
---
```java title=Example.java
/**
 * @author matthew_hicks
 */
public class Utils {
  public static final String breakLinesHTML(String s, int width) {
    if (s == null) return null;
    StringBuffer buffer = new StringBuffer();
    buffer.append("<html><body><font face=\"Arial\" size=\"-1\">");
    int p = 0;
    char c;
    for (int i = 0; i < s.length(); i++) {
      c = s.charAt(i);
      if (((p >= width) && (c == ' '))||(c == '\n')) {
        buffer.append("<br>");
        p = 0;
      } else {
        buffer.append(c);
      }
      p++;
    }
    buffer.append("</font></body></html>");
    return buffer.toString();
  }
}
```

1.  Servlet Output HTML Demo
---  ---
2.  Servlet Display Static HTML
3.  Prints a conversion table of miles per gallon to kilometers per liter
4.  Servlet: Print Table
5.  Html utilities
6.  Html Parse Servlet
7.  Escape and unescape string
8.  Escapes newlines, tabs, backslashes, and quotes in the specified string
9.  Web Calendar
10.  HTML Helper
11.  Escape HTML
12.  Convert HTML to text
13.  Text To HTML
14.  Unescape HTML
15.  Java object representations of the HTML table structure
16.  Entity Decoder
17.  Format a color to HTML RGB color format (e.g. #FF0000 for Color.red)
18.  Definitions of HTML character entities and conversions between unicode characters and HTML character entities
19.  Encode special characters and do formatting for HTML output
20.  HTML color names
21.  Utility methods for dealing with HTML
22.  Filter the specified message string for characters that are sensitive in HTML
23.  A collection of all character entites defined in the HTML4 standard.
24.  Decode an HTML color string like '#F567BA;' into a Color
25.  Normalize Post Data
26.  Get HTML Color String from Java Color object
27.  HTML Decoder
28.  HTML Parser
29.  HTML color and Java Color
30.  HTML form Utilites
31.  Html Dimensions
32.  insert HTML block dynamically
33.  Convert an integer to an HTML RGB value
34.  Convert to HTML string
