---
title: Checks if the String contains only unicode letters, digits or space (' ').
nav: Checks if the String conta...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1748
source: https://web.archive.org/web/20140811062853/http://www.java2s.com/Tutorial/Java/0120__Development/ChecksiftheStringcontainsonlyunicodelettersdigitsorspace.htm
---
```java title=Example.java
/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
public class Main {
  /**
   * Checks if the String contains only unicode letters, digits
   * or space (<code>' '</code>).
   *
   * <code>null</code> will return <code>false</code>.
   * An empty String ("") will return <code>true</code>.
   *
   * <pre>
   * StringUtils.isAlphanumeric(null)   = false
   * StringUtils.isAlphanumeric("")     = true
   * StringUtils.isAlphanumeric("  ")   = true
   * StringUtils.isAlphanumeric("abc")  = true
   * StringUtils.isAlphanumeric("ab c") = true
   * StringUtils.isAlphanumeric("ab2c") = true
   * StringUtils.isAlphanumeric("ab-c") = false
   * </pre>
   *
   * @param str  the String to check, may be null
   * @return <code>true</code> if only contains letters, digits or space,
   *  and is non-null
   */
  public static boolean isAlphanumericSpace(String str) {
      if (str == null) {
          return false;
      }
      int sz = str.length();
      for (int i = 0; i < sz; i++) {
          if ((Character.isLetterOrDigit(str.charAt(i)) == false) && (str.charAt(i) != ' ')) {
              return false;
          }
      }
      return true;
  }
}
```

| 6.16.1. | Using Unicode in String |
|---|---|
| 6.16.2. | Display special character using Unicode |
| 6.16.3. | Convert from Unicode to UTF-8 |
| 6.16.4. | Convert from UTF-8 to Unicode |
| 6.16.5. | Convert string to UTF8 bytes |
| 6.16.6. | Converts Unicode into something that can be embedded in a java properties file |
| 6.16.7. | Converts the string to the unicode format |
| 6.16.8. | Return an UTF-8 encoded String |
| 6.16.9. | Return an UTF-8 encoded String by length |
| 6.16.10. | Return UTF-8 encoded byte[] representation of a String |
| 6.16.11. | Get UTF String Size |
| 6.16.12. | Return the number of bytes that hold an Unicode char. |
| 6.16.13. | Return the Unicode char which is coded in the bytes at position 0. |
| 6.16.14. | Return the Unicode char which is coded in the bytes at the given position. |
| 6.16.15. | Checks if the String contains only unicode digits or space |
| 6.16.16. | Checks if the String contains only unicode digits. A decimal point is not a unicode digit and returns false. |
| 6.16.17. | Checks if the String contains only unicode letters and space (' '). |
| 6.16.18. | Checks if the String contains only unicode letters or digits. |
| 6.16.19. | Checks if the String contains only unicode letters, digits or space (' '). |
| 6.16.20. | Checks if the String contains only unicode letters. |
| 6.16.21. | Count the number of bytes included in the given char[]. |
| 6.16.22. | Count the number of bytes needed to return an Unicode char. This can be from 1 to 6. |
| 6.16.23. | Count the number of chars included in the given byte[]. |
| 6.16.24. | Decodes values of attributes in the DN encoded in hex into a UTF-8 String. |
| 6.16.25. | Safe UTF: 64K serialized size |
