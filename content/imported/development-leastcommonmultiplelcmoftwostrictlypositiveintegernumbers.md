---
title: Least Common Multiple (LCM) of two strictly positive integer numbers
nav: Least Common Multiple (LCM...
description: * This software module was originally developed by Raphaël Grosbois and
section: Imported - java2s Archive
order: 1699
source: https://web.archive.org/web/20140805222913/http://www.java2s.com/Tutorial/Java/0120__Development/LeastCommonMultipleLCMoftwostrictlypositiveintegernumbers.htm
---
```java title=Example.java
/*
 * $RCSfile: MathUtil.java,v $
 * $Revision: 1.1 $
 * $Date: 2005/02/11 05:02:25 $
 * $State: Exp $
 *
 * Class:                   MathUtil
 *
 * Description:             Utility mathematical methods
 *
 *
 *
 * COPYRIGHT:
 *
 * This software module was originally developed by Raphaël Grosbois and
 * Diego Santa Cruz (Swiss Federal Institute of Technology-EPFL); Joel
 * Askelöf (Ericsson Radio Systems AB); and Bertrand Berthelot, David
 * Bouchard, Félix Henry, Gerard Mozelle and Patrice Onno (Canon Research
 * Centre France S.A) in the course of development of the JPEG2000
 * standard as specified by ISO/IEC 15444 (JPEG 2000 Standard). This
 * software module is an implementation of a part of the JPEG 2000
 * Standard. Swiss Federal Institute of Technology-EPFL, Ericsson Radio
 * Systems AB and Canon Research Centre France S.A (collectively JJ2000
 * Partners) agree not to assert against ISO/IEC and users of the JPEG
 * 2000 Standard (Users) any of their rights under the copyright, not
 * including other intellectual property rights, for this software module
 * with respect to the usage by ISO/IEC and Users of this software module
 * or modifications thereof for use in hardware or software products
 * claiming conformance to the JPEG 2000 Standard. Those intending to use
 * this software module in hardware or software products are advised that
 * their use may infringe existing patents. The original developers of
 * this software module, JJ2000 Partners and ISO/IEC assume no liability
 * for use of this software module or modifications thereof. No license
 * or right to this software module is granted for non JPEG 2000 Standard
 * conforming products. JJ2000 Partners have full right to use this
 * software module for his/her own purpose, assign or donate this
 * software module to any third party and to inhibit third parties from
 * using this software module for non JPEG 2000 Standard conforming
 * products. This copyright notice must be included in all copies or
 * derivative works of this software module.
 *
 * Copyright (c) 1999/2000 JJ2000 Partners.
 * */
/**
 * This class contains a collection of utility methods fro mathematical
 * operations. All methods are static.
 * */
public class MathUtil {
  /**
   * Method that calculates the Least Common Multiple (LCM) of two strictly
   * positive integer numbers.
   *
   * @param x1 First number
   *
   * @param x2 Second number
   * */
  public static final int lcm(int x1,int x2) {
      if(x1<=0 || x2<=0) {
          throw new IllegalArgumentException("Cannot compute the least "+
                                             "common multiple of two "+
                                             "numbers if one, at least,"+
                                             "is negative.");
      }
      int max,min;
      if (x1>x2) {
          max = x1;
          min = x2;
      } else {
          max = x2;
          min = x1;
      }
      for(int i=1; i<=min; i++) {
          if( (max*i)%min == 0 ) {
              return i*max;
          }
      }
      throw new Error("Cannot find the least common multiple of numbers "+
                      x1+" and "+x2);
  }
  /**
   * Method that calculates the Least Common Multiple (LCM) of several
   * positive integer numbers.
   *
   * @param x Array containing the numbers.
   * */
  public static final int lcm(int[] x) {
      if(x.length<2) {
          throw new Error("Do not use this method if there are less than"+
                          " two numbers.");
      }
      int tmp = lcm(x[x.length-1],x[x.length-2]);
      for(int i=x.length-3; i>=0; i--) {
          if(x[i]<=0) {
              throw new IllegalArgumentException("Cannot compute the least "+
                                                 "common multiple of "+
                                                 "several numbers where "+
                                                 "one, at least,"+
                                                 "is negative.");
          }
          tmp = lcm(tmp,x[i]);
      }
      return tmp;
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
