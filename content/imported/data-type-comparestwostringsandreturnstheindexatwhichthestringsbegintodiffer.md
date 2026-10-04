---
title: Compares two Strings, and returns the index at which the Strings begin to differ.
nav: Compares two Strings, and ...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1009
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ComparestwoStringsandreturnstheindexatwhichtheStringsbegintodiffer.htm
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
   * Compares two Strings, and returns the index at which the
   * Strings begin to differ.
   *
   * For example,
   * <code>indexOfDifference("i am a machine", "i am a robot") -> 7</code>
   *
   * <pre>
   * StringUtils.indexOfDifference(null, null) = -1
   * StringUtils.indexOfDifference("", "") = -1
   * StringUtils.indexOfDifference("", "abc") = 0
   * StringUtils.indexOfDifference("abc", "") = 0
   * StringUtils.indexOfDifference("abc", "abc") = -1
   * StringUtils.indexOfDifference("ab", "abxyz") = 2
   * StringUtils.indexOfDifference("abcde", "abxyz") = 2
   * StringUtils.indexOfDifference("abcde", "xyz") = 0
   * </pre>
   *
   * @param str1  the first String, may be null
   * @param str2  the second String, may be null
   * @return the index where str2 and str1 begin to differ; -1 if they are equal
   * @since 2.0
   */ public static int indexOfDifference(String str1, String str2) {
      if (str1 == str2) {
          return -1;
      }
      if (str1 == null || str2 == null) {
          return 0;
      }
      int i;
      for (i = 0; i < str1.length() && i < str2.length(); ++i) {
          if (str1.charAt(i) != str2.charAt(i)) {
              break;
          }
      }
      if (i < str2.length() || i < str1.length()) {
          return i;
      }
      return -1;
  }
}
```
