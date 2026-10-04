---
title: Multiply two integers, checking for overflow.
nav: Multiply two integers, che...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1156
source: https://web.archive.org/web/20100719201956/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/Multiplytwointegerscheckingforoverflow.htm
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
   * Multiply two integers, checking for overflow.
   *
   * @param x a factor
   * @param y a factor
   * @return the product <code>x*y</code>
   * @throws ArithmeticException if the result can not be represented as an
   *         int
   * @since 1.1
   */
  public static int mulAndCheck(int x, int y) {
      long m = ((long)x) * ((long)y);
      if (m < Integer.MIN_VALUE || m > Integer.MAX_VALUE) {
          throw new ArithmeticException("overflow: mul");
      }
      return (int)m;
  }
}
```
