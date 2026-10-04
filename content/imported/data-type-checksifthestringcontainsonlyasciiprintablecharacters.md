---
title: Checks if the string contains only ASCII printable characters.
nav: Checks if the string conta...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1028
source: https://web.archive.org/web/20140829083334/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ChecksifthestringcontainsonlyASCIIprintablecharacters.htm
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
   *
   * <code>null</code> will return <code>false</code>.
   * An empty String ("") will return <code>true</code>.
   *
   * <pre>
   * StringUtils.isAsciiPrintable(null)     = false
   * StringUtils.isAsciiPrintable("")       = true
   * StringUtils.isAsciiPrintable(" ")      = true
   * StringUtils.isAsciiPrintable("Ceki")   = true
   * StringUtils.isAsciiPrintable("ab2c")   = true
   * StringUtils.isAsciiPrintable("!ab-c~") = true
   * StringUtils.isAsciiPrintable("\u0020") = true
   * StringUtils.isAsciiPrintable("\u0021") = true
   * StringUtils.isAsciiPrintable("\u007e") = true
   * StringUtils.isAsciiPrintable("\u007f") = false
   * StringUtils.isAsciiPrintable("Ceki G\u00fclc\u00fc") = false
   * </pre>
   *
   * @param str the string to check, may be null
   * @return <code>true</code> if every character is in the range
   *  32 thru 126
   * @since 2.1
   */
  public static boolean isAsciiPrintable(String str) {
      if (str == null) {
          return false;
      }
      int sz = str.length();
      for (int i = 0; i < sz; i++) {
          if (isAsciiPrintable(str.charAt(i)) == false) {
              return false;
          }
      }
      return true;
  }
  /**
   * Checks whether the character is ASCII 7 bit printable.
   *
   * <pre>
   *   CharUtils.isAsciiPrintable('a')  = true
   *   CharUtils.isAsciiPrintable('A')  = true
   *   CharUtils.isAsciiPrintable('3')  = true
   *   CharUtils.isAsciiPrintable('-')  = true
   *   CharUtils.isAsciiPrintable('\n') = false
   *   CharUtils.isAsciiPrintable('&copy;') = false
   * </pre>
   *
   * @param ch  the character to check
   * @return true if between 32 and 126 inclusive
   */
  public static boolean isAsciiPrintable(char ch) {
      return ch >= 32 && ch < 127;
  }
}
```
