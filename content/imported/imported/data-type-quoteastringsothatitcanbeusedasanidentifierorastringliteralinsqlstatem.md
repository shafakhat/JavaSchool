---
title: Quote a string so that it can be used as an identifier or a string literal in SQL statements.
nav: Quote a string so that it ...
description: Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1076
source: https://web.archive.org/web/20100412211322/http://java2s.com:80/Tutorial/Java/0040__Data-Type/QuoteastringsothatitcanbeusedasanidentifierorastringliteralinSQLstatements.htm
---
```java title=Example.java
import java.io.IOException;
import java.io.InputStream;
import java.util.Enumeration;
import java.util.Properties;
/*
   Derby - Class org.apache.derby.iapi.util.PropertyUtil
   Licensed to the Apache Software Foundation (ASF) under one or more
   contributor license agreements.  See the NOTICE file distributed with
   this work for additional information regarding copyright ownership.
   The ASF licenses this file to you under the Apache License, Version 2.0
   (the "License"); you may not use this file except in compliance with
   the License.  You may obtain a copy of the License at
      http://www.apache.org/licenses/LICENSE-2.0
   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
 */
public class Main {
  /**
   * Quote a string so that it can be used as an identifier or a string
   * literal in SQL statements. Identifiers are surrounded by double quotes
   * and string literals are surrounded by single quotes. If the string
   * contains quote characters, they are escaped.
   *
   * @param source the string to quote
   * @param quote the character to quote the string with (' or &quot;)
   * @return a string quoted with the specified quote character
   * @see #quoteStringLiteral(String)
   * @see IdUtil#normalToDelimited(String)
   */
  static String quoteString(String source, char quote) {
      // Normally, the quoted string is two characters longer than the source
      // string (because of start quote and end quote).
      StringBuffer quoted = new StringBuffer(source.length() + 2);
      quoted.append(quote);
      for (int i = 0; i < source.length(); i++) {
          char c = source.charAt(i);
          // if the character is a quote, escape it with an extra quote
          if (c == quote) quoted.append(quote);
          quoted.append(c);
      }
      quoted.append(quote);
      return quoted.toString();
  }
  /**
   * Quote a string so that it can be used as a string literal in an
   * SQL statement.
   *
   * @param string the string to quote
   * @return the string surrounded by single quotes and with proper escaping
   * of any single quotes inside the string
   */
  public static String quoteStringLiteral(String string) {
      return quoteString(string, '\'');
  }
}
```
