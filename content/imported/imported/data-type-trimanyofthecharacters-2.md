---
title: Trim any of the characters
nav: Trim any of the characters
description: * This program is free software; you can redistribute it and/or modify
section: Imported - java2s Archive
order: 1007
source: https://web.archive.org/web/20100412211327/http://java2s.com:80/Tutorial/Java/0040__Data-Type/Trimanyofthecharacters.htm
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
