---
title: Helper function that returns a char from an hex
nav: Helper function that retur...
description: * Licensed to the Apache Software Foundation (ASF) under one
section: Imported - java2s Archive
order: 1183
source: https://web.archive.org/web/20140829091503/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Helperfunctionthatreturnsacharfromanhex.htm
---
```java title=Example.java
import java.io.File;
import java.io.FileFilter;
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Pattern;
import java.util.regex.PatternSyntaxException;
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
 */
/**
 * Various string manipulation methods that are more efficient then chaining
 * string operations: all is done in the same buffer without creating a bunch of
 * string objects.
 *
 * @author <a href="mailto:dev@labs.apache.org">Dungeon Project</a>
 */
public class Main {
  /** Hex chars */
  private static final byte[] HEX_CHAR = new byte[]
      { '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F' };
  /**
   *
   * @param hex The hex to dump
   * @return A char representation of the hex
   */
  public static final char dumpHex( byte hex )
  {
      return ( char ) HEX_CHAR[hex & 0x000F];
  }
}
```

| 2.9.1. | Hexadecimal integer literal |
|---|---|
| 2.9.2. | A hexadecimal literal of type long |
| 2.9.3. | Defining integer literals as octal values |
| 2.9.4. | Decode string to integer |
| 2.9.5. | Convert octal number to decimal number example |
| 2.9.6. | Convert decimal integer to octal number example |
| 2.9.7. | Convert decimal integer to hexadecimal number example |
| 2.9.8. | Parsing and Formatting a Number into Binary |
| 2.9.9. | Convert byte array to Hex String |
| 2.9.10. | Convert the bytes to a hex string representation of the bytes |
| 2.9.11. | Converting hexadecimal strings |
| 2.9.12. | Dumps data in hexadecimal format |
| 2.9.13. | Given a hexstring this will return the byte array corresponding to string |
| 2.9.14. | Hex encoder/decoder implementation borrowed from BouncyCastle |
| 2.9.15. | Returns the hexadecimal value of the supplied byte array |
| 2.9.16. | A custom number formatter that formats numbers as hexadecimal strings. |
| 2.9.17. | Decodes Hex data into octects |
| 2.9.18. | Decodes Base64 data into octects |
| 2.9.19. | Helper function that returns a char from an hex |
| 2.9.20. | Encodes hex octects into Base64 |
| 2.9.21. | Hex encoder and decoder. |
| 2.9.22. | Helper function that dump an array of bytes in hex pair form, without '0x' and space chars |
| 2.9.23. | dump an array of bytes in hex form |
| 2.9.24. | Decode byte array |
