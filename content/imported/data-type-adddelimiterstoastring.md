---
title: Add delimiters to a string.
nav: Add delimiters to a string.
description: * the character will be escaped by repeating the delimitter character.
section: Imported - java2s Archive
order: 1109
source: https://web.archive.org/web/20111125121433/http://java2s.com/Code/Java/Data-Type/Adddelimiterstoastring.htm
---
Add delimiters to a string.

```java title=Example.java
/**
 * This software is provided as IS by Antilia-Soft SL.
 * Copyright 2006-2007.
 */
//package com.antilia.common.util;
public class StringUtils {
  /**
   * Add delimiters to a string.
   * If the string itself contains the delimiter character,
   * the character will be escaped by repeating the delimitter character.
   *
   * @return The delimited String
   * @param str The String to delimit
   * @param delimiter
   */
  public static String delimit(String str, char delimiter) {
    if (delimiter == 0)
      return (str);
    StringBuffer buffer = new StringBuffer();
    buffer.append(delimiter);
    if (str != null) {
      for (int i = 0; i < str.length(); i++) {
        if (str.charAt(i) == delimiter)
          buffer.append(delimiter);
        buffer.append(str.charAt(i));
      }
    }
    buffer.append(delimiter);
    return (buffer.toString());
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
9.  Abbreviates a String using ellipses.
10.  Abbreviate string
11.  Word Wrap
12.  Centers a String in a larger String of size size using the space character (' ').
13.  Centers a String in a larger String of size size. Uses a supplied String as the value to pad the String with.
14.  Centers a String in a larger String of size size. Uses a supplied character as the value to pad the String with.
15.  Capitalize the first character of the given string
16.  Capitalize the first letter but leave the rest as they are.
17.  Capitalizes a String changing the first letter to title case as Character.toTitleCase(char). No other letters are changed.
18.  Format strings into table
19.  Center the contents of the string.
20.  Truncate the supplied string to be no more than the specified length.
21.  Replace, remove, format strings
22.  Adds spaces in suitable locations of the input string
23.  Blank string: empty or white space
24.  Capital and uncapital strings
25.  Capitalizes the first character of the given string
26.  Utilities for String formatting, manipulation, and queries
27.  Fast lower case conversion
28.  Format a percentage for presentation to the user
29.  Left justify the contents of the string, ensuring that the supplied string begins at the first character and that the resulting string is of the desired length.
30.  Transforms words to singular, plural, humanized (human readable), underscore, camel case, or ordinal form
31.  Escapes all necessary characters in the String so that it can be used in SQL
32.  Escapes all necessary characters in the String so that it can be used in an XML doc
33.  Adds zeros to the beginning of a value so that the total length matches the given precision, otherwise trims the right digits.
34.  Right justify string, ensuring that the string ends at the last character
35.  Makes the first letter caps and the rest lowercase.
36.  Quote a string so that it can be used as an identifier or a string literal in SQL statements.
37.  Remove the hyphens from the begining of str and return the new String.
38.  Swaps the case of a String changing upper and title case to lower case, and lower case to upper case.
39.  Uncapitalizes a String changing the first letter to title case as per Character.toLowerCase(char). No other letters are changed.
40.  Capitlize each word in a string (journal titles, etc)
41.  Uncapitalize String
42.  Utility inserts a space before every caps in a string
43.  convert String array To Comma Delimited
44.  Constructs a method name from element's bean name for a given prefix
45.  break Lines
46.  Limit the string to a certain number of characters, adding "..." if it was truncated
47.  Capicalizes the first letter of a string
48.  Get Truncated String
49.  Convert to $(Dollars) string
50.  Convert string to multiline
51.  Deletes all whitespace from a String.
52.  Trim string from left or right
53.  implode and explode string
54.  To Upper Case First Char
55.  Left trim and right trim
56.  capitalize and uncapitalize
