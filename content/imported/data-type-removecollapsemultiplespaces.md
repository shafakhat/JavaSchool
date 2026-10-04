---
title: Remove/collapse multiple spaces.
nav: Remove/collapse multiple s...
description: * or more contributor license agreements. See the NOTICE file
section: Imported - java2s Archive
order: 1282
source: https://web.archive.org/web/20140829080342/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Removecollapsemultiplespaces.htm
---
```java title=Example.java
/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */
/**
 *
 *  @author <a href="mailto:jvanzyl@apache.org">Jason van Zyl</a>
 *  @author <a href="mailto:dlr@finemaltcoding.com">Daniel Rall</a>
 *  @version $Id: StringUtils.java 685685 2008-08-13 21:43:27Z nbubna $
 */
public class Main {
  /**
   *
   * @param argStr string to remove multiple spaces from.
   * @return String
   */
  public static String collapseSpaces(String argStr)
  {
      char last = argStr.charAt(0);
      StringBuffer argBuf = new StringBuffer();
      for (int cIdx = 0 ; cIdx < argStr.length(); cIdx++)
      {
          char ch = argStr.charAt(cIdx);
          if (ch != ' ' || last != ' ')
          {
              argBuf.append(ch);
              last = ch;
          }
      }
      return argBuf.toString();
  }
}
```

| 2.21.1. | To replace one specific character with another throughout a string |
|---|---|
| 2.21.2. | To remove whitespace from the beginning and end of a string (but not the interior) |
| 2.21.3. | Replacing Characters in a String: replace() method creates a new string with the replaced characters. |
| 2.21.4. | Replacing Substrings in a String |
| 2.21.5. | String.Replace |
| 2.21.6. | Replaces all occourances of given character with new one and returns new String object. |
| 2.21.7. | Replaces only first occourances of given String with new one and returns new String object. |
| 2.21.8. | Replaces all occourances of given String with new one and returns new String object. |
| 2.21.9. | Replace/remove character in a String: replace all occurences of a given character |
| 2.21.10. | To replace a character at a specified position |
| 2.21.11. | Replace \r\n with the tag |
| 2.21.12. | Replace multiple whitespaces between words with single blank |
| 2.21.13. | Unaccent letters |
| 2.21.14. | Only replace first occurence |
| 2.21.15. | Get all digits from a string |
| 2.21.16. | Returns a new string with all the whitespace removed |
| 2.21.17. | Removes specified chars from a string |
| 2.21.18. | Remove/collapse multiple spaces. |
