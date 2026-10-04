---
title: Convert to HTML string
nav: Convert to HTML string
description: * soapUI is free software; you can redistribute it and/or modify it under the
section: Imported - java2s Archive
order: 1026
source: https://web.archive.org/web/20091006231101/http://www.java2s.com:80/Code/Java/Servlets/ConverttoHTMLstring.htm
---
Convert to HTML string

```java title=Example.java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.StringReader;
/*
 *  soapUI, copyright (C) 2004-2009 eviware.com
 *
 *  soapUI is free software; you can redistribute it and/or modify it under the
 *  terms of version 2.1 of the GNU Lesser General Public License as published by
 *  the Free Software Foundation.
 *
 *  soapUI is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
 *  even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 *  See the GNU Lesser General Public License for more details at gnu.org.
 */
public class Utils {
  public static String toHtml( String string )
  {
    if( StringUtils.isNullOrEmpty( string ) )
      return "<html><body></body></html>";
    BufferedReader st = new BufferedReader( new StringReader( string ) );
    StringBuffer buf = new StringBuffer( "<html><body>" );
    try
    {
      String str = st.readLine();
      while( str != null )
      {
        if( str.equalsIgnoreCase( "<br/>" ) )
        {
          str = "<br>";
        }
        buf.append( str );
        if( !str.equalsIgnoreCase( "<br>" ) )
        {
          buf.append( "<br>" );
        }
        str = st.readLine();
      }
    }
    catch( IOException e )
    {
      e.printStackTrace();
    }
    buf.append( "</body></html>" );
    string = buf.toString();
    return string;
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
32.  break Lines with HTML
33.  insert HTML block dynamically
34.  Convert an integer to an HTML RGB value
