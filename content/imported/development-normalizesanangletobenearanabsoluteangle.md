---
title: Normalizes an angle to be near an absolute angle
nav: Normalizes an angle to be ...
description: /*******************************************************************************
section: Imported - java2s Archive
order: 1693
source: https://web.archive.org/web/20140807033651/http://www.java2s.com/Tutorial/Java/0120__Development/Normalizesanangletobenearanabsoluteangle.htm
---
```java title=Example.java
/*******************************************************************************
 * Copyright (c) 2001, 2008 Mathew A. Nelson and Robocode contributors
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Common Public License v1.0
 * which accompanies this distribution, and is available at
 * http://robocode.sourceforge.net/license/cpl-v10.html
 *
 * Contributors:
 *     Mathew A. Nelson
 *     - Initial API and implementation
 *     Flemming N. Larsen
 *     - Moved all methods to classes like FileUtil, StringUtil, WindowUtil,
 *       Logger etc. exception for the following methods, which have been kept
 *       here as legacy robots make use of these methods:
 *       - normalAbsoluteAngle()
 *       - normalNearAbsoluteAngle()
 *       - normalRelativeAngle()
 *     - The isNear() was made public
 *     - Optimized and provided javadocs for all methods
 *******************************************************************************/
import static java.lang.Math.PI;
import java.util.Random;
/**
 * Utility class that provide methods for normalizing angles.
 *
 * @author Mathew A. Nelson (original)
 * @author Flemming N. Larsen (contributor)
 */
public class Utils {
  private final static double TWO_PI = 2 * PI;
  private final static double THREE_PI_OVER_TWO = 3 * PI / 2;
  private final static double PI_OVER_TWO = PI / 2;
  public static final double NEAR_DELTA = .00001;
  /**
   * The normalized angle will be in the range from 0 to 2*PI, where 2*PI
   * itself is not included.
   * If the normalized angle is near to 0, PI/2, PI, 3*PI/2 or 2*PI, that
   * angle will be returned. The {@link #isNear(double, double) isNear}
   * method is used for defining when the angle is near one of angles listed
   * above.
   *
   * @param angle the angle to normalize
   * @return the normalized angle that will be in the range of [0,2*PI[
   * @see #normalAbsoluteAngle(double)
   * @see #isNear(double, double)
   */
  public static double normalNearAbsoluteAngle(double angle) {
    angle = (angle %= TWO_PI) >= 0 ? angle : (angle + TWO_PI);
    if (isNear(angle, PI)) {
      return PI;
    } else if (angle < PI) {
      if (isNear(angle, 0)) {
        return 0;
      } else if (isNear(angle, PI_OVER_TWO)) {
        return PI_OVER_TWO;
      }
    } else {
      if (isNear(angle, THREE_PI_OVER_TWO)) {
        return THREE_PI_OVER_TWO;
      } else if (isNear(angle, TWO_PI)) {
        return 0;
      }
    }
    return angle;
  }
  /**
   * Tests if the two {@code double} values are near to each other.
   * It is recommended to use this method instead of testing if the two
   * doubles are equal using an this expression: {@code value1 == value2}.
   * The reason being, that this expression might never become
   * {@code true} due to the precision of double values.
   * Whether or not the specified doubles are near to each other is defined by
   * the following expression:
   * {@code (Math.abs(value1 - value2) < .00001)}
   *
   * @param value1 the first double value
   * @param value2 the second double value
   * @return {@code true} if the two doubles are near to each other;
   *         {@code false} otherwise.
   */
  public static boolean isNear(double value1, double value2) {
    return (Math.abs(value1 - value2) < NEAR_DELTA);
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
