---
title: Removes a substring only if it is at the end of a source string, otherwise returns the source string.
nav: Removes a substring only i...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1081
source: https://web.archive.org/web/20100606070851/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/Removesasubstringonlyifitisattheendofasourcestringotherwisereturnsthesourcestring.htm
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
 */
public class Main {
  /**
   * Removes a substring only if it is at the end of a source string,
   * otherwise returns the source string.
   *
   * A <code>null</code> source string will return <code>null</code>.
   * An empty ("") source string will return the empty string.
   * A <code>null</code> search string will return the source string.
   *
   * <pre>
   * StringUtils.removeEnd(null, *)      = null
   * StringUtils.removeEnd("", *)        = ""
   * StringUtils.removeEnd(*, null)      = *
   * StringUtils.removeEnd("www.domain.com", ".com.")  = "www.domain.com"
   * StringUtils.removeEnd("www.domain.com", ".com")   = "www.domain"
   * StringUtils.removeEnd("www.domain.com", "domain") = "www.domain.com"
   * StringUtils.removeEnd("abc", "")    = "abc"
   * </pre>
   *
   * @param str  the source String to search, may be null
   * @param remove  the String to search for and remove, may be null
   * @return the substring with the string removed if found,
   *  <code>null</code> if null String input
   * @since 2.1
   */
  public static String removeEnd(String str, String remove) {
      if (isEmpty(str) || isEmpty(remove)) {
          return str;
      }
      if (str.endsWith(remove)) {
          return str.substring(0, str.length() - remove.length());
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
