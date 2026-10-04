---
title: Case insensitive check if a String ends with a specified suffix.
nav: Case insensitive check if ...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1000
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/CaseinsensitivecheckifaStringendswithaspecifiedsuffix.htm
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
   *
   * <code>null</code>s are handled without exceptions. Two <code>null</code>
   * references are considered to be equal. The comparison is case insensitive.
   *
   * <pre>
   * StringUtils.endsWithIgnoreCase(null, null)      = true
   * StringUtils.endsWithIgnoreCase(null, "abcdef")  = false
   * StringUtils.endsWithIgnoreCase("def", null)     = false
   * StringUtils.endsWithIgnoreCase("def", "abcdef") = true
   * StringUtils.endsWithIgnoreCase("def", "ABCDEF") = false
   * </pre>
   *
   * @see java.lang.String#endsWith(String)
   * @param str  the String to check, may be null
   * @param suffix the suffix to find, may be null
   * @return <code>true</code> if the String ends with the suffix, case insensitive, or
   *  both <code>null</code>
   * @since 2.4
   */publicstaticboolean endsWithIgnoreCase(String str, String suffix) {
      return endsWith(str, suffix, true);
  }
  /**
   * Check if a String ends with a specified suffix (optionally case insensitive).
   *
   * @see java.lang.String#endsWith(String)
   * @param str  the String to check, may be null
   * @param suffix the suffix to find, may be null
   * @param ignoreCase inidicates whether the compare should ignore case
   *  (case insensitive) or not.
   * @return <code>true</code> if the String starts with the prefix or
   *  both <code>null</code>
   */privatestaticboolean endsWith(String str, String suffix, boolean ignoreCase) {
      if (str == null || suffix == null) {
          return (str == null && suffix == null);
      }
      if (suffix.length() > str.length()) {
          return false;
      }
      int strOffset = str.length() - suffix.length();
      return str.regionMatches(ignoreCase, strOffset, suffix, 0, suffix.length());
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
