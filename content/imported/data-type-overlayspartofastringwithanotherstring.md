---
title: Overlays part of a String with another String.
nav: Overlays part of a String ...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1070
source: https://web.archive.org/web/20100604104946/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/OverlayspartofaStringwithanotherString.htm
---
```java title=Example.java
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.SQLException;
/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 *  contributor license agreements.  See the NOTICE file distributed with
 *  this work for additional information regarding copyright ownership.
 *  The ASF licenses this file to You under the Apache License, Version 2.0
 *  (the "License"); you may not use this file except in compliance with
 *  the License.  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS,
 *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *  See the License for the specific language governing permissions and
 *  limitations under the License.
 *
 *
 */
public class Main {
  /**
   *
   * A <code>null</code> string input returns <code>null</code>.
   * A negative index is treated as zero.
   * An index greater than the string length is treated as the string length.
   * The start index is always the smaller of the two indices.
   *
   * <pre>
   * StringUtils.overlay(null, *, *, *)            = null
   * StringUtils.overlay("", "abc", 0, 0)          = "abc"
   * StringUtils.overlay("abcdef", null, 2, 4)     = "abef"
   * StringUtils.overlay("abcdef", "", 2, 4)       = "abef"
   * StringUtils.overlay("abcdef", "", 4, 2)       = "abef"
   * StringUtils.overlay("abcdef", "zzzz", 2, 4)   = "abzzzzef"
   * StringUtils.overlay("abcdef", "zzzz", 4, 2)   = "abzzzzef"
   * StringUtils.overlay("abcdef", "zzzz", -1, 4)  = "zzzzef"
   * StringUtils.overlay("abcdef", "zzzz", 2, 8)   = "abzzzz"
   * StringUtils.overlay("abcdef", "zzzz", -2, -3) = "zzzzabcdef"
   * StringUtils.overlay("abcdef", "zzzz", 8, 10)  = "abcdefzzzz"
   * </pre>
   *
   * @param str  the String to do overlaying in, may be null
   * @param overlay  the String to overlay, may be null
   * @param start  the position to start overlaying at
   * @param end  the position to stop overlaying before
   * @return overlayed String, <code>null</code> if null String input
   * @since 2.0
   */
  public static String overlay(String str, String overlay, int start, int end) {
      if (str == null) {
          return null;
      }
      if (overlay == null) {
          overlay = "";
      }
      int len = str.length();
      if (start < 0) {
          start = 0;
      }
      if (start > len) {
          start = len;
      }
      if (end < 0) {
          end = 0;
      }
      if (end > len) {
          end = len;
      }
      if (start > end) {
          int temp = start;
          start = end;
          end = temp;
      }
      return new StringBuffer(len + start - end + overlay.length() + 1)
          .append(str.substring(0, start))
          .append(overlay)
          .append(str.substring(end))
          .toString();
  }
}
```
