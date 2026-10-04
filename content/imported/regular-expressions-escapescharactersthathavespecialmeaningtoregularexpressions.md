---
title: Escapes characters that have special meaning to regular expressions
nav: Escapes characters that ha...
description: * This program is free software; you can redistribute it and/or modify
section: Imported - java2s Archive
order: 2234
source: https://web.archive.org/web/20140829091014/http://www.java2s.com/Tutorial/Java/0130__Regular-Expressions/Escapescharactersthathavespecialmeaningtoregularexpressions.htm
---
```java title=Example.java
/*
 * Static String formatting and query routines.
 * Copyright (C) 2001-2005 Stephen Ostermiller
 * http://ostermiller.org/contact.pl?regarding=Java+Utilities
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * See COPYING.TXT for details.
 */
import java.util.HashMap;
import java.util.regex.Pattern;
/**
 * Utilities for String formatting, manipulation, and queries.
 * More information about this class is available from <a target="_top" href=
 * "http://ostermiller.org/utils/StringHelper.html">ostermiller.org</a>.
 *
 * @author Stephen Ostermiller http://ostermiller.org/contact.pl?regarding=Java+Utilities
 * @since ostermillerutils 1.00.00
 */
public class StringHelper {
  /**
   * Escapes characters that have special meaning to
   * regular expressions
   *
   * @param s String to be escaped
   * @return escaped String
   * @throws NullPointerException if s is null.
   *
   * @since ostermillerutils 1.02.25
   */
  public static String escapeRegularExpressionLiteral(String s){
    // According to the documentation in the Pattern class:
    //
    // The backslash character ('\') serves to introduce escaped constructs,
    // as defined in the table above, as well as to quote characters that
    // otherwise would be interpreted as unescaped constructs. Thus the
    // expression \\ matches a single backslash and \{ matches a left brace.
    //
    // It is an error to use a backslash prior to any alphabetic character
    // that does not denote an escaped construct; these are reserved for future
    // extensions to the regular-expression language. A backslash may be used
    // prior to a non-alphabetic character regardless of whether that character
    // is part of an unescaped construct.
    //
    // As a result, escape everything except [0-9a-zA-Z]
    int length = s.length();
    int newLength = length;
    // first check for characters that might
    // be dangerous and calculate a length
    // of the string that has escapes.
    for (int i=0; i<length; i++){
      char c = s.charAt(i);
      if (!((c>='0' && c<='9') || (c>='A' && c<='Z') || (c>='a' && c<='z'))){
        newLength += 1;
      }
    }
    if (length == newLength){
      // nothing to escape in the string
      return s;
    }
    StringBuffer sb = new StringBuffer(newLength);
    for (int i=0; i<length; i++){
      char c = s.charAt(i);
      if (!((c>='0' && c<='9') || (c>='A' && c<='Z') || (c>='a' && c<='z'))){
        sb.append('\\');
      }
      sb.append(c);
    }
    return sb.toString();
  }
}
```

| 8.1.1. | Meta-characters predefined to match specific characters. |
|---|---|
| 8.1.2. | Meta-characters to match against certain string boundaries. |
| 8.1.3. | Regular expression languages also have character classes. |
| 8.1.4. | POSIX character classes and Java character classes |
| 8.1.5. | Java Character Class |
| 8.1.6. | Match a particular character a specified number of times. |
| 8.1.7. | Read regular expression from console |
| 8.1.8. | Regex Test Harness |
| 8.1.9. | Match Java source file and file and class name |
| 8.1.10. | Finding all words that start with an 'a' |
| 8.1.11. | Simple validation using the Pattern and Matcher objects |
| 8.1.12. | A possessive qualifier |
| 8.1.13. | Find the starting point of the second 'Bond' |
| 8.1.14. | A negative look ahead |
| 8.1.15. | A negative behind ahead |
| 8.1.16. | A positive look ahead |
| 8.1.17. | Pattern helper |
| 8.1.18. | Escapes characters that have special meaning to regular expressions |
