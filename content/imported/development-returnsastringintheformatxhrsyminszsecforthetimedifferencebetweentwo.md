---
title: Returns a String in the format Xhrs, Ymins, Z sec, for the time difference between two times
nav: Returns a String in the fo...
description: * or more contributor license agreements. See the NOTICE file
section: Imported - java2s Archive
order: 1729
source: https://web.archive.org/web/20140829081040/http://www.java2s.com/Tutorial/Java/0120__Development/ReturnsaStringintheformatXhrsYminsZsecforthetimedifferencebetweentwotimes.htm
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
   *
   * Given a finish and start time in long milliseconds, returns a
   * String in the format Xhrs, Ymins, Z sec, for the time difference between two times.
   * If finish time comes before start time then negative valeus of X, Y and Z wil return.
   *
   * @param finishTime finish time
   * @param startTime start time
   */
  public static String formatTimeDiff(long finishTime, long startTime){
    StringBuffer buf = new StringBuffer();
    long timeDiff = finishTime - startTime;
    long hours = timeDiff / (60*60*1000);
    long rem = (timeDiff % (60*60*1000));
    long minutes =  rem / (60*1000);
    rem = rem % (60*1000);
    long seconds = rem / 1000;
    if (hours != 0){
      buf.append(hours);
      buf.append("hrs, ");
    }
    if (minutes != 0){
      buf.append(minutes);
      buf.append("mins, ");
    }
    // return "0sec if no difference
    buf.append(seconds);
    buf.append("sec");
    return buf.toString();
  }
}
```

| 6.20.1. | Compute and display elapsed time of an operation |
|---|---|
| 6.20.2. | Get system time using System class |
| 6.20.3. | Get elapsed time in milliseconds |
| 6.20.4. | Get elapsed time in seconds |
| 6.20.5. | Get elapsed time in minutes |
| 6.20.6. | Get elapsed time in hours |
| 6.20.7. | Get elapsed time in days |
| 6.20.8. | Returns a String in the format Xhrs, Ymins, Z sec, for the time difference between two times |
| 6.20.9. | Returns a formatted String from time |
| 6.20.10. | Convert milliseconds to readable string |
