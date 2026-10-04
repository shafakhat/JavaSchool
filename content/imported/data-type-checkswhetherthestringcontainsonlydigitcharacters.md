---
title: Checks whether the String contains only digit characters.
nav: Checks whether the String ...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1357
source: https://web.archive.org/web/20140828211759/http://www.java2s.com/Tutorial/Java/0040__Data-Type/CheckswhethertheStringcontainsonlydigitcharacters.htm
---
```java title=Example.java
import java.math.BigDecimal;
import java.math.BigInteger;
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
 * Provides extra functionality for Java Number classes.
 *
 * @author <a href="mailto:rand_mcneely@yahoo.com">Rand McNeely</a>
 * @author Stephen Colebourne
 * @author <a href="mailto:steve.downey@netfolio.com">Steve Downey</a>
 * @author Eric Pugh
 * @author Phil Steitz
 * @since 1.0
 * @version $Id: NumberUtils.java 488819 2006-12-19 21:50:04Z bayard $
 *
 */
public class Main {
  //--------------------------------------------------------------------
  /**
   * Checks whether the <code>String</code> contains only
   * digit characters.
   *
   * <code>Null</code> and empty String will return
   * <code>false</code>.
   *
   * @param str  the <code>String</code> to check
   * @return <code>true</code> if str contains only unicode numeric
   */
  public static boolean isDigits(String str) {
      if ((str == null) || (str.length() == 0)) {
          return false;
      }
      for (int i = 0; i < str.length(); i++) {
          if (!Character.isDigit(str.charAt(i))) {
              return false;
          }
      }
      return true;
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
