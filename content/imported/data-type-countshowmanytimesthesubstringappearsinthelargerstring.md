---
title: Counts how many times the substring appears in the larger String.
nav: Counts how many times the ...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1067
source: https://web.archive.org/web/20100120070745/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/CountshowmanytimesthesubstringappearsinthelargerString.htm
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
  //-----------------------------------------------------------------------
  /**
   *
   * A <code>null</code> or empty ("") String input returns <code>0</code>.
   *
   * <pre>
   * StringUtils.countMatches(null, *)       = 0
   * StringUtils.countMatches("", *)         = 0
   * StringUtils.countMatches("abba", null)  = 0
   * StringUtils.countMatches("abba", "")    = 0
   * StringUtils.countMatches("abba", "a")   = 2
   * StringUtils.countMatches("abba", "ab")  = 1
   * StringUtils.countMatches("abba", "xxx") = 0
   * </pre>
   *
   * @param str  the String to check, may be null
   * @param sub  the substring to count, may be null
   * @return the number of occurrences, 0 if either String is <code>null</code>
   */
  public static int countMatches(String str, String sub) {
      if (isEmpty(str) || isEmpty(sub)) {
          return 0;
      }
      int count = 0;
      int idx = 0;
      while ((idx = str.indexOf(sub, idx)) != -1) {
          count++;
          idx += sub.length();
      }
      return count;
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
