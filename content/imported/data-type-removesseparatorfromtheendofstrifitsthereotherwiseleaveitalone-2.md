---
title: Removes separator from the end of str if it's there, otherwise leave it alone.
nav: Removes separator from the...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1175
source: https://web.archive.org/web/20100707054344/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/Removesseparatorfromtheendofstrifitsthereotherwiseleaveitalone.htm
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
   * Removes <code>separator</code> from the end of
   * <code>str</code> if it's there, otherwise leave it alone.
   *
   * NOTE: This method changed in version 2.0.
   * It now more closely matches Perl chomp.
   * For the previous behavior, use {@link #substringBeforeLast(String, String)}.
   * This method uses {@link String#endsWith(String)}.
   *
   * <pre>
   * StringUtils.chomp(null, *)         = null
   * StringUtils.chomp("", *)           = ""
   * StringUtils.chomp("foobar", "bar") = "foo"
   * StringUtils.chomp("foobar", "baz") = "foobar"
   * StringUtils.chomp("foo", "foo")    = ""
   * StringUtils.chomp("foo ", "foo")   = "foo "
   * StringUtils.chomp(" foo", "foo")   = " "
   * StringUtils.chomp("foo", "foooo")  = "foo"
   * StringUtils.chomp("foo", "")       = "foo"
   * StringUtils.chomp("foo", null)     = "foo"
   * </pre>
   *
   * @param str  the String to chomp from, may be null
   * @param separator  separator String, may be null
   * @return String without trailing separator, <code>null</code> if null String input
   */
  public static String chomp(String str, String separator) {
      if (isEmpty(str) || separator == null) {
          return str;
      }
      if (str.endsWith(separator)) {
          return str.substring(0, str.length() - separator.length());
      }
      return str;
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
