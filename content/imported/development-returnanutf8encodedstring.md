---
title: Return an UTF-8 encoded String
nav: Return an UTF-8 encoded St...
description: * Licensed to the Apache Software Foundation (ASF) under one
section: Imported - java2s Archive
order: 1742
source: https://web.archive.org/web/2018/http://www.java2s.com/Tutorial/Java/0120__Development/ReturnanUTF8encodedString.htm
---
```java title=Example.java
import java.io.UnsupportedEncodingException;
/*
 *  Licensed to the Apache Software Foundation (ASF) under one
 *  or more contributor license agreements.  See the NOTICE file
 *  distributed with this work for additional information
 *  regarding copyright ownership.  The ASF licenses this file
 *  to you under the Apache License, Version 2.0 (the
 *  "License"); you may not use this file except in compliance
 *  with the License.  You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing,
 *  software distributed under the License is distributed on an
 *  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 *  KIND, either express or implied.  See the License for the
 *  specific language governing permissions and limitations
 *  under the License.
 *
 *//**
 * Various string manipulation methods that are more efficient then chaining
 * string operations: all is done in the same buffer without creating a bunch of
 * string objects.
 *
 * @author <a href="mailto:dev@labs.apache.org">Dungeon Project</a>
 */public class Main {
  /**
   *
   * @param bytes
   *            The byte array to be transformed to a String
   * @return A String.
   */ public static final String utf8ToString( byte[] bytes )
  {
      if ( bytes == null )
      {
          return "";
      }
      try
      {
          return new String( bytes, "UTF-8" );
      }
      catch ( UnsupportedEncodingException uee )
      {
          return "";
      }
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
