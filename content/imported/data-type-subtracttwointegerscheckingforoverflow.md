---
title: Subtract two integers, checking for overflow.
nav: Subtract two integers, che...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1334
source: https://web.archive.org/web/20140829093947/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Subtracttwointegerscheckingforoverflow.htm
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
   * Subtract two integers, checking for overflow.
   *
   * @param x the minuend
   * @param y the subtrahend
   * @return the difference <code>x-y</code>
   * @throws ArithmeticException if the result can not be represented as an
   *         int
   * @since 1.1
   */
  public static int subAndCheck(int x, int y) {
      long s = (long)x - (long)y;
      if (s < Integer.MIN_VALUE || s > Integer.MAX_VALUE) {
          throw new ArithmeticException("overflow: subtract");
      }
      return (int)s;
  }
}
```

| 2.3.1. | Integer Data Types in Java: memory and length |
|---|---|
| 2.3.2. | Integer Calculations |
| 2.3.3. | Add two integers, checking for overflow. |
| 2.3.4. | Multiply two integers, checking for overflow. |
| 2.3.5. | Subtract two integers, checking for overflow. |
| 2.3.6. | Binary and Decimal value table |
| 2.3.7. | Min and Max values of datatype int |
| 2.3.8. | Hexadecimal Numbers and its corresponding Decimal and binary value |
| 2.3.9. | Gets the maximum of three int values. |
| 2.3.10. | Gets the minimum of three int values. |
| 2.3.11. | Given an integer, return a string that is in an approximate, but human readable format |
| 2.3.12. | int array to byte array |
