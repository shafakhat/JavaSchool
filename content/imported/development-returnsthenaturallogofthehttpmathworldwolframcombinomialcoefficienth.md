---
title: Returns the natural log of the (http
nav: Returns the natural log of...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1702
source: https://web.archive.org/web/20140829081902/http://www.java2s.com/Tutorial/Java/0120__Development/ReturnsthenaturallogofthehttpmathworldwolframcomBinomialCoefficienthtmlBinomialCoefficient.htm
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
   * Returns the natural <code>log</code> of the <a
   * href="http://mathworld.wolfram.com/BinomialCoefficient.html"> Binomial
   * Coefficient</a>, "<code>n choose k</code>", the number of
   * <code>k</code>-element subsets that can be selected from an
   * <code>n</code>-element set.
   *
   * <Strong>Preconditions</strong>:
   * <ul>
   * <li> <code>0 <= k <= n </code> (otherwise
   * <code>IllegalArgumentException</code> is thrown)</li>
   * </ul>
   *
   * @param n the size of the set
   * @param k the size of the subsets to be counted
   * @return <code>n choose k</code>
   * @throws IllegalArgumentException if preconditions are not met.
   */
  public static double binomialCoefficientLog(final int n, final int k) {
      if (n < k) {
          throw new IllegalArgumentException(
              "must have n >= k for binomial coefficient (n,k)");
      }
      if (n < 0) {
          throw new IllegalArgumentException(
              "must have n >= 0 for binomial coefficient (n,k)");
      }
      if ((n == k) || (k == 0)) {
          return 0;
      }
      if ((k == 1) || (k == n - 1)) {
          return Math.log((double)n);
      }
      double logSum = 0;
      // n!/k!
      for (int i = k + 1; i <= n; i++) {
          logSum += Math.log((double)i);
      }
      // divide by (n-k)!
      for (int i = 2; i <= n - k; i++) {
          logSum -= Math.log((double)i);
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
