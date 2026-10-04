---
title: Testing the Math class methods
nav: Testing the Math class met...
description: System.out.printf( "Math.abs( 23.7 ) = %f\n", Math.abs( 23.7 ) );
section: Imported - java2s Archive
order: 1677
source: https://web.archive.org/web/20140807033541/http://www.java2s.com/Tutorial/Java/0120__Development/TestingtheMathclassmethods.htm
---
```java title=Example.java
public class MainClass
{
   public static void main( String args[] )
   {
      System.out.printf( "Math.abs( 23.7 ) = %f\n", Math.abs( 23.7 ) );
      System.out.printf( "Math.abs( 0.0 ) = %f\n", Math.abs( 0.0 ) );
      System.out.printf( "Math.abs( -23.7 ) = %f\n", Math.abs( -23.7 ) );
      System.out.printf( "Math.ceil( 9.2 ) = %f\n", Math.ceil( 9.2 ) );
      System.out.printf( "Math.ceil( -9.8 ) = %f\n", Math.ceil( -9.8 ) );
      System.out.printf( "Math.cos( 0.0 ) = %f\n", Math.cos( 0.0 ) );
      System.out.printf( "Math.exp( 1.0 ) = %f\n", Math.exp( 1.0 ) );
      System.out.printf( "Math.exp( 2.0 ) = %f\n", Math.exp( 2.0 ) );
      System.out.printf( "Math.floor( 9.2 ) = %f\n", Math.floor( 9.2 ) );
      System.out.printf( "Math.floor( -9.8 ) = %f\n", Math.floor( -9.8 ) );
      System.out.printf( "Math.log( Math.E ) = %f\n", Math.log( Math.E ) );
      System.out.printf( "Math.log( Math.E * Math.E ) = %f\n", Math.log( Math.E * Math.E ) );
      System.out.printf( "Math.max( 2.3, 12.7 ) = %f\n",Math.max( 2.3, 12.7 ) );
      System.out.printf( "Math.max( -2.3, -12.7 ) = %f\n",Math.max( -2.3, -12.7 ) );
      System.out.printf( "Math.min( 2.3, 12.7 ) = %f\n",Math.min( 2.3, 12.7 ) );
      System.out.printf( "Math.min( -2.3, -12.7 ) = %f\n",Math.min( -2.3, -12.7 ) );
      System.out.printf( "Math.pow( 2.0, 7.0 ) = %f\n",Math.pow( 2.0, 7.0 ) );
      System.out.printf( "Math.pow( 9.0, 0.5 ) = %f\n", Math.pow( 9.0, 0.5 ) );
      System.out.printf( "Math.sin( 0.0 ) = %f\n", Math.sin( 0.0 ) );
      System.out.printf( "Math.sqrt( 900.0 ) = %f\n", Math.sqrt( 900.0 ) );
      System.out.printf( "Math.sqrt( 9.0 ) = %f\n", Math.sqrt( 9.0 ) );
      System.out.printf( "Math.tan( 0.0 ) = %f\n", Math.tan( 0.0 ) );
   }
}
java title=Example.java
Math.abs( 23.7 ) = 23.700000
Math.abs( 0.0 ) = 0.000000
Math.abs( -23.7 ) = 23.700000
Math.ceil( 9.2 ) = 10.000000
Math.ceil( -9.8 ) = -9.000000
Math.cos( 0.0 ) = 1.000000
Math.exp( 1.0 ) = 2.718282
Math.exp( 2.0 ) = 7.389056
Math.floor( 9.2 ) = 9.000000
Math.floor( -9.8 ) = -10.000000
Math.log( Math.E ) = 1.000000
Math.log( Math.E * Math.E ) = 2.000000
Math.max( 2.3, 12.7 ) = 12.700000
Math.max( -2.3, -12.7 ) = -2.300000
Math.min( 2.3, 12.7 ) = 2.300000
Math.min( -2.3, -12.7 ) = -12.700000
Math.pow( 2.0, 7.0 ) = 128.000000
Math.pow( 9.0, 0.5 ) = 3.000000
Math.sin( 0.0 ) = 0.000000
Math.sqrt( 900.0 ) = 30.000000
Math.sqrt( 9.0 ) = 3.000000
Math.tan( 0.0 ) = 0.000000
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
