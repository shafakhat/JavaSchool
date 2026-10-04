---
title: Add two integers, checking for overflow.
nav: Add two integers, checking...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1121
source: https://web.archive.org/web/20091107101831/http://www.java2s.com:80/Code/Java/Data-Type/Addtwointegerscheckingforoverflow.htm
---
Add two integers, checking for overflow.

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
   * Add two integers, checking for overflow.
   *
   * @param x an addend
   * @param y an addend
   * @return the sum <code>x+y</code>
   * @throws ArithmeticException if the result can not be represented as an
   *         int
   * @since 1.1
   */
  public static int addAndCheck(int x, int y) {
      long s = (long)x + (long)y;
      if (s < Integer.MIN_VALUE || s > Integer.MAX_VALUE) {
          throw new ArithmeticException("overflow: add");
      }
      return (int)s;
  }
}
```

1.  Java int:int is 32 bit signed type ranges from 2,147,483,648 to 2,147,483,647.
---  ---
2.  Integer class creates primitives that wrap themselves around data items of the int data type
3.  Rolling the Dice
4.  Are all hex integers negative
5.  Int Overflow
6.  Multiply a decimal fraction, not using floating point
7.  The Integer class cannot be changed
8.  Demonstrate a type wrapper.
9.  Autoboxing/unboxing int
10.  Getting a Valid Integer
11.  Convert string to integer
12.  Integer.toBinaryString
13.  Convert octal number to decimal number
14.  Convert binary number to decimal number
15.  Convert decimal integer to octal number
16.  Convert decimal integer to hexadecimal number
17.  Convert hexadecimal number to decimal number
18.  Integer.toHexString
19.  Integer.MIN_VALUE
20.  Java Sort int Array
21.  Compare Two Java int Arrays
22.  Pass an integer by reference
23.  Modifiable Integer
24.  Given an integer, return a string that is in an approximate, but human readable format
25.  Returns the sign for int value x
26.  Gets the maximum of three int values.
27.  Gets the minimum of three int values.
