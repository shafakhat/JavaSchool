---
title: Case insensitive removal of a substring if it is at the begining of a source string, otherwise returns the source string.
nav: Case insensitive removal o...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1014
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Caseinsensitiveremovalofasubstringifitisatthebeginingofasourcestringotherwisereturnsthesourcestring.htm
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
 */publicclass Main {

  /**
   * Case insensitive removal of a substring if it is at the begining of a source string,
   * otherwise returns the source string.
   *
   * A <code>null</code> source string will return <code>null</code>.
   * An empty ("") source string will return the empty string.
   * A <code>null</code> search string will return the source string.
   *
   * <pre>
   * StringUtils.removeStartIgnoreCase(null, *)      = null
   * StringUtils.removeStartIgnoreCase("", *)        = ""
   * StringUtils.removeStartIgnoreCase(*, null)      = *
   * StringUtils.removeStartIgnoreCase("www.domain.com", "www.")   = "domain.com"
   * StringUtils.removeStartIgnoreCase("www.domain.com", "WWW.")   = "domain.com"
   * StringUtils.removeStartIgnoreCase("domain.com", "www.")       = "domain.com"
   * StringUtils.removeStartIgnoreCase("www.domain.com", "domain") = "www.domain.com"
   * StringUtils.removeStartIgnoreCase("abc", "")    = "abc"
   * </pre>
   *
   * @param str  the source String to search, may be null
   * @param remove  the String to search for (case insensitive) and remove, may be null
   * @return the substring with the string removed if found,
   *  <code>null</code> if null String input
   * @since 2.4
   */publicstatic String removeStartIgnoreCase(String str, String remove) {
      if (isEmpty(str) || isEmpty(remove)) {
          return str;
      }
      if (startsWithIgnoreCase(str, remove)) {
          return str.substring(remove.length());
      }
      return str;
  }

  /**
   * Case insensitive check if a String starts with a specified prefix.
   *
   * <code>null</code>s are handled without exceptions. Two <code>null</code>
   * references are considered to be equal. The comparison is case insensitive.
   *
   * <pre>
   * StringUtils.startsWithIgnoreCase(null, null)      = true
   * StringUtils.startsWithIgnoreCase(null, "abcdef")  = false
   * StringUtils.startsWithIgnoreCase("abc", null)     = false
   * StringUtils.startsWithIgnoreCase("abc", "abcdef") = true
   * StringUtils.startsWithIgnoreCase("abc", "ABCDEF") = true
   * </pre>
   *
   * @see java.lang.String#startsWith(String)
   * @param str  the String to check, may be null
   * @param prefix the prefix to find, may be null
   * @return <code>true</code> if the String starts with the prefix, case insensitive, or
   *  both <code>null</code>
   * @since 2.4
   */publicstaticboolean startsWithIgnoreCase(String str, String prefix) {
      return startsWith(str, prefix, true);
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
   */privatestaticboolean startsWith(String str, String prefix, boolean ignoreCase) {
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
   */publicstaticboolean isEmpty(String str) {
      return str == null || str.length() == 0;
  }

}
```
