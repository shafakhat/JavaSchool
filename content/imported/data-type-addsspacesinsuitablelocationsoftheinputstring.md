---
title: Adds spaces in suitable locations of the input string
nav: Adds spaces in suitable lo...
description: * Adds spaces in suitable locations of the input string. This is
section: Imported - java2s Archive
order: 1119
source: https://web.archive.org/web/20100214083500/http://java2s.com/Code/Java/Data-Type/Addsspacesinsuitablelocationsoftheinputstring.htm
---
Adds spaces in suitable locations of the input string

```java title=Example.java
/*
    JSPWiki - a JSP-based WikiWiki clone.
    Licensed to the Apache Software Foundation (ASF) under one
    or more contributor license agreements.  See the NOTICE file
    distributed with this work for additional information
    regarding copyright ownership.  The ASF licenses this file
    to you under the Apache License, Version 2.0 (the
    "License"); you may not use this file except in compliance
    with the License.  You may obtain a copy of the License at
       http://www.apache.org/licenses/LICENSE-2.0
    Unless required by applicable law or agreed to in writing,
    software distributed under the License is distributed on an
    "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
    KIND, either express or implied.  See the License for the
    specific language governing permissions and limitations
    under the License.
 */
import java.security.SecureRandom;
import java.util.Properties;
import java.util.Random;
public class StringUtils
{
  private static final int EOI   = 0;
  private static final int LOWER = 1;
  private static final int UPPER = 2;
  private static final int DIGIT = 3;
  private static final int OTHER = 4;
  private static int getCharKind(int c)
  {
      if (c==-1)
      {
          return EOI;
      }
      char ch = (char) c;
      if (Character.isLowerCase(ch))
          return LOWER;
      else if (Character.isUpperCase(ch))
          return UPPER;
      else if (Character.isDigit(ch))
          return DIGIT;
      else
          return OTHER;
  }
  /**
   *  Adds spaces in suitable locations of the input string.  This is
   *  used to transform a WikiName into a more readable format.
   *
   *  @param s String to be beautified.
   *  @return A beautified string.
   */
  public static String beautifyString( String s )
  {
      return beautifyString( s, " " );
  }
  /**
   *  Adds spaces in suitable locations of the input string.  This is
   *  used to transform a WikiName into a more readable format.
   *
   *  @param s String to be beautified.
   *  @param space Use this string for the space character.
   *  @return A beautified string.
   *  @since 2.1.127
   */
  public static String beautifyString( String s, String space )
  {
      StringBuffer result = new StringBuffer();
      if( s == null || s.length() == 0 ) return "";
      int cur     = s.charAt(0);
      int curKind = getCharKind(cur);
      int prevKind = LOWER;
      int nextKind = -1;
      int next = -1;
      int nextPos = 1;
      while( curKind != EOI )
      {
          next = (nextPos < s.length()) ? s.charAt(nextPos++) : -1;
          nextKind = getCharKind( next );
          if( (prevKind == UPPER) && (curKind == UPPER) && (nextKind == LOWER) )
          {
              result.append(space);
              result.append((char) cur);
          }
          else
          {
              result.append((char) cur);
              if( ( (curKind == UPPER) && (nextKind == DIGIT) )
                  || ( (curKind == LOWER) && ((nextKind == DIGIT) || (nextKind == UPPER)) )
                  || ( (curKind == DIGIT) && ((nextKind == UPPER) || (nextKind == LOWER)) ))
              {
                  result.append(space);
              }
          }
          prevKind = curKind;
          cur      = next;
          curKind  = nextKind;
      }
      return result.toString();
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
