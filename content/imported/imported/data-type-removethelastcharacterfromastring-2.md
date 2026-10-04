---
title: Remove the last character from a String.
nav: Remove the last character ...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1176
source: https://web.archive.org/web/20100704044542/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/RemovethelastcharacterfromaString.htm
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
   * <code>\u000a</code> linefeed LF ('\n').
   *
   * @see <a href="http://java.sun.com/docs/books/jls/third_edition/html/lexical.html#101089">JLF: Escape Sequences
   *      for Character and String Literals</a>
   * @since 2.2
   */
  public static final char LF = '\n';
  /**
   * <code>\u000d</code> carriage return CR ('\r').
   *
   * @see <a href="http://java.sun.com/docs/books/jls/third_edition/html/lexical.html#101089">JLF: Escape Sequences
   *      for Character and String Literals</a>
   * @since 2.2
   */
  public static final char CR = '\r';
  // Chopping
  //-----------------------------------------------------------------------
  /**
   * Remove the last character from a String.
   *
   * If the String ends in <code>\r\n</code>, then remove both
   * of them.
   *
   * <pre>
   * StringUtils.chop(null)          = null
   * StringUtils.chop("")            = ""
   * StringUtils.chop("abc \r")      = "abc "
   * StringUtils.chop("abc\n")       = "abc"
   * StringUtils.chop("abc\r\n")     = "abc"
   * StringUtils.chop("abc")         = "ab"
   * StringUtils.chop("abc\nabc")    = "abc\nab"
   * StringUtils.chop("a")           = ""
   * StringUtils.chop("\r")          = ""
   * StringUtils.chop("\n")          = ""
   * StringUtils.chop("\r\n")        = ""
   * </pre>
   *
   * @param str  the String to chop last character from, may be null
   * @return String without last character, <code>null</code> if null String input
   */
  public static String chop(String str) {
      if (str == null) {
          return null;
      }
      int strLen = str.length();
      if (strLen < 2) {
          return "";
      }
      int lastIdx = strLen - 1;
      String ret = str.substring(0, lastIdx);
      char last = str.charAt(lastIdx);
      if (last == LF) {
          if (ret.charAt(lastIdx - 1) == CR) {
              return ret.substring(0, lastIdx - 1);
          }
      }
      return ret;
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
   */
  public static boolean isEmpty(String str) {
      return str == null || str.length() == 0;
  }
}
```
