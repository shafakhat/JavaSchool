---
title: Gets a substring from the specified String avoiding exceptions.
nav: Gets a substring from the ...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1111
source: https://web.archive.org/web/20110109132131/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/GetsasubstringfromthespecifiedStringavoidingexceptions.htm
---
```java title=Example.java
/**
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
/**
 * Operations on {@link java.lang.String} that are
 * <code>null</code> safe.
 *
 * @see java.lang.String
 * @author <a href="http://jakarta.apache.org/turbine/">Apache Jakarta Turbine</a>
 * @author <a href="mailto:jon@latchkey.com">Jon S. Stevens</a>
 * @author Daniel L. Rall
 * @author <a href="mailto:gcoladonato@yahoo.com">Greg Coladonato</a>
 * @author <a href="mailto:ed@apache.org">Ed Korthof</a>
 * @author <a href="mailto:rand_mcneely@yahoo.com">Rand McNeely</a>
 * @author Stephen Colebourne
 * @author <a href="mailto:fredrik@westermarck.com">Fredrik Westermarck</a>
 * @author Holger Krauth
 * @author <a href="mailto:alex@purpletech.com">Alexander Day Chaffee</a>
 * @author <a href="mailto:hps@intermeta.de">Henning P. Schmiedehausen</a>
 * @author Arun Mammen Thomas
 * @author Gary Gregory
 * @author Phil Steitz
 * @author Al Chou
 * @author Michael Davey
 * @author Reuben Sivan
 * @author Chris Hyzer
 * @author Scott Johnson
 * @since 1.0
 * @version $Id: StringUtils.java 635447 2008-03-10 06:27:09Z bayard $
 */
public class Main {
  /**
   * Gets a substring from the specified String avoiding exceptions.
   *
   * A negative start position can be used to start/end <code>n</code>
   * characters from the end of the String.
   *
   * The returned substring starts with the character in the <code>start</code>
   * position and ends before the <code>end</code> position. All position counting is
   * zero-based -- i.e., to start at the beginning of the string use
   * <code>start = 0</code>. Negative start and end positions can be used to
   * specify offsets relative to the end of the String.
   *
   * If <code>start</code> is not strictly to the left of <code>end</code>, ""
   * is returned.
   *
   * <pre>
   * StringUtils.substring(null, *, *)    = null
   * StringUtils.substring("", * ,  *)    = "";
   * StringUtils.substring("abc", 0, 2)   = "ab"
   * StringUtils.substring("abc", 2, 0)   = ""
   * StringUtils.substring("abc", 2, 4)   = "c"
   * StringUtils.substring("abc", 4, 6)   = ""
   * StringUtils.substring("abc", 2, 2)   = ""
   * StringUtils.substring("abc", -2, -1) = "b"
   * StringUtils.substring("abc", -4, 2)  = "ab"
   * </pre>
   *
   * @param str  the String to get the substring from, may be null
   * @param start  the position to start from, negative means
   *  count back from the end of the String by this many characters
   * @param end  the position to end at (exclusive), negative means
   *  count back from the end of the String by this many characters
   * @return substring from start position to end positon,
   *  <code>null</code> if null String input
   */
  public static String substring(String str, int start, int end) {
      if (str == null) {
          return null;
      }
      // handle negatives
      if (end < 0) {
          end = str.length() + end; // remember end is negative
      }
      if (start < 0) {
          start = str.length() + start; // remember start is negative
      }
      // check length next
      if (end > str.length()) {
          end = str.length();
      }
      // if start is greater than end, return ""
      if (start > end) {
          return "";
      }
      if (start < 0) {
          start = 0;
      }
      if (end < 0) {
          end = 0;
      }
      return str.substring(start, end);
  }
}
```
