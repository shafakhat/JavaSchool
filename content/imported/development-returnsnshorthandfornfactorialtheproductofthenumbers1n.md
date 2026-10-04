---
title: Returns n!. Shorthand for n Factorial, the product of the numbers 1,...,n.
nav: Returns n!. Shorthand for ...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1709
source: https://web.archive.org/web/20140807032727/http://www.java2s.com/Tutorial/Java/0120__Development/ReturnsnShorthandfornFactorialtheproductofthenumbers1n.htm
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
   * Returns n!. Shorthand for <code>n</code> <a
   * href="http://mathworld.wolfram.com/Factorial.html"> Factorial</a>, the
   * product of the numbers <code>1,...,n</code>.
   *
   * <Strong>Preconditions</strong>:
   * <ul>
   * <li> <code>n >= 0</code> (otherwise
   * <code>IllegalArgumentException</code> is thrown)</li>
   * <li> The result is small enough to fit into a <code>long</code>. The
   * largest value of <code>n</code> for which <code>n!</code> <
   * Long.MAX_VALUE</code> is 20. If the computed value exceeds <code>Long.MAX_VALUE</code>
   * an <code>ArithMeticException </code> is thrown.</li>
   * </ul>
   *
   *
   * @param n argument
   * @return <code>n!</code>
   * @throws ArithmeticException if the result is too large to be represented
   *         by a long integer.
   * @throws IllegalArgumentException if n < 0
   */
  public static long factorial(final int n) {
      long result = Math.round(factorialDouble(n));
      if (result == Long.MAX_VALUE) {
          throw new ArithmeticException(
              "result too large to represent in a long integer");
      }
      return result;
  }
  /**
   * Returns n!. Shorthand for <code>n</code> <a
   * href="http://mathworld.wolfram.com/Factorial.html"> Factorial</a>, the
   * product of the numbers <code>1,...,n</code> as a <code>double</code>.
   *
   * <Strong>Preconditions</strong>:
   * <ul>
   * <li> <code>n >= 0</code> (otherwise
   * <code>IllegalArgumentException</code> is thrown)</li>
   * <li> The result is small enough to fit into a <code>double</code>. The
   * largest value of <code>n</code> for which <code>n!</code> <
   * Double.MAX_VALUE</code> is 170. If the computed value exceeds
   * Double.MAX_VALUE, Double.POSITIVE_INFINITY is returned</li>
   * </ul>
   *
   *
   * @param n argument
   * @return <code>n!</code>
   * @throws IllegalArgumentException if n < 0
   */
  public static double factorialDouble(final int n) {
      if (n < 0) {
          throw new IllegalArgumentException("must have n >= 0 for n!");
      }
      return Math.floor(Math.exp(factorialLog(n)) + 0.5);
  }
  /**
   * Returns the natural logarithm of n!.
   *
   * <Strong>Preconditions</strong>:
   * <ul>
   * <li> <code>n >= 0</code> (otherwise
   * <code>IllegalArgumentException</code> is thrown)</li>
   * </ul>
   *
   * @param n argument
   * @return <code>n!</code>
   * @throws IllegalArgumentException if preconditions are not met.
   */
  public static double factorialLog(final int n) {
      if (n < 0) {
          throw new IllegalArgumentException("must have n > 0 for n!");
      }
      double logSum = 0;
      for (int i = 2; i <= n; i++) {
          logSum += Math.log((double)i);
      }
      return logSum;
  }
}
```

| 6.17.1. | Math Class Methods |
|---|---|
| 6.17.2. | Use math functions |
| 6.17.3. | Testing the Math class methods |
| 6.17.4. | Floating Point Number Enhancements in JDK 6 |
| 6.17.5. | Math.scalb |
| 6.17.6. | Math.getExponent |
| 6.17.7. | Math.nextAfter |
| 6.17.8. | Math.nextUp |
| 6.17.9. | Math.copySign |
| 6.17.10. | Demonstrate toDegrees() and toRadians(). |
| 6.17.11. | Find absolute value of float, int, double and long using Math.abs |
| 6.17.12. | Find ceiling value of a number using Math.ceil |
| 6.17.13. | Find exponential value of a number using Math.exp |
| 6.17.14. | Find floor value of a number using Math.floor |
| 6.17.15. | Find maximum of two numbers using Math.max |
| 6.17.16. | Find natural logarithm value of a number using Math.log |
| 6.17.17. | Find power using Math.pow |
| 6.17.18. | Find square root of a number using Math.sqrt |
| 6.17.19. | Round Java float and double numbers using Math.round |
| 6.17.20. | Math.min |
| 6.17.21. | Normalizes an angle to a relative angle. |
| 6.17.22. | Normalizes an angle to an absolute angle. |
| 6.17.23. | Normalizes an angle to be near an absolute angle |
| 6.17.24. | Calculate the floor of the log, base 2 |
| 6.17.25. | Greatest Common Divisor (GCD) of positive integer numbers |
| 6.17.26. | Least Common Multiple (LCM) of two strictly positive integer numbers |
| 6.17.27. | Moving Average |
| 6.17.28. | Normalize an angle in a 2&pi wide interval around a center value. |
| 6.17.29. | Returns n!. Shorthand for n Factorial, the product of the numbers 1,...,n as a double. |
| 6.17.30. | Returns n!. Shorthand for n Factorial, the product of the numbers 1,...,n. |
| 6.17.31. | Returns the hyperbolic cosine of x. |
| 6.17.32. | Returns the hyperbolic sine of x. |
| 6.17.33. | Returns the natural log of the (http://mathworld.wolfram.com/BinomialCoefficient.html) Binomial Coefficient |
| 6.17.34. | Returns the natural logarithm of n!. |
| 6.17.35. | Round the given value to the specified number of decimal places. The value is rounded using the BigDecimal.ROUND_HALF_UP method. |
| 6.17.36. | Value is rounded using the given method which is any method defined in BigDecimal |
| 6.17.37. | sqrt(a^2 + b^2) without under/overflow |
