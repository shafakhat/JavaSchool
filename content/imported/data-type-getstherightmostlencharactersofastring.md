---
title: Gets the rightmost len characters of a String.
nav: Gets the rightmost len cha...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1000
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/GetstherightmostlencharactersofaString.htm
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
 *//**
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
 */public class Main {
  /**
   * Gets the rightmost <code>len</code> characters of a String.
   *
   * If <code>len</code> characters are not available, or the String
   * is <code>null</code>, the String will be returned without an
   * an exception. An exception is thrown if len is negative.
   *
   * <pre>
   * StringUtils.right(null, *)    = null
   * StringUtils.right(*, -ve)     = ""
   * StringUtils.right("", *)      = ""
   * StringUtils.right("abc", 0)   = ""
   * StringUtils.right("abc", 2)   = "bc"
   * StringUtils.right("abc", 4)   = "abc"
   * </pre>
   *
   * @param str  the String to get the rightmost characters from, may be null
   * @param len  the length of the required String, must be zero or positive
   * @return the rightmost characters, <code>null</code> if null String input
   */ public static String right(String str, int len) {
      if (str == null) {
          return null;
      }
      if (len < 0) {
          return "";
      }
      if (str.length() <= len) {
          return str;
      }
      return str.substring(str.length() - len);
  }
}
```
