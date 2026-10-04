---
title: Multiply two long integers, checking for overflow.
nav: Multiply two long integers...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1038
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Multiplytwolongintegerscheckingforoverflow.htm
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
 */publicclass Main {
  /**
   *
   * @param a first value
   * @param b second value
   * @return the product <code>a * b</code>
   * @throws ArithmeticException if the result can not be represented as an
   *         long
   * @since 1.2
   */publicstaticlong mulAndCheck(long a, long b) {
      long ret;
      String msg = "overflow: multiply";
      if (a > b) {
          // use symmetry to reduce boundry cases
          ret = mulAndCheck(b, a);
      } else {
          if (a < 0) {
              if (b < 0) {
                  // check for positive overflow with negative a, negative b
if (a >= Long.MAX_VALUE / b) {
                      ret = a * b;
                  } else {
                      thrownew ArithmeticException(msg);
                  }
              } elseif (b > 0) {
                  // check for negative overflow with negative a, positive b
if (Long.MIN_VALUE / b <= a) {
                      ret = a * b;
                  } else {
                      thrownew ArithmeticException(msg);
                  }
              } else {
                  // assert b == 0
                  ret = 0;
              }
          } elseif (a > 0) {
              // assert a > 0
// assert b > 0
// check for positive overflow with positive a, positive b
if (a <= Long.MAX_VALUE / b) {
                  ret = a * b;
              } else {
                  thrownew ArithmeticException(msg);
              }
          } else {
              // assert a == 0
              ret = 0;
          }
      }
      return ret;
  }
}
```
