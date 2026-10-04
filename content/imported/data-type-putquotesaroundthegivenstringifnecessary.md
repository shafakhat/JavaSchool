---
title: Put quotes around the given String if necessary.
nav: Put quotes around the give...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1273
source: https://web.archive.org/web/20140829075616/http://www.java2s.com/Tutorial/Java/0040__Data-Type/PutquotesaroundthegivenStringifnecessary.htm
---
```java title=Example.java
import java.io.File;
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
 *@author <a href="mailto:siegfried.goeschl@it20one.at">Siegfried Goeschl</a>
 */
public class Main {
  private static final String SINGLE_QUOTE = "\'";
  private static final String DOUBLE_QUOTE = "\"";
  private static final char SLASH_CHAR = '/';
  private static final char BACKSLASH_CHAR = '\\';
  /**
   *
   * If the argument doesn't include spaces or quotes, return it as is. If it
   * contains double quotes, use single quotes - else surround the argument by
   * double quotes.
   *
   *
   * @param argument the argument to be quoted
   * @return the quoted argument
   * @throws IllegalArgumentException If argument contains both types of quotes
   */
  public static String quoteArgument(final String argument) {
      String cleanedArgument = argument.trim();
      while(cleanedArgument.startsWith(SINGLE_QUOTE) || cleanedArgument.startsWith(DOUBLE_QUOTE)) {
          cleanedArgument = cleanedArgument.substring(1);
      }
      while(cleanedArgument.endsWith(SINGLE_QUOTE) || cleanedArgument.endsWith(DOUBLE_QUOTE)) {
          cleanedArgument = cleanedArgument.substring(0, cleanedArgument.length() - 1);
      }
      final StringBuffer buf = new StringBuffer();
      if (cleanedArgument.indexOf(DOUBLE_QUOTE) > -1) {
          if (cleanedArgument.indexOf(SINGLE_QUOTE) > -1) {
              throw new IllegalArgumentException(
                      "Can't handle single and double quotes in same argument");
          } else {
              return buf.append(SINGLE_QUOTE).append(cleanedArgument).append(
                      SINGLE_QUOTE).toString();
          }
      } else if (cleanedArgument.indexOf(SINGLE_QUOTE) > -1
              || cleanedArgument.indexOf(" ") > -1) {
          return buf.append(DOUBLE_QUOTE).append(cleanedArgument).append(
                  DOUBLE_QUOTE).toString();
      } else {
          return cleanedArgument;
      }
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
