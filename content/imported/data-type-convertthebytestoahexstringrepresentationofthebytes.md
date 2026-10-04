---
title: Convert the bytes to a hex string representation of the bytes
nav: Convert the bytes to a hex...
description: * or more contributor license agreements. See the NOTICE file
section: Imported - java2s Archive
order: 1013
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Convertthebytestoahexstringrepresentationofthebytes.htm
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
 */import java.io.PrintWriter;
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
 */public class StringUtils {
  final public static char COMMA = ',';
  final public static String COMMA_STR = ",";
  final public static char ESCAPE_CHAR = '\\';
  private static DecimalFormat oneDecimal = new DecimalFormat("0.0");
  /**
   * Given an array of bytes it will convert the bytes to a hex string
   * representation of the bytes
   * @param bytes
   * @return hex string representation of the byte array
   */ public static String byteToHexString(byte bytes[]) {
    StringBuffer retString = new StringBuffer();
    for (int i = 0; i < bytes.length; ++i) {
      retString.append(Integer.toHexString(0x0100 + (bytes[i] & 0x00FF))
                       .substring(1));
    }
    return retString.toString();
  }
}
```
