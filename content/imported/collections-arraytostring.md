---
title: Array To String
nav: Array To String
description: * or more contributor license agreements. See the NOTICE file
section: Imported - java2s Archive
order: 1047
source: https://web.archive.org/web/20100222015853/http://www.java2s.com:80/Tutorial/Java/0140__Collections/ArrayToString.htm
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
   * Given an array of strings, return a comma-separated list of its elements.
   * @param strs Array of strings
   * @return Empty string if strs.length is 0, comma separated list of strings
   * otherwise
   */
  public static String arrayToString(String[] strs) {
    if (strs.length == 0) { return ""; }
    StringBuffer sbuf = new StringBuffer();
    sbuf.append(strs[0]);
    for (int idx = 1; idx < strs.length; idx++) {
      sbuf.append(",");
      sbuf.append(strs[idx]);
    }
    return sbuf.toString();
  }
}
```
