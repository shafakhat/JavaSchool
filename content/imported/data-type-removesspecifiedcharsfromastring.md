---
title: Removes specified chars from a string
nav: Removes specified chars fr...
description: * The contents of this file are subject to the Sapient Public License
section: Imported - java2s Archive
order: 1135
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Removesspecifiedcharsfromastring.htm
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
 */import java.util.ArrayList;
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
 */public class StringUtil {
  /**
   *
   * @param aString the string that will be examined to remove chars
   * @param unWantedCharArray the char array containing the chars
   * that should be removed from a string
   * @return the string after removing the specified chars
   */ public static String removeCharsFromString(String aString, char[] unWantedCharArray) {
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
