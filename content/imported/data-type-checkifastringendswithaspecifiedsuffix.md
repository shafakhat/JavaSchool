---
title: Check if a String ends with a specified suffix.
nav: Check if a String ends wit...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1337
source: https://web.archive.org/web/20140829081724/http://www.java2s.com/Tutorial/Java/0040__Data-Type/CheckifaStringendswithaspecifiedsuffix.htm
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
  // endsWith
  //-----------------------------------------------------------------------
  /**
   *
   * <code>null</code>s are handled without exceptions. Two <code>null</code>
   * references are considered to be equal. The comparison is case sensitive.
   *
   * <pre>
   * StringUtils.endsWith(null, null)      = true
   * StringUtils.endsWith(null, "abcdef")  = false
   * StringUtils.endsWith("def", null)     = false
   * StringUtils.endsWith("def", "abcdef") = true
   * StringUtils.endsWith("def", "ABCDEF") = false
   * </pre>
   *
   * @see java.lang.String#endsWith(String)
   * @param str  the String to check, may be null
   * @param suffix the suffix to find, may be null
   * @return <code>true</code> if the String ends with the suffix, case sensitive, or
   *  both <code>null</code>
   * @since 2.4
   */
  public static boolean endsWith(String str, String suffix) {
      return endsWith(str, suffix, false);
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
   */
  private static boolean endsWith(String str, String suffix, boolean ignoreCase) {
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
   */
  public static boolean isEmpty(String str) {
      return str == null || str.length() == 0;
  }
}
```

| 2.31.1. | Match Phone Number |
|---|---|
| 2.31.2. | Match Zip Codes |
| 2.31.3. | Match Dates |
| 2.31.4. | Match Name Formats |
| 2.31.5. | Case insensitive check if a String ends with a specified suffix. |
| 2.31.6. | Case insensitive check if a String starts with a specified prefix. |
| 2.31.7. | Case insensitive removal of a substring if it is at the begining of a source string, otherwise returns the source string. |
| 2.31.8. | Case insensitive removal of a substring if it is at the end of a source string, otherwise returns the source string. |
| 2.31.9. | Check if a String ends with a specified suffix. |
| 2.31.10. | Check if a String starts with a specified prefix. |
| 2.31.11. | Check if a string is present at the current position in another string. |
| 2.31.12. | Check whether the given String is a valid identifier according to the Java Language specifications. |
| 2.31.13. | Checks if String contains a search String irrespective of case, handling null |
| 2.31.14. | Checks if String contains a search String, handling null |
| 2.31.15. | Checks if String contains a search character, handling null |
| 2.31.16. | Checks if a String is empty ("") or null. |
| 2.31.17. | Checks if a String is not empty ("") and not null. |
| 2.31.18. | Checks if a String is whitespace, empty ("") or null. |
| 2.31.19. | Checks if the String contains any character in the given set of characters. |
| 2.31.20. | Checks if the String contains only certain characters. |
