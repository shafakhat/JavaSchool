---
title: For a float value x, this method returns +1.0F if x >= 0 and -1.0F if x < 0. Returns NaN if x is NaN.
nav: For a float value x, this ...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1167
source: https://web.archive.org/web/20140829080338/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Forafloatvaluexthismethodreturns10Fifx0and10Fifx0ReturnsNaNifxisNaN.htm
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
   * For a float value x, this method returns +1.0F if x >= 0 and -1.0F if x <
   * 0. Returns <code>NaN</code> if <code>x</code> is <code>NaN</code>.
   *
   * @param x the value, a float
   * @return +1.0F or -1.0F, depending on the sign of x
   */
  public static float indicator(final float x) {
      if (Float.isNaN(x)) {
          return Float.NaN;
      }
      return (x >= 0.0F) ? 1.0F : -1.0F;
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
