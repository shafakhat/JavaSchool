---
title: Convert to HTML string
nav: Convert to HTML string
description: * soapUI is free software; you can redistribute it and/or modify it under the
section: Imported - java2s Archive
order: 1819
source: https://web.archive.org/web/20140217213734/http://www.java2s.com/Tutorial/Java/0120__Development/ConverttoHTMLstring.htm
---
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
