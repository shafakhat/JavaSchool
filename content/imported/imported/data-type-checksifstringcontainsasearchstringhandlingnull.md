---
title: Checks if String contains a search String, handling null
nav: Checks if String contains ...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1010
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ChecksifStringcontainsasearchStringhandlingnull.htm
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
 */publicclass Main {
  /**
   * Checks if String contains a search String, handling <code>null</code>.
   * This method uses {@link String#indexOf(String)}.
   *
   * A <code>null</code> String will return <code>false</code>.
   *
   * <pre>
   * StringUtils.contains(null, *)     = false
   * StringUtils.contains(*, null)     = false
   * StringUtils.contains("", "")      = true
   * StringUtils.contains("abc", "")   = true
   * StringUtils.contains("abc", "a")  = true
   * StringUtils.contains("abc", "z")  = false
   * </pre>
   *
   * @param str  the String to check, may be null
   * @param searchStr  the String to find, may be null
   * @return true if the String contains the search String,
   *  false if not or <code>null</code> string input
   * @since 2.0
   */publicstaticboolean contains(String str, String searchStr) {
      if (str == null || searchStr == null) {
          return false;
      }
      return str.indexOf(searchStr) >= 0;
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
   */publicstaticboolean isEmpty(String str) {
      return str == null || str.length() == 0;
  }

}
```
