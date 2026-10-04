---
title: Left pad a String with a specified character.
nav: Left pad a String with a s...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1032
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/LeftpadaStringwithaspecifiedcharacter.htm
---
```java title=Example.java
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
 */publicclass Main {
  /**
   * The maximum size to which the padding constant(s) can expand.
   */privatestaticfinalint PAD_LIMIT = 8192;
  /**
   *
   * Pad to a size of <code>size</code>.
   *
   * <pre>
   * StringUtils.leftPad(null, *, *)     = null
   * StringUtils.leftPad("", 3, 'z')     = "zzz"
   * StringUtils.leftPad("bat", 3, 'z')  = "bat"
   * StringUtils.leftPad("bat", 5, 'z')  = "zzbat"
   * StringUtils.leftPad("bat", 1, 'z')  = "bat"
   * StringUtils.leftPad("bat", -1, 'z') = "bat"
   * </pre>
   *
   * @param str  the String to pad out, may be null
   * @param size  the size to pad to
   * @param padChar  the character to pad with
   * @return left padded String or original String if no padding is necessary,
   *  <code>null</code> if null String input
   * @since 2.0
   */publicstatic String leftPad(String str, int size, char padChar) {
      if (str == null) {
          return null;
      }
      int pads = size - str.length();
      if (pads <= 0) {
          return str; // returns original String when possible
      }
      if (pads > PAD_LIMIT) {
          return leftPad(str, size, String.valueOf(padChar));
      }
      return padding(pads, padChar).concat(str);
  }
  /**
   * Left pad a String with a specified String.
   *
   * Pad to a size of <code>size</code>.
   *
   * <pre>
   * StringUtils.leftPad(null, *, *)      = null
   * StringUtils.leftPad("", 3, "z")      = "zzz"
   * StringUtils.leftPad("bat", 3, "yz")  = "bat"
   * StringUtils.leftPad("bat", 5, "yz")  = "yzbat"
   * StringUtils.leftPad("bat", 8, "yz")  = "yzyzybat"
   * StringUtils.leftPad("bat", 1, "yz")  = "bat"
   * StringUtils.leftPad("bat", -1, "yz") = "bat"
   * StringUtils.leftPad("bat", 5, null)  = "  bat"
   * StringUtils.leftPad("bat", 5, "")    = "  bat"
   * </pre>
   *
   * @param str  the String to pad out, may be null
   * @param size  the size to pad to
   * @param padStr  the String to pad with, null or empty treated as single space
   * @return left padded String or original String if no padding is necessary,
   *  <code>null</code> if null String input
   */publicstatic String leftPad(String str, int size, String padStr) {
      if (str == null) {
          return null;
      }
      if (isEmpty(padStr)) {
          padStr = " ";
      }
      int padLen = padStr.length();
      int strLen = str.length();
      int pads = size - strLen;
      if (pads <= 0) {
          return str; // returns original String when possible
      }
      if (padLen == 1 && pads <= PAD_LIMIT) {
          return leftPad(str, size, padStr.charAt(0));
      }
      if (pads == padLen) {
          return padStr.concat(str);
      } elseif (pads < padLen) {
          return padStr.substring(0, pads).concat(str);
      } else {
          char[] padding = newchar[pads];
          char[] padChars = padStr.toCharArray();
          for (int i = 0; i < pads; i++) {
              padding[i] = padChars[i % padLen];
          }
          returnnew String(padding).concat(str);
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
   */privatestatic String padding(int repeat, char padChar) throws IndexOutOfBoundsException {
      if (repeat < 0) {
          thrownew IndexOutOfBoundsException("Cannot pad a negative amount: " + repeat);
      }
      finalchar[] buf = newchar[repeat];
      for (int i = 0; i < buf.length; i++) {
          buf[i] = padChar;
      }
      returnnew String(buf);
  }
  // Empty checks
//-----------------------------------------------------------------------
/**
   * Checks if a String is empty ("") or null.
   *
   * <pre>
   * StringUtils.isEmpty(null)      = true
   * StringUtils.isEmpty("")        = true
   * StringUtils.isEmpty(" ")       = false
   * StringUtils.isEmpty("bob")     = false
   * StringUtils.isEmpty("  bob  ") = false
   * </pre>
   *
   * NOTE: This method changed in Lang version 2.0.
   * It no longer trims the String.
   * That functionality is available in isBlank().
   *
   * @param str  the String to check, may be null
   * @return <code>true</code> if the String is empty or null
   */publicstaticboolean isEmpty(String str) {
      return str == null || str.length() == 0;
  }
}
```
