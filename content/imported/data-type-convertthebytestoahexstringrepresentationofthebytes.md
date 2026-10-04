---
title: Convert the bytes to a hex string representation of the bytes
nav: Convert the bytes to a hex...
description: * or more contributor license agreements. See the NOTICE file
section: Imported - java2s Archive
order: 1469
source: https://web.archive.org/web/20140829091249/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Convertthebytestoahexstringrepresentationofthebytes.htm
---
```java title=Example.java
/**
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
import java.io.PrintWriter;
import java.io.StringWriter;
import java.net.InetAddress;
import java.net.URI;
import java.net.URISyntaxException;
import java.net.UnknownHostException;
import java.text.DateFormat;
import java.text.DecimalFormat;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Date;
import java.util.List;
import java.util.StringTokenizer;
import java.util.Collection;
/**
 * General string utils
 */
public class StringUtils {
  final public static char COMMA = ',';
  final public static String COMMA_STR = ",";
  final public static char ESCAPE_CHAR = '\\';
  private static DecimalFormat oneDecimal = new DecimalFormat("0.0");
  /**
   * Given an array of bytes it will convert the bytes to a hex string
   * representation of the bytes
   * @param bytes
   * @return hex string representation of the byte array
   */
  public static String byteToHexString(byte bytes[]) {
    StringBuffer retString = new StringBuffer();
    for (int i = 0; i < bytes.length; ++i) {
      retString.append(Integer.toHexString(0x0100 + (bytes[i] & 0x00FF))
                       .substring(1));
    }
    return retString.toString();
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
