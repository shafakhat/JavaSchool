---
title: Recursion
nav: Recursion
description: System.out.println("7.5 to the power 5 is " + power(7.5, 5));
section: Imported - java2s Archive
order: 1221
source: https://web.archive.org/web/20140829085458/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Recursionanotherexample.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String[] args) {
    double x = 5.0;
    System.out.println(x + " to the power 4 is " + power(x, 4));
    System.out.println("7.5 to the power 5 is " + power(7.5, 5));
    System.out.println("7.5 to the power 0 is " + power(7.5, 0));
    System.out.println("10 to the power -2 is " + power(10, -2));
  }
  // Raise x to the power n
  static double power(double x, int n) {
    if (n > 1)
      return x * power(x, n - 1); // Recursive call
    else if (n < 0)
      return 1.0 / power(x, -n); // Negative power of x
    else
      return x;
  }
}
```
