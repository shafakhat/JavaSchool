---
title: Swaps the case of a String changing upper and title case to lower case, and lower case to upper case.
nav: Swaps the case of a String...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1148
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/SwapsthecaseofaStringchangingupperandtitlecasetolowercaseandlowercasetouppercase.htm
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
  /**
   * Swaps the case of a String changing upper and title case to
   * lower case, and lower case to upper case.
   *
   * <ul>
   *  <li>Upper case character converts to Lower case</li>
   *  <li>Title case character converts to Lower case</li>
   *  <li>Lower case character converts to Upper case</li>
   * </ul>
   *
   * For a word based algorithm, see {@link WordUtils#swapCase(String)}.
   * A <code>null</code> input String returns <code>null</code>.
   *
   * <pre>
   * StringUtils.swapCase(null)                 = null
   * StringUtils.swapCase("")                   = ""
   * StringUtils.swapCase("The dog has a BONE") = "tHE DOG HAS A bone"
   * </pre>
   *
   * NOTE: This method changed in Lang version 2.0.
   * It no longer performs a word based algorithm.
   * If you only use ASCII, you will notice no change.
   * That functionality is available in WordUtils.
   *
   * @param str  the String to swap case, may be null
   * @return the changed String, <code>null</code> if null String input
   */ public static String swapCase(String str) {
      int strLen;
      if (str == null || (strLen = str.length()) == 0) {
          return str;
      }
      StringBuffer buffer = new StringBuffer(strLen);
      char ch = 0;
      for (int i = 0; i < strLen; i++) {
          ch = str.charAt(i);
          if (Character.isUpperCase(ch)) {
              ch = Character.toLowerCase(ch);
          } else if (Character.isTitleCase(ch)) {
              ch = Character.toLowerCase(ch);
          } else if (Character.isLowerCase(ch)) {
              ch = Character.toUpperCase(ch);
          }
          buffer.append(ch);
      }
      return buffer.toString();
  }
}
```
