---
title: Join String
nav: Join String
description: * This program is free software; you can redistribute it and/or modify
section: Imported - java2s Archive
order: 1054
source: https://web.archive.org/web/20100604102143/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/JoinString.htm
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
   * Join all the elements of a string array into a single
   * String.
   *
   * If the given array empty an empty string
   * will be returned.  Null elements of the array are allowed
   * and will be treated like empty Strings.
   *
   * @param array Array to be joined into a string.
   * @return Concatenation of all the elements of the given array.
   * @throws NullPointerException if array is null.
   *
   * @since ostermillerutils 1.05.00
   */
  public static String join(String[] array){
    return join(array, "");
  }
  /**
   * Join all the elements of a string array into a single
   * String.
   *
   * If the given array empty an empty string
   * will be returned.  Null elements of the array are allowed
   * and will be treated like empty Strings.
   *
   * @param array Array to be joined into a string.
   * @param delimiter String to place between array elements.
   * @return Concatenation of all the elements of the given array with the the delimiter in between.
   * @throws NullPointerException if array or delimiter is null.
   *
   * @since ostermillerutils 1.05.00
   */
  public static String join(String[] array, String delimiter){
    // Cache the length of the delimiter
    // has the side effect of throwing a NullPointerException if
    // the delimiter is null.
    int delimiterLength = delimiter.length();
    // Nothing in the array return empty string
    // has the side effect of throwing a NullPointerException if
    // the array is null.
    if (array.length == 0) return "";
    // Only one thing in the array, return it.
    if (array.length == 1){
      if (array[0] == null) return "";
      return array[0];
    }
    // Make a pass through and determine the size
    // of the resulting string.
    int length = 0;
    for (int i=0; i<array.length; i++){
      if (array[i] != null) length+=array[i].length();
      if (i<array.length-1) length+=delimiterLength;
    }
    // Make a second pass through and concatenate everything
    // into a string buffer.
    StringBuffer result = new StringBuffer(length);
    for (int i=0; i<array.length; i++){
      if (array[i] != null) result.append(array[i]);
      if (i<array.length-1) result.append(delimiter);
    }
    return result.toString();
  }
}
```
