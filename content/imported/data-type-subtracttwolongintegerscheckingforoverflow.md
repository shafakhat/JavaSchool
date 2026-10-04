---
title: Subtract two long integers, checking for overflow.
nav: Subtract two long integers...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1332
source: https://web.archive.org/web/20140829082745/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Subtracttwolongintegerscheckingforoverflow.htm
---
```java title=Example.java
import java.math.BigDecimal;
/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 *  contributor license agreements.  See the NOTICE file distributed with
 *  this work for additional information regarding copyright ownership.
 *  The ASF licenses this file to You under the Apache License, Version 2.0
 *  (the "License"); you may not use this file except in compliance with
 *  the License.  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS,
 *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *  See the License for the specific language governing permissions and
 *  limitations under the License.
 *
 *
 */
public class Main {
  /**
   * Subtract two long integers, checking for overflow.
   *
   * @param a first value
   * @param b second value
   * @return the difference <code>a-b</code>
   * @throws ArithmeticException if the result can not be represented as an
   *         long
   * @since 1.2
   */
  public static long subAndCheck(long a, long b) {
      long ret;
      String msg = "overflow: subtract";
      if (b == Long.MIN_VALUE) {
          if (a < 0) {
              ret = a - b;
          } else {
              throw new ArithmeticException(msg);
          }
      } else {
          // use additive inverse
          ret = addAndCheck(a, -b, msg);
      }
      return ret;
  }
  /**
   * Add two long integers, checking for overflow.
   *
   * @param a an addend
   * @param b an addend
   * @param msg the message to use for any thrown exception.
   * @return the sum <code>a+b</code>
   * @throws ArithmeticException if the result can not be represented as an
   *         long
   * @since 1.2
   */
  private static long addAndCheck(long a, long b, String msg) {
      long ret;
      if (a > b) {
          // use symmetry to reduce boundry cases
          ret = addAndCheck(b, a, msg);
      } else {
          // assert a <= b
          if (a < 0) {
              if (b < 0) {
                  // check for negative overflow
                  if (Long.MIN_VALUE - b <= a) {
                      ret = a + b;
                  } else {
                      throw new ArithmeticException(msg);
                  }
              } else {
                  // oppisite sign addition is always safe
                  ret = a + b;
              }
          } else {
              // assert a >= 0
              // assert b >= 0
              // check for positive overflow
              if (a <= Long.MAX_VALUE - b) {
                  ret = a + b;
              } else {
                  throw new ArithmeticException(msg);
              }
          }
      }
      return ret;
  }
}
```

| 2.8.1. | Long Integer Literal |
|---|---|
| 2.8.2. | Create a Long object |
| 2.8.3. | Add two long integers, checking for overflow. |
| 2.8.4. | Multiply two long integers, checking for overflow. |
| 2.8.5. | Subtract two long integers, checking for overflow. |
| 2.8.6. | Convert Long to numeric primitive data types example |
| 2.8.7. | Convert long primitive to Long object Example |
| 2.8.8. | Compute distance light travels using long variables |
| 2.8.9. | Java long Example: long is 64 bit signed type |
| 2.8.10. | Min and Max values of datatype long |
| 2.8.11. | Gets the maximum of three long values. |
| 2.8.12. | Gets the minimum of three long values. |
| 2.8.13. | Convert Java String to Long example |
| 2.8.14. | Use toString method of Long class to convert Long into String. |
| 2.8.15. | Convert from long to String |
| 2.8.16. | Convert from String to long |
| 2.8.17. | A utility class for converting a long into a human readable string. |
| 2.8.18. | Java Sort long Array Example |
| 2.8.19. | Compare Two Java long Arrays Example |
| 2.8.20. | Format long with System.out.format |
