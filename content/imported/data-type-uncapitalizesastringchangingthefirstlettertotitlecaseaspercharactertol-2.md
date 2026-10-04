---
title: Uncapitalizes a String changing the first letter to title case as per Character.toLowerCase(char). No other letters are changed.
nav: Uncapitalizes a String cha...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1040
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/UncapitalizesaStringchangingthefirstlettertotitlecaseasperCharactertoLowerCasecharNootherlettersarechanged.htm
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
   * Uncapitalizes a String changing the first letter to title case as
   * per {@link Character#toLowerCase(char)}. No other letters are changed.
   *
   * For a word based algorithm, see {@link WordUtils#uncapitalize(String)}.
   * A <code>null</code> input String returns <code>null</code>.
   *
   * <pre>
   * StringUtils.uncapitalize(null)  = null
   * StringUtils.uncapitalize("")    = ""
   * StringUtils.uncapitalize("Cat") = "cat"
   * StringUtils.uncapitalize("CAT") = "cAT"
   * </pre>
   *
   * @param str  the String to uncapitalize, may be null
   * @return the uncapitalized String, <code>null</code> if null String input
   * @see WordUtils#uncapitalize(String)
   * @see #capitalize(String)
   * @since 2.0
   */publicstatic String uncapitalize(String str) {
      int strLen;
      if (str == null || (strLen = str.length()) == 0) {
          return str;
      }
      returnnew StringBuffer(strLen)
          .append(Character.toLowerCase(str.charAt(0)))
          .append(str.substring(1))
          .toString();
  }
}
```
