---
title: Finds the first index within a String, handling null.
nav: Finds the first index with...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1098
source: https://web.archive.org/web/20140829091000/http://www.java2s.com/Tutorial/Java/0040__Data-Type/FindsthefirstindexwithinaStringhandlingnull.htm
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
   * Finds the first index within a String, handling <code>null</code>.
   * This method uses {@link String#indexOf(String, int)}.
   *
   * A <code>null</code> String will return <code>-1</code>.
   * A negative start position is treated as zero.
   * An empty ("") search String always matches.
   * A start position greater than the string length only matches
   * an empty search String.
   *
   * <pre>
   * StringUtils.indexOf(null, *, *)          = -1
   * StringUtils.indexOf(*, null, *)          = -1
   * StringUtils.indexOf("", "", 0)           = 0
   * StringUtils.indexOf("aabaabaa", "a", 0)  = 0
   * StringUtils.indexOf("aabaabaa", "b", 0)  = 2
   * StringUtils.indexOf("aabaabaa", "ab", 0) = 1
   * StringUtils.indexOf("aabaabaa", "b", 3)  = 5
   * StringUtils.indexOf("aabaabaa", "b", 9)  = -1
   * StringUtils.indexOf("aabaabaa", "b", -1) = 2
   * StringUtils.indexOf("aabaabaa", "", 2)   = 2
   * StringUtils.indexOf("abc", "", 9)        = 3
   * </pre>
   *
   * @param str  the String to check, may be null
   * @param searchStr  the String to find, may be null
   * @param startPos  the start position, negative treated as zero
   * @return the first index of the search String,
   *  -1 if no match or <code>null</code> string input
   * @since 2.0
   */
  public static int indexOf(String str, String searchStr, int startPos) {
      if (str == null || searchStr == null) {
          return -1;
      }
      // JDK1.2/JDK1.3 have a bug, when startPos > str.length for "", hence
      if (searchStr.length() == 0 && startPos >= str.length()) {
          return str.length();
      }
      return str.indexOf(searchStr, startPos);
  }
}
```
