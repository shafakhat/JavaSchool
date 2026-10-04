---
title: insert HTML block dynamically
nav: insert HTML block dynamica...
description: * Licensed to the Apache Software Foundation (ASF) under one
section: Imported - java2s Archive
order: 1824
source: https://web.archive.org/web/20140829092038/http://www.java2s.com/Tutorial/Java/0120__Development/insertHTMLblockdynamically.htm
---
```java title=Example.java
/*
 *  Licensed to the Apache Software Foundation (ASF) under one
 *  or more contributor license agreements.  See the NOTICE file
 *  distributed with this work for additional information
 *  regarding copyright ownership.  The ASF licenses this file
 *  to you under the Apache License, Version 2.0 (the
 *  "License"); you may not use this file except in compliance
 *  with the License.  You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing,
 *  software distributed under the License is distributed on an
 *  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 *  KIND, either express or implied.  See the License for the
 *  specific language governing permissions and limitations
 *  under the License.
 *
 */
/**
 * Various string manipulation methods that are more efficient then chaining
 * string operations: all is done in the same buffer without creating a bunch of
 * string objects.
 *
 * @author <a href="mailto:dev@labs.apache.org">Dungeon Project</a>
 */
public class Main {
  /**
   * This method is used to insert HTML block dynamically
   *
   * @param source
   *            the HTML code to be processes
   * @param replaceNl
   *            if true '\n' will be replaced by &lt;br>
   * @param replaceTag
   *            if true '<' will be replaced by &lt; and '>' will be replaced
   *            by &gt;
   * @param replaceQuote
   *            if true '\"' will be replaced by &quot;
   * @return the formated html block
   */
  public static final String formatHtml( String source, boolean replaceNl, boolean replaceTag,
      boolean replaceQuote )
  {
      StringBuffer buf = new StringBuffer();
      int len = source.length();
      for ( int ii = 0; ii < len; ii++ )
      {
          char ch = source.charAt( ii );
          switch ( ch )
          {
              case '\"':
                  if ( replaceQuote )
                  {
                      buf.append( "&quot;" );
                  }
                  else
                  {
                      buf.append( ch );
                  }
                  break;
              case '<':
                  if ( replaceTag )
                  {
                      buf.append( "&lt;" );
                  }
                  else
                  {
                      buf.append( ch );
                  }
                  break;
              case '>':
                  if ( replaceTag )
                  {
                      buf.append( "&gt;" );
                  }
                  else
                  {
                      buf.append( ch );
                  }
                  break;
              case '\n':
                  if ( replaceNl )
                  {
                      if ( replaceTag )
                      {
                          buf.append( "&lt;br&gt;" );
                      }
                      else
                      {
                          buf.append( "<br>" );
                      }
                  }
                  else
                  {
                      buf.append( ch );
                  }
                  break;
              case '\r':
                  break;
              case '&':
                  buf.append( "&amp;" );
                  break;
              default:
                  buf.append( ch );
                  break;
          }
      }
      return buf.toString();
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
