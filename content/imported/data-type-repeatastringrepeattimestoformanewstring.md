---
title: Repeat a String repeat times to form a new String.
nav: Repeat a String repeat tim...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1286
source: https://web.archive.org/web/20140305134459/http://www.java2s.com/Tutorial/Java/0040__Data-Type/RepeataStringrepeattimestoformanewString.htm
---
```java title=Example.java
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.SQLException;
/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 *  contributor license agreements.  See the NOTICE file distributed with
 *  this work for additional information regarding copyright ownership.
 *  The ASF licenses this file to You under the Apache License, Version 2.0
 *  (the "License"); you may not use this file except in compliance with
 *  the License.  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS,
 *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *  See the License for the specific language governing permissions and
 *  limitations under the License.
 *
 *
 */
public class Main {
  /**
   * The maximum size to which the padding constant(s) can expand.
   */
  private static final int PAD_LIMIT = 8192;
  // Padding
  //-----------------------------------------------------------------------
  /**
   * Repeat a String <code>repeat</code> times to form a
   * new String.
   *
   * <pre>
   * StringUtils.repeat(null, 2) = null
   * StringUtils.repeat("", 0)   = ""
   * StringUtils.repeat("", 2)   = ""
   * StringUtils.repeat("a", 3)  = "aaa"
   * StringUtils.repeat("ab", 2) = "abab"
   * StringUtils.repeat("a", -2) = ""
   * </pre>
   *
   * @param str  the String to repeat, may be null
   * @param repeat  number of times to repeat str, negative treated as zero
   * @return a new String consisting of the original String repeated,
   *  <code>null</code> if null String input
   */
  public static String repeat(String str, int repeat) {
      // Performance tuned for 2.0 (JDK1.4)
      if (str == null) {
          return null;
      }
      if (repeat <= 0) {
          return "";
      }
      int inputLength = str.length();
      if (repeat == 1 || inputLength == 0) {
          return str;
      }
      if (inputLength == 1 && repeat <= PAD_LIMIT) {
          return padding(repeat, str.charAt(0));
      }
      int outputLength = inputLength * repeat;
      switch (inputLength) {
          case 1 :
              char ch = str.charAt(0);
              char[] output1 = new char[outputLength];
              for (int i = repeat - 1; i >= 0; i--) {
                  output1[i] = ch;
              }
              return new String(output1);
          case 2 :
              char ch0 = str.charAt(0);
              char ch1 = str.charAt(1);
              char[] output2 = new char[outputLength];
              for (int i = repeat * 2 - 2; i >= 0; i--, i--) {
                  output2[i] = ch0;
                  output2[i + 1] = ch1;
              }
              return new String(output2);
          default :
              StringBuffer buf = new StringBuffer(outputLength);
              for (int i = 0; i < repeat; i++) {
                  buf.append(str);
              }
              return buf.toString();
      }
  }
  /**
   * Returns padding using the specified delimiter repeated
   * to a given length.
   *
   * <pre>
   * StringUtils.padding(0, 'e')  = ""
   * StringUtils.padding(3, 'e')  = "eee"
   * StringUtils.padding(-2, 'e') = IndexOutOfBoundsException
   * </pre>
   *
   * Note: this method doesn't not support padding with
   * <a href="http://www.unicode.org/glossary/#supplementary_character">Unicode Supplementary Characters</a>
   * as they require a pair of <code>char</code>s to be represented.
   * If you are needing to support full I18N of your applications
   * consider using {@link #repeat(String, int)} instead.
   *
   *
   * @param repeat  number of times to repeat delim
   * @param padChar  character to repeat
   * @return String with repeated character
   * @throws IndexOutOfBoundsException if <code>repeat &lt; 0</code>
   * @see #repeat(String, int)
   */
  private static String padding(int repeat, char padChar) throws IndexOutOfBoundsException {
      if (repeat < 0) {
          throw new IndexOutOfBoundsException("Cannot pad a negative amount: " + repeat);
      }
      final char[] buf = new char[repeat];
      for (int i = 0; i < buf.length; i++) {
          buf[i] = padChar;
      }
      return new String(buf);
  }
}
```

| 2.30.1. | Format Calendar with String.format() |
|---|---|
| 2.30.2. | Format strings into table |
| 2.30.3. | String.format(): right pad a string |
| 2.30.4. | String.format(): left pad a string |
| 2.30.5. | Format a String (JDK1.5) |
| 2.30.6. | Pass value array to String.format() |
| 2.30.7. | Remove/collapse multiple newline characters. |
| 2.30.8. | Abbreviate string |
| 2.30.9. | Capital and uncapital strings |
| 2.30.10. | Transforms words to singular, plural, humanized (human readable), underscore, camel case, or ordinal form |
| 2.30.11. | Replace New Lines |
| 2.30.12. | Fix Line Separator |
| 2.30.13. | Abbreviates a String using ellipses in both sides. |
| 2.30.14. | Abbreviates a String using ellipses. |
| 2.30.15. | Capitalize the first character of the given string |
| 2.30.16. | Centers a String in a larger String of size size using the space character (' '). |
| 2.30.17. | Centers a String in a larger String of size size. Uses a supplied String as the value to pad the String with. |
| 2.30.18. | Centers a String in a larger String of size size. Uses a supplied character as the value to pad the String with. |
| 2.30.19. | Convert string to uppercase |
| 2.30.20. | Left pad a String with a specified String. |
| 2.30.21. | Left pad a String with a specified character. |
| 2.30.22. | Left pad a String with spaces (' '). |
| 2.30.23. | Makes the first letter caps and the rest lowercase. |
| 2.30.24. | Put quotes around the given String if necessary. |
| 2.30.25. | Quote a string so that it can be used as an identifier or a string literal in SQL statements. |
| 2.30.26. | Right pad a String with a specified String. |
| 2.30.27. | Right pad a String with a specified character. |
| 2.30.28. | Right pad a String with spaces (' '). |
| 2.30.29. | Trim off trailing blanks but not leading blanks |
| 2.30.30. | Truncate a String to the given length with no warnings or error raised if it is bigger. |
| 2.30.31. | Uncapitalizes a String changing the first letter to title case as per Character.toLowerCase(char). No other letters are changed. |
| 2.30.32. | Repeat String |
| 2.30.33. | Repeat a String repeat times to form a new String. |
| 2.30.34. | Strip Line Breaks |
| 2.30.35. | Trim any of the characters |
| 2.30.36. | Removes one newline from end of a String if it's there, otherwise leave it alone. |
| 2.30.37. | Removes newline, carriage return and tab characters from a string |
| 2.30.38. | Remove the leading and trailing quotes from str. |
