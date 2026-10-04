---
title: Add two long integers, checking for overflow.
nav: Add two long integers, che...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1122
source: https://web.archive.org/web/20090904105500/http://www.java2s.com:80/Code/Java/Data-Type/Addtwolongintegerscheckingforoverflow.htm
---
```java title=Example.java
import java.io.File;
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
   *
   * @param a an addend
   * @param b an addend
   * @return the sum <code>a+b</code>
   * @throws ArithmeticException if the result can not be represented as an
   *         long
   * @since 1.2
   */
  public static long addAndCheck(long a, long b) {
      return addAndCheck(a, b, "overflow: add");
  }
  /**
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

1.  Long class creates primitives that wrap themselves around data items of the long data type
---  ---
2.  Calculate factorial of integers up to this value
3.  Min and Max values of datatype long
4.  Java long Example: long is 64 bit signed type
5.  Convert Java String to Long example
6.  Use toString method of Long class to convert Long into String.
7.  Convert long primitive to Long object Example
8.  Convert Long to numeric primitive data types example
9.  Create a Long object
10.  Convert String to long Example
11.  Compare Two Java long Arrays Example
12.  Java Sort long Array Example
13.  Convert bytes to megabytes
14.  Converting a String to a long type Number
15.  Convert from String to long
16.  Convert from long to String
17.  Compute prime numbers
18.  Returns the sign for long value x
19.  Gets the maximum of three long values.
20.  Gets the minimum of three long values.
21.  A utility class for converting a long into a human readable string.
