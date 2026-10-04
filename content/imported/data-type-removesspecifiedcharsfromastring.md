---
title: Removes specified chars from a string
nav: Removes specified chars fr...
description: * The contents of this file are subject to the Sapient Public License
section: Imported - java2s Archive
order: 1080
source: https://web.archive.org/web/20140829080243/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Removesspecifiedcharsfromastring.htm
---
```java title=Example.java
/*
 * The contents of this file are subject to the Sapient Public License
 * Version 1.0 (the "License"); you may not use this file except in compliance
 * with the License. You may obtain a copy of the License at
 * http://carbon.sf.net/License.html.
 *
 * Software distributed under the License is distributed on an "AS IS" basis,
 * WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License for
 * the specific language governing rights and limitations under the License.
 *
 * The Original Code is The Carbon Component Framework.
 *
 * The Initial Developer of the Original Code is Sapient Corporation
 *
 * Copyright (C) 2003 Sapient Corporation. All Rights Reserved.
 */
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.StringTokenizer;
/**
 * Utilities for strings.
 *
 *
 * Copyright 2002 Sapient
 * @since carbon 1.0
 * @author Greg Hinkle, May 2002
 * @version $Revision: 1.5 $($Author: dvoet $ / $Date: 2003/05/05 21:21:24 $)
 */
public class StringUtil {
  /**
   *
   * @param aString the string that will be examined to remove chars
   * @param unWantedCharArray the char array containing the chars
   * that should be removed from a string
   * @return the string after removing the specified chars
   */
  public static String removeCharsFromString(String aString, char[] unWantedCharArray) {
      Character character = null;
      // Store unwanted chars in a hashset
      Set unWantedCharSet = new HashSet();
      for (int i = 0; i < unWantedCharArray.length; i++) {
          character = new Character(unWantedCharArray[i]);
          unWantedCharSet.add(character);
      }
      // Create result String buffer
      StringBuffer result = new StringBuffer(aString.length());
      // For each character in aString, append it to the result string buffer
      // if it is not in unWantedCharSet
      for (int i = 0; i < aString.length(); i++) {
          character = new Character(aString.charAt(i));
          if (!unWantedCharSet.contains(character)) {
              result.append(aString.charAt(i));
          }
      }
      // Return result
      return result.toString();
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
