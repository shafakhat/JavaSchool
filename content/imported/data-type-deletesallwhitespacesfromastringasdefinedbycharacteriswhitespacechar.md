---
title: Deletes all whitespaces from a String as defined by Character.isWhitespace(char).
nav: Deletes all whitespaces fr...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1014
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/DeletesallwhitespacesfromaStringasdefinedbyCharacterisWhitespacechar.htm
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
   * Deletes all whitespaces from a String as defined by
   * {@link Character#isWhitespace(char)}.
   *
   * <pre>
   * StringUtils.deleteWhitespace(null)         = null
   * StringUtils.deleteWhitespace("")           = ""
   * StringUtils.deleteWhitespace("abc")        = "abc"
   * StringUtils.deleteWhitespace("   ab  c  ") = "abc"
   * </pre>
   *
   * @param str  the String to delete whitespace from, may be null
   * @return the String without whitespaces, <code>null</code> if null String input
   */publicstatic String deleteWhitespace(String str) {
      if (isEmpty(str)) {
          return str;
      }
      int sz = str.length();
      char[] chs = newchar[sz];
      int count = 0;
      for (int i = 0; i < sz; i++) {
          if (!Character.isWhitespace(str.charAt(i))) {
              chs[count++] = str.charAt(i);
          }
      }
      if (count == sz) {
          return str;
      }
      returnnew String(chs, 0, count);
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
