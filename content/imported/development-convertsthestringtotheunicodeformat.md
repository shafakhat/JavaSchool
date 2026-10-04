---
title: Converts the string to the unicode format
nav: Converts the string to the...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1741
source: https://web.archive.org/web/2018/http://www.java2s.com/Tutorial/Java/0120__Development/Convertsthestringtotheunicodeformat.htm
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
 * Operations on char primitives and Character objects.
 *
 * This class tries to handle <code>null</code> input gracefully.
 * An exception will not be thrown for a <code>null</code> input.
 * Each method documents its behaviour in more detail.
 *
 * @author Stephen Colebourne
 * @since 2.1
 * @version $Id: CharUtils.java 437554 2006-08-28 06:21:41Z bayard $
 */public class Main {
  //--------------------------------------------------------------------------
 /**
   * Converts the string to the unicode format '\u0020'.
   *
   * This format is the Java source code format.
   *
   * <pre>
   *   CharUtils.unicodeEscaped(' ') = "\u0020"
   *   CharUtils.unicodeEscaped('A') = "\u0041"
   * </pre>
   *
   * @param ch  the character to convert
   * @return the escaped unicode string
   */ public static String unicodeEscaped(char ch) {
      if (ch < 0x10) {
          return "\\u000" + Integer.toHexString(ch);
      } else if (ch < 0x100) {
          return "\\u00" + Integer.toHexString(ch);
      } else if (ch < 0x1000) {
          return "\\u0" + Integer.toHexString(ch);
      }
      return "\\u" + Integer.toHexString(ch);
  }
  /**
   * Converts the string to the unicode format '\u0020'.
   *
   * This format is the Java source code format.
   *
   * If <code>null</code> is passed in, <code>null</code> will be returned.
   *
   * <pre>
   *   CharUtils.unicodeEscaped(null) = null
   *   CharUtils.unicodeEscaped(' ')  = "\u0020"
   *   CharUtils.unicodeEscaped('A')  = "\u0041"
   * </pre>
   *
   * @param ch  the character to convert, may be null
   * @return the escaped unicode string, null if null input
   */ public static String unicodeEscaped(Character ch) {
      if (ch == null) {
          return null;
      }
      return unicodeEscaped(ch.charValue());
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
