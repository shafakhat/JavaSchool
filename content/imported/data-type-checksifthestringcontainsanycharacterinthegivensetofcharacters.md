---
title: Checks if the String contains any character in the given set of characters.
nav: Checks if the String conta...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1348
source: https://web.archive.org/web/20140216150145/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ChecksiftheStringcontainsanycharacterinthegivensetofcharacters.htm
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
   *
   *
   *
   * A <code>null</code> String will return <code>false</code>. A <code>null</code> search string will return
   * <code>false</code>.
   *
   *
   * <pre>
   * StringUtils.containsAny(null, *)            = false
   * StringUtils.containsAny("", *)              = false
   * StringUtils.containsAny(*, null)            = false
   * StringUtils.containsAny(*, "")              = false
   * StringUtils.containsAny("zzabyycdxx", "za") = true
   * StringUtils.containsAny("zzabyycdxx", "by") = true
   * StringUtils.containsAny("aba","z")          = false
   * </pre>
   *
   * @param str
   *            the String to check, may be null
   * @param searchChars
   *            the chars to search for, may be null
   * @return the <code>true</code> if any of the chars are found, <code>false</code> if no match or null input
   * @since 2.4
   */
  public static boolean containsAny(String str, String searchChars) {
      if (searchChars == null) {
          return false;
      }
      return containsAny(str, searchChars.toCharArray());
  }
  // ContainsAny
  //-----------------------------------------------------------------------
  /**
   * Checks if the String contains any character in the given
   * set of characters.
   *
   * A <code>null</code> String will return <code>false</code>.
   * A <code>null</code> or zero length search array will return <code>false</code>.
   *
   * <pre>
   * StringUtils.containsAny(null, *)                = false
   * StringUtils.containsAny("", *)                  = false
   * StringUtils.containsAny(*, null)                = false
   * StringUtils.containsAny(*, [])                  = false
   * StringUtils.containsAny("zzabyycdxx",['z','a']) = true
   * StringUtils.containsAny("zzabyycdxx",['b','y']) = true
   * StringUtils.containsAny("aba", ['z'])           = false
   * </pre>
   *
   * @param str  the String to check, may be null
   * @param searchChars  the chars to search for, may be null
   * @return the <code>true</code> if any of the chars are found,
   * <code>false</code> if no match or null input
   * @since 2.4
   */
  public static boolean containsAny(String str, char[] searchChars) {
      if (str == null || str.length() == 0 || searchChars == null || searchChars.length == 0) {
          return false;
      }
      for (int i = 0; i < str.length(); i++) {
          char ch = str.charAt(i);
          for (int j = 0; j < searchChars.length; j++) {
              if (searchChars[j] == ch) {
                  return true;
              }
          }
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

| 2.31.1. | Match Phone Number |
|---|---|
| 2.31.2. | Match Zip Codes |
| 2.31.3. | Match Dates |
| 2.31.4. | Match Name Formats |
| 2.31.5. | Case insensitive check if a String ends with a specified suffix. |
| 2.31.6. | Case insensitive check if a String starts with a specified prefix. |
| 2.31.7. | Case insensitive removal of a substring if it is at the begining of a source string, otherwise returns the source string. |
| 2.31.8. | Case insensitive removal of a substring if it is at the end of a source string, otherwise returns the source string. |
| 2.31.9. | Check if a String ends with a specified suffix. |
| 2.31.10. | Check if a String starts with a specified prefix. |
| 2.31.11. | Check if a string is present at the current position in another string. |
| 2.31.12. | Check whether the given String is a valid identifier according to the Java Language specifications. |
| 2.31.13. | Checks if String contains a search String irrespective of case, handling null |
| 2.31.14. | Checks if String contains a search String, handling null |
| 2.31.15. | Checks if String contains a search character, handling null |
| 2.31.16. | Checks if a String is empty ("") or null. |
| 2.31.17. | Checks if a String is not empty ("") and not null. |
| 2.31.18. | Checks if a String is whitespace, empty ("") or null. |
| 2.31.19. | Checks if the String contains any character in the given set of characters. |
| 2.31.20. | Checks if the String contains only certain characters. |
