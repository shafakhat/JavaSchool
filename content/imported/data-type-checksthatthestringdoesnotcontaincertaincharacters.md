---
title: Checks that the String does not contain certain characters.
nav: Checks that the String doe...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1351
source: https://web.archive.org/web/20140829081438/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ChecksthattheStringdoesnotcontaincertaincharacters.htm
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
   *
   * A <code>null</code> String will return <code>true</code>.
   * A <code>null</code> invalid character array will return <code>true</code>.
   * An empty String ("") always returns true.
   *
   * <pre>
   * StringUtils.containsNone(null, *)       = true
   * StringUtils.containsNone(*, null)       = true
   * StringUtils.containsNone("", *)         = true
   * StringUtils.containsNone("ab", "")      = true
   * StringUtils.containsNone("abab", "xyz") = true
   * StringUtils.containsNone("ab1", "xyz")  = true
   * StringUtils.containsNone("abz", "xyz")  = false
   * </pre>
   *
   * @param str  the String to check, may be null
   * @param invalidChars  a String of invalid chars, may be null
   * @return true if it contains none of the invalid chars, or is null
   * @since 2.0
   */
  public static boolean containsNone(String str, String invalidChars) {
      if (str == null || invalidChars == null) {
          return true;
      }
      return containsNone(str, invalidChars.toCharArray());
  }
  // ContainsNone
  //-----------------------------------------------------------------------
  /**
   *
   * A <code>null</code> String will return <code>true</code>.
   * A <code>null</code> invalid character array will return <code>true</code>.
   * An empty String ("") always returns true.
   *
   * <pre>
   * StringUtils.containsNone(null, *)       = true
   * StringUtils.containsNone(*, null)       = true
   * StringUtils.containsNone("", *)         = true
   * StringUtils.containsNone("ab", '')      = true
   * StringUtils.containsNone("abab", 'xyz') = true
   * StringUtils.containsNone("ab1", 'xyz')  = true
   * StringUtils.containsNone("abz", 'xyz')  = false
   * </pre>
   *
   * @param str  the String to check, may be null
   * @param invalidChars  an array of invalid chars, may be null
   * @return true if it contains none of the invalid chars, or is null
   * @since 2.0
   */
  public static boolean containsNone(String str, char[] invalidChars) {
      if (str == null || invalidChars == null) {
          return true;
      }
      int strSize = str.length();
      int validSize = invalidChars.length;
      for (int i = 0; i < strSize; i++) {
          char ch = str.charAt(i);
          for (int j = 0; j < validSize; j++) {
              if (invalidChars[j] == ch) {
                  return false;
              }
          }
      }
      return true;
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

| 2.28.1. | Demonstrates the charAt and getChars |
|---|---|
| 2.28.2. | Converting Char array to String |
| 2.28.3. | Creating Character Arrays From String Objects |
| 2.28.4. | Copy characters from string into char Array |
| 2.28.5. | Creating String Objects From Character Arrays |
| 2.28.6. | new String(textArray, 9, 3): Creating String Objects From certain part of a character Array |
| 2.28.7. | Creating String Objects From Character Arrays using String.copyValueOf() |
| 2.28.8. | Creating a string from a subset of the array elements |
| 2.28.9. | Extracting a substring as an array of characters using the method getChars() |
| 2.28.10. | Using the Collection-Based for Loop with a String: Counting all vowels in a string |
| 2.28.11. | Construct one String from another. |
| 2.28.12. | demonstrates getChars( ): |
| 2.28.13. | implements CharSequence |
| 2.28.14. | Removes spaces (char <= 32) from end of this String with escape, handling null by returning null |
| 2.28.15. | Removes spaces (char <= 32) from end of this String, handling null by returning null |
| 2.28.16. | Swaps the case of a String changing upper and title case to lower case, and lower case to upper case. |
| 2.28.17. | Deletes all whitespaces from a String as defined by Character.isWhitespace(char). |
| 2.28.18. | Checks whether the String contains only digit characters. |
| 2.28.19. | Checks that the String does not contain certain characters. |
