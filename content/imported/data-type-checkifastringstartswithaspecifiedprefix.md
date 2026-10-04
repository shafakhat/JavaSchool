---
title: Check if a String starts with a specified prefix.
nav: Check if a String starts w...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1167
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/CheckifaStringstartswithaspecifiedprefix.htm
---
```java title=Example.java
/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */public class Main {
  // startsWith
 //-----------------------------------------------------------------------
 /**
   *
   * <code>null</code>s are handled without exceptions. Two <code>null</code>
   * references are considered to be equal. The comparison is case sensitive.
   *
   * <pre>
   * StringUtils.startsWith(null, null)      = true
   * StringUtils.startsWith(null, "abcdef")  = false
   * StringUtils.startsWith("abc", null)     = false
   * StringUtils.startsWith("abc", "abcdef") = true
   * StringUtils.startsWith("abc", "ABCDEF") = false
   * </pre>
   *
   * @see java.lang.String#startsWith(String)
   * @param str  the String to check, may be null
   * @param prefix the prefix to find, may be null
   * @return <code>true</code> if the String starts with the prefix, case sensitive, or
   *  both <code>null</code>
   * @since 2.4
   */ public static boolean startsWith(String str, String prefix) {
      return startsWith(str, prefix, false);
  }
  /**
   * Check if a String starts with a specified prefix (optionally case insensitive).
   *
   * @see java.lang.String#startsWith(String)
   * @param str  the String to check, may be null
   * @param prefix the prefix to find, may be null
   * @param ignoreCase inidicates whether the compare should ignore case
   *  (case insensitive) or not.
   * @return <code>true</code> if the String starts with the prefix or
   *  both <code>null</code>
   */ private static boolean startsWith(String str, String prefix, boolean ignoreCase) {
      if (str == null || prefix == null) {
          return (str == null && prefix == null);
      }
      if (prefix.length() > str.length()) {
          return false;
      }
      return str.regionMatches(ignoreCase, 0, prefix, 0, prefix.length());
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
   */ public static boolean isEmpty(String str) {
      return str == null || str.length() == 0;
  }
}
```
