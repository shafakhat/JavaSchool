---
title: Compares two floats for order.
nav: Compares two floats for or...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1367
source: https://web.archive.org/web/20140829080532/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Comparestwofloatsfororder.htm
---
```java title=Example.java
import java.math.BigDecimal;
import java.math.BigInteger;
/**
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
/**
 * Provides extra functionality for Java Number classes.
 *
 * @author <a href="mailto:rand_mcneely@yahoo.com">Rand McNeely</a>
 * @author Stephen Colebourne
 * @author <a href="mailto:steve.downey@netfolio.com">Steve Downey</a>
 * @author Eric Pugh
 * @author Phil Steitz
 * @since 1.0
 * @version $Id: NumberUtils.java 488819 2006-12-19 21:50:04Z bayard $
 *
 */
public class Main {
  /**
   *
   * This method is more comprehensive than the standard Java greater than,
   * less than and equals operators.
   * <ul>
   *  <li>It returns <code>-1</code> if the first value is less than the second.
   *  <li>It returns <code>+1</code> if the first value is greater than the second.
   *  <li>It returns <code>0</code> if the values are equal.
   * </ul>
   *
   *  The ordering is as follows, largest to smallest:
   * <ul>
   * <li>NaN
   * <li>Positive infinity
   * <li>Maximum float
   * <li>Normal positive numbers
   * <li>+0.0
   * <li>-0.0
   * <li>Normal negative numbers
   * <li>Minimum float (-Float.MAX_VALUE)
   * <li>Negative infinity
   * </ul>
   *
   * Comparing <code>NaN</code> with <code>NaN</code> will return
   * <code>0</code>.
   *
   * @param lhs  the first <code>float</code>
   * @param rhs  the second <code>float</code>
   * @return <code>-1</code> if lhs is less, <code>+1</code> if greater,
   *  <code>0</code> if equal to rhs
   */
  public static int compare(float lhs, float rhs) {
      if (lhs < rhs) {
          return -1;
      }
      if (lhs > rhs) {
          return +1;
      }
      //Need to compare bits to handle 0.0 == -0.0 being true
      // compare should put -0.0 < +0.0
      // Two NaNs are also == for compare purposes
      // where NaN == NaN is false
      int lhsBits = Float.floatToIntBits(lhs);
      int rhsBits = Float.floatToIntBits(rhs);
      if (lhsBits == rhsBits) {
          return 0;
      }
      //Something exotic! A comparison to NaN or 0.0 vs -0.0
      //Fortunately NaN's int is > than everything else
      //Also negzeros bits < poszero
      //NAN: 2143289344
      //MAX: 2139095039
      //NEGZERO: -2147483648
      if (lhsBits < rhsBits) {
          return -1;
      } else {
          return +1;
      }
  }
}
```

| 2.11.1. | Java float is 32 bit single precision type and used when fractional precision calculation is required. |
|---|---|
| 2.11.2. | Floating­Point Types |
| 2.11.3. | Min and Max values of data type float |
| 2.11.4. | Use Float constructor to convert float primitive type to a Float object. |
| 2.11.5. | Java Float Comparison |
| 2.11.6. | Java Float isInfinite Method |
| 2.11.7. | Java Float isNaN Method |
| 2.11.8. | Java Float Wrapper Class |
| 2.11.9. | Pass floats as string literals to a method |
| 2.11.10. | Check if a string is a valid number |
| 2.11.11. | Use toString method of Float class to convert Float into String. |
| 2.11.12. | Declaring a variable of type float |
| 2.11.13. | Declaring more than one float variable in a single statement |
| 2.11.14. | Use Float.valueOf to convert string value to float |
| 2.11.15. | Convert Java Float to Numeric Primitive Data Types |
| 2.11.16. | Convert Java String to Float Object |
| 2.11.17. | Convert from float to String |
| 2.11.18. | Convert from String to float |
| 2.11.19. | Converting a String to a float type Number |
| 2.11.20. | Compare Two Java float Arrays |
| 2.11.21. | Compares two floats for order. |
| 2.11.22. | For a float value x, this method returns +1.0F if x >= 0 and -1.0F if x < 0. Returns NaN if x is NaN. |
| 2.11.23. | Tests two float arrays for equality. |
| 2.11.24. | Use System.out.printf to format float point number |
