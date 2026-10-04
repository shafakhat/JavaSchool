---
title: Pad string
nav: Pad string
description: * This program is free software; you can redistribute it and/or modify
section: Imported - java2s Archive
order: 1092
source: https://web.archive.org/web/20140829080842/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Padstring.htm
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
   * Pad the beginning of the given String with spaces until
   * the String is of the given length.
   *
   * If a String is longer than the desired length,
   * it will not be truncated, however no padding
   * will be added.
   *
   * @param s String to be padded.
   * @param length desired length of result.
   * @return padded String.
   * @throws NullPointerException if s is null.
   *
   * @since ostermillerutils 1.00.00
   */
  public static String prepad(String s, int length){
    return prepad(s, length, ' ');
  }
  /**
   * Pre-pend the given character to the String until
   * the result is the desired length.
   *
   * If a String is longer than the desired length,
   * it will not be truncated, however no padding
   * will be added.
   *
   * @param s String to be padded.
   * @param length desired length of result.
   * @param c padding character.
   * @return padded String.
   * @throws NullPointerException if s is null.
   *
   * @since ostermillerutils 1.00.00
   */
  public static String prepad(String s, int length, char c){
    int needed = length - s.length();
    if (needed <= 0){
      return s;
    }
    char padding[] = new char[needed];
    java.util.Arrays.fill(padding, c);
    StringBuffer sb = new StringBuffer(length);
    sb.append(padding);
    sb.append(s);
    return sb.toString();
  }
  /**
   * Pad the end of the given String with spaces until
   * the String is of the given length.
   *
   * If a String is longer than the desired length,
   * it will not be truncated, however no padding
   * will be added.
   *
   * @param s String to be padded.
   * @param length desired length of result.
   * @return padded String.
   * @throws NullPointerException if s is null.
   *
   * @since ostermillerutils 1.00.00
   */
  public static String postpad(String s, int length){
    return postpad(s, length, ' ');
  }
  /**
   * Append the given character to the String until
   * the result is  the desired length.
   *
   * If a String is longer than the desired length,
   * it will not be truncated, however no padding
   * will be added.
   *
   * @param s String to be padded.
   * @param length desired length of result.
   * @param c padding character.
   * @return padded String.
   * @throws NullPointerException if s is null.
   *
   * @since ostermillerutils 1.00.00
   */
  public static String postpad(String s, int length, char c){
    int needed = length - s.length();
    if (needed <= 0){
      return s;
    }
    char padding[] = new char[needed];
    java.util.Arrays.fill(padding, c);
    StringBuffer sb = new StringBuffer(length);
    sb.append(s);
    sb.append(padding);
    return sb.toString();
  }
  /**
   * Pad the beginning and end of the given String with spaces until
   * the String is of the given length.  The result is that the original
   * String is centered in the middle of the new string.
   *
   * If the number of characters to pad is even, then the padding
   * will be split evenly between the beginning and end, otherwise,
   * the extra character will be added to the end.
   *
   * If a String is longer than the desired length,
   * it will not be truncated, however no padding
   * will be added.
   *
   * @param s String to be padded.
   * @param length desired length of result.
   * @return padded String.
   * @throws NullPointerException if s is null.
   *
   * @since ostermillerutils 1.00.00
   */
  public static String midpad(String s, int length){
    return midpad(s, length, ' ');
  }
  /**
   * Pad the beginning and end of the given String with the given character
   * until the result is  the desired length.  The result is that the original
   * String is centered in the middle of the new string.
   *
   * If the number of characters to pad is even, then the padding
   * will be split evenly between the beginning and end, otherwise,
   * the extra character will be added to the end.
   *
   * If a String is longer than the desired length,
   * it will not be truncated, however no padding
   * will be added.
   *
   * @param s String to be padded.
   * @param length desired length of result.
   * @param c padding character.
   * @return padded String.
   * @throws NullPointerException if s is null.
   *
   * @since ostermillerutils 1.00.00
   */
  public static String midpad(String s, int length, char c){
    int needed = length - s.length();
    if (needed <= 0){
      return s;
    }
    int beginning = needed / 2;
    int end = beginning + needed % 2;
    char prepadding[] = new char[beginning];
    java.util.Arrays.fill(prepadding, c);
    char postpadding[] = new char[end];
    java.util.Arrays.fill(postpadding, c);
    StringBuffer sb = new StringBuffer(length);
    sb.append(prepadding);
    sb.append(s);
    sb.append(postpadding);
    return sb.toString();
  }
}
```
