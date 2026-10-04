---
title: Finds the n-th index within a String, handling null.
nav: Finds the n-th index withi...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1151
source: https://web.archive.org/web/20140829090902/http://www.java2s.com/Tutorial/Java/0040__Data-Type/FindsthenthindexwithinaStringhandlingnull.htm
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
   * Finds the n-th index within a String, handling <code>null</code>.
   * This method uses {@link String#indexOf(String)}.
   *
   * A <code>null</code> String will return <code>-1</code>.
   *
   * <pre>
   * StringUtils.ordinalIndexOf(null, *, *)          = -1
   * StringUtils.ordinalIndexOf(*, null, *)          = -1
   * StringUtils.ordinalIndexOf("", "", *)           = 0
   * StringUtils.ordinalIndexOf("aabaabaa", "a", 1)  = 0
   * StringUtils.ordinalIndexOf("aabaabaa", "a", 2)  = 1
   * StringUtils.ordinalIndexOf("aabaabaa", "b", 1)  = 2
   * StringUtils.ordinalIndexOf("aabaabaa", "b", 2)  = 5
   * StringUtils.ordinalIndexOf("aabaabaa", "ab", 1) = 1
   * StringUtils.ordinalIndexOf("aabaabaa", "ab", 2) = 4
   * StringUtils.ordinalIndexOf("aabaabaa", "", 1)   = 0
   * StringUtils.ordinalIndexOf("aabaabaa", "", 2)   = 0
   * </pre>
   *
   * @param str  the String to check, may be null
   * @param searchStr  the String to find, may be null
   * @param ordinal  the n-th <code>searchStr</code> to find
   * @return the n-th index of the search String,
   *  <code>-1</code> (<code>INDEX_NOT_FOUND</code>) if no match or <code>null</code> string input
   * @since 2.1
   */
  public static int ordinalIndexOf(String str, String searchStr, int ordinal) {
      if (str == null || searchStr == null || ordinal <= 0) {
          return -1;
      }
      if (searchStr.length() == 0) {
          return 0;
      }
      int found = 0;
      int index = -1;
      do {
          index = str.indexOf(searchStr, index + 1);
          if (index < 0) {
              return index;
          }
          found++;
      } while (found < ordinal);
      return index;
  }
}
```

| 2.29.1. | Find the latest index of any of a set of potential substrings. |
|---|---|
| 2.29.2. | Find the first index of any of a set of potential substrings. |
| 2.29.3. | Finds the first index within a String, handling null. |
| 2.29.4. | Finds the last index within a String from a start position, handling null. |
| 2.29.5. | Finds the n-th index within a String, handling null. |
| 2.29.6. | Use String.indexOf to locate a character in a string |
| 2.29.7. | Use String.lastIndexOf to find a character in a string |
| 2.29.8. | Use String.indexOf to locate a substring in a string |
| 2.29.9. | Use lastIndexOf to find a substring in a string |
| 2.29.10. | Demonstrate indexOf() and lastIndexOf(). |
| 2.29.11. | Extract Substring with indexOf |
| 2.29.12. | Java String endsWith |
| 2.29.13. | Java String startsWith |
| 2.29.14. | Starts with, ignore case( regular expressions ) |
| 2.29.15. | Ends with, ignore case( regular expressions ) |
| 2.29.16. | Anywhere, ignore case( regular expressions ) |
| 2.29.17. | Last occurrence of a character |
| 2.29.18. | Not found returns -1 |
| 2.29.19. | A bubble sort for Strings. |
| 2.29.20. | Search a String to find the first index of any character in the given set of characters. |
| 2.29.21. | Search a String to find the first index of any character not in the given set of characters. |
