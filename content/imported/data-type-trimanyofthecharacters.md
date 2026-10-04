---
title: Trim any of the characters
nav: Trim any of the characters
description: * This program is free software; you can redistribute it and/or modify
section: Imported - java2s Archive
order: 1357
source: https://web.archive.org/web/20140407035416/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Trimanyofthecharacters.htm
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
   * Trim any of the characters contained in the second
   * string from the beginning and end of the first.
   *
   * @param s String to be trimmed.
   * @param c list of characters to trim from s.
   * @return trimmed String.
   * @throws NullPointerException if s is null.
   *
   * @since ostermillerutils 1.00.00
   */
  public static String trim(String s, String c){
    int length = s.length();
    if (c == null){
      return s;
    }
    int cLength = c.length();
    if (c.length() == 0){
      return s;
    }
    int start = 0;
    int end = length;
    boolean found; // trim-able character found.
    int i;
    // Start from the beginning and find the
    // first non-trim-able character.
    found = false;
    for (i=0; !found && i<length; i++){
      char ch = s.charAt(i);
      found = true;
      for (int j=0; found && j<cLength; j++){
        if (c.charAt(j) == ch) found = false;
      }
    }
    // if all characters are trim-able.
    if (!found) return "";
    start = i-1;
    // Start from the end and find the
    // last non-trim-able character.
    found = false;
    for (i=length-1; !found && i>=0; i--){
      char ch = s.charAt(i);
      found = true;
      for (int j=0; found && j<cLength; j++){
        if (c.charAt(j) == ch) found = false;
      }
    }
    end = i+2;
    return s.substring(start, end);
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
