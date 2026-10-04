---
title: Search a String to find the first index of any character not in the given set of characters.
nav: Search a String to find th...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1111
source: https://web.archive.org/web/20140829091020/http://www.java2s.com/Tutorial/Java/0040__Data-Type/SearchaStringtofindthefirstindexofanycharacternotinthegivensetofcharacters.htm
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
   * Search a String to find the first index of any
   * character not in the given set of characters.
   *
   * A <code>null</code> String will return <code>-1</code>.
   * A <code>null</code> search string will return <code>-1</code>.
   *
   * <pre>
   * StringUtils.indexOfAnyBut(null, *)            = -1
   * StringUtils.indexOfAnyBut("", *)              = -1
   * StringUtils.indexOfAnyBut(*, null)            = -1
   * StringUtils.indexOfAnyBut(*, "")              = -1
   * StringUtils.indexOfAnyBut("zzabyycdxx", "za") = 3
   * StringUtils.indexOfAnyBut("zzabyycdxx", "")   = 0
   * StringUtils.indexOfAnyBut("aba","ab")         = -1
   * </pre>
   *
   * @param str  the String to check, may be null
   * @param searchChars  the chars to search for, may be null
   * @return the index of any of the chars, -1 if no match or null input
   * @since 2.0
   */
  public static int indexOfAnyBut(String str, String searchChars) {
      if (isEmpty(str) || isEmpty(searchChars)) {
          return -1;
      }
      for (int i = 0; i < str.length(); i++) {
          if (searchChars.indexOf(str.charAt(i)) < 0) {
              return i;
          }
      }
      return -1;
  }
  // ----------------------------------------------------------------------
  /**
   * Checks if an array of Objects is empty or <code>null</code>.
   *
   * @param array  the array to test
   * @return <code>true</code> if the array is empty or <code>null</code>
   * @since 2.1
   */
  public static boolean isEmpty(char[] array) {
      if (array == null || array.length == 0) {
          return true;
      }
      return false;
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
   */
  public static boolean isEmpty(String str) {
      return str == null || str.length() == 0;
  }
}
```
