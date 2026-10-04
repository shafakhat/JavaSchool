---
title: Subtract two long integers, checking for overflow.
nav: Subtract two long integers...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1120
source: https://web.archive.org/web/20090912060605/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/Subtracttwolongintegerscheckingforoverflow.htm
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
