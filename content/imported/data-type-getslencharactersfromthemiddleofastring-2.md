---
title: Gets len characters from the middle of a String.
nav: Gets len characters from t...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1018
source: https://web.archive.org/web/20100606072206/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/GetslencharactersfromthemiddleofaString.htm
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
   * Gets <code>len</code> characters from the middle of a String.
   *
   * If <code>len</code> characters are not available, the remainder
   * of the String will be returned without an exception. If the
   * String is <code>null</code>, <code>null</code> will be returned.
   * An exception is thrown if len is negative.
   *
   * <pre>
   * StringUtils.mid(null, *, *)    = null
   * StringUtils.mid(*, *, -ve)     = ""
   * StringUtils.mid("", 0, *)      = ""
   * StringUtils.mid("abc", 0, 2)   = "ab"
   * StringUtils.mid("abc", 0, 4)   = "abc"
   * StringUtils.mid("abc", 2, 4)   = "c"
   * StringUtils.mid("abc", 4, 2)   = ""
   * StringUtils.mid("abc", -2, 2)  = "ab"
   * </pre>
   *
   * @param str  the String to get the characters from, may be null
   * @param pos  the position to start from, negative treated as zero
   * @param len  the length of the required String, must be zero or positive
   * @return the middle characters, <code>null</code> if null String input
   */
  public static String mid(String str, int pos, int len) {
      if (str == null) {
          return null;
      }
      if (len < 0 || pos > str.length()) {
          return "";
      }
      if (pos < 0) {
          pos = 0;
      }
      if (str.length() <= (pos + len)) {
          return str.substring(pos);
      }
      return str.substring(pos, pos + len);
  }
}
```
