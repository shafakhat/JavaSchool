---
title: Abbreviates a String using ellipses.
nav: Abbreviates a String using...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1104
source: https://web.archive.org/web/20100214082950/http://java2s.com/Code/Java/Data-Type/AbbreviatesaStringusingellipses.htm
---
```java title=Example.java
/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
public class Main {
  // Abbreviating
  //-----------------------------------------------------------------------
  /**
   * <p>Abbreviates a String using ellipses. This will turn
   * "Now is the time for all good men" into "Now is the time for..."</p>
   *
   * <p>Specifically:
   * <ul>
   *   <li>If <code>str</code> is less than <code>maxWidth</code> characters
   *       long, return it.</li>
   *   <li>Else abbreviate it to <code>(substring(str, 0, max-3) + "...")</code>.</li>
   *   <li>If <code>maxWidth</code> is less than <code>4</code>, throw an
   *       <code>IllegalArgumentException</code>.</li>
   *   <li>In no case will it return a String of length greater than
   *       <code>maxWidth</code>.</li>
   * </ul>
   * </p>
   *
   * <pre>
   * StringUtils.abbreviate(null, *)      = null
   * StringUtils.abbreviate("", 4)        = ""
   * StringUtils.abbreviate("abcdefg", 6) = "abc..."
   * StringUtils.abbreviate("abcdefg", 7) = "abcdefg"
   * StringUtils.abbreviate("abcdefg", 8) = "abcdefg"
   * StringUtils.abbreviate("abcdefg", 4) = "a..."
   * StringUtils.abbreviate("abcdefg", 3) = IllegalArgumentException
   * </pre>
   *
   * @param str  the String to check, may be null
   * @param maxWidth  maximum length of result String, must be at least 4
   * @return abbreviated String, <code>null</code> if null String input
   * @throws IllegalArgumentException if the width is too small
   * @since 2.0
   */
  public static String abbreviate(String str, int maxWidth) {
      return abbreviate(str, 0, maxWidth);
  }
  /**
   * <p>Abbreviates a String using ellipses. This will turn
   * "Now is the time for all good men" into "...is the time for..."</p>
   *
   * <p>Works like <code>abbreviate(String, int)</code>, but allows you to specify
   * a "left edge" offset.  Note that this left edge is not necessarily going to
   * be the leftmost character in the result, or the first character following the
   * ellipses, but it will appear somewhere in the result.
   *
   * <p>In no case will it return a String of length greater than
   * <code>maxWidth</code>.</p>
   *
   * <pre>
   * StringUtils.abbreviate(null, *, *)                = null
   * StringUtils.abbreviate("", 0, 4)                  = ""
   * StringUtils.abbreviate("abcdefghijklmno", -1, 10) = "abcdefg..."
   * StringUtils.abbreviate("abcdefghijklmno", 0, 10)  = "abcdefg..."
   * StringUtils.abbreviate("abcdefghijklmno", 1, 10)  = "abcdefg..."
   * StringUtils.abbreviate("abcdefghijklmno", 4, 10)  = "abcdefg..."
   * StringUtils.abbreviate("abcdefghijklmno", 5, 10)  = "...fghi..."
   * StringUtils.abbreviate("abcdefghijklmno", 6, 10)  = "...ghij..."
   * StringUtils.abbreviate("abcdefghijklmno", 8, 10)  = "...ijklmno"
   * StringUtils.abbreviate("abcdefghijklmno", 10, 10) = "...ijklmno"
   * StringUtils.abbreviate("abcdefghijklmno", 12, 10) = "...ijklmno"
   * StringUtils.abbreviate("abcdefghij", 0, 3)        = IllegalArgumentException
   * StringUtils.abbreviate("abcdefghij", 5, 6)        = IllegalArgumentException
   * </pre>
   *
   * @param str  the String to check, may be null
   * @param offset  left edge of source String
   * @param maxWidth  maximum length of result String, must be at least 4
   * @return abbreviated String, <code>null</code> if null String input
   * @throws IllegalArgumentException if the width is too small
   * @since 2.0
   */
  public static String abbreviate(String str, int offset, int maxWidth) {
      if (str == null) {
          return null;
      }
      if (maxWidth < 4) {
          throw new IllegalArgumentException("Minimum abbreviation width is 4");
      }
      if (str.length() <= maxWidth) {
          return str;
      }
      if (offset > str.length()) {
          offset = str.length();
      }
      if ((str.length() - offset) < (maxWidth - 3)) {
          offset = str.length() - (maxWidth - 3);
      }
      if (offset <= 4) {
          return str.substring(0, maxWidth - 3) + "...";
      }
      if (maxWidth < 7) {
          throw new IllegalArgumentException("Minimum abbreviation width with offset is 7");
      }
      if ((offset + (maxWidth - 3)) < str.length()) {
          return "..." + abbreviate(str.substring(offset), maxWidth - 3);
      }
      return "..." + str.substring(str.length() - (maxWidth - 3));
  }
}
```

1.  Fmt - format text (like Berkeley UNIX fmt)
---  ---
2.  Demonstrate some usage patterns and format-code examples of the Formatter
3.  String.format(): right pad a string
4.  String.format(): left pad a string
5.  Format a String (JDK1.5)
6.  Pass value array to String.format()
7.  Format Calendar with String.format()
8.  Abbreviates a String using ellipses in both sides.
9.  Abbreviate string
10.  Word Wrap
11.  Centers a String in a larger String of size size using the space character (' ').
12.  Centers a String in a larger String of size size. Uses a supplied String as the value to pad the String with.
13.  Centers a String in a larger String of size size. Uses a supplied character as the value to pad the String with.
14.  Capitalize the first character of the given string
15.  Capitalize the first letter but leave the rest as they are.
16.  Capitalizes a String changing the first letter to title case as Character.toTitleCase(char). No other letters are changed.
17.  Format strings into table
18.  Center the contents of the string.
19.  Truncate the supplied string to be no more than the specified length.
20.  Replace, remove, format strings
21.  Adds spaces in suitable locations of the input string
22.  Blank string: empty or white space
23.  Capital and uncapital strings
24.  Capitalizes the first character of the given string
25.  Utilities for String formatting, manipulation, and queries
26.  Fast lower case conversion
27.  Format a percentage for presentation to the user
28.  Left justify the contents of the string, ensuring that the supplied string begins at the first character and that the resulting string is of the desired length.
29.  Transforms words to singular, plural, humanized (human readable), underscore, camel case, or ordinal form
30.  Escapes all necessary characters in the String so that it can be used in SQL
31.  Escapes all necessary characters in the String so that it can be used in an XML doc
32.  Adds zeros to the beginning of a value so that the total length matches the given precision, otherwise trims the right digits.
33.  Right justify string, ensuring that the string ends at the last character
34.  Makes the first letter caps and the rest lowercase.
35.  Quote a string so that it can be used as an identifier or a string literal in SQL statements.
36.  Remove the hyphens from the begining of str and return the new String.
37.  Swaps the case of a String changing upper and title case to lower case, and lower case to upper case.
38.  Uncapitalizes a String changing the first letter to title case as per Character.toLowerCase(char). No other letters are changed.
39.  Capitlize each word in a string (journal titles, etc)
40.  Uncapitalize String
41.  Utility inserts a space before every caps in a string
42.  convert String array To Comma Delimited
43.  Constructs a method name from element's bean name for a given prefix
44.  break Lines
45.  Limit the string to a certain number of characters, adding "..." if it was truncated
