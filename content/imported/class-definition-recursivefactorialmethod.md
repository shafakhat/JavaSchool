---
title: Recursive factorial method
nav: Recursive factorial method
description: System.out.printf("%d! = %d\n", counter, factorial(counter));
section: Imported - java2s Archive
order: 1297
source: https://web.archive.org/web/20140829085523/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Recursivefactorialmethod.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String args[]) {
    for (int counter = 0; counter <= 10; counter++)
      System.out.printf("%d! = %d\n", counter, factorial(counter));
  }
  // recursive declaration of method factorial
  public static long factorial(long number) {
    if (number <= 1) // test for base case
      return 1; // base cases: 0! = 1 and 1! = 1
    else
      // recursion step
      return number * factorial(number - 1);
  }
}
java title=Example.java
0! = 1
1! = 1
2! = 2
3! = 6
4! = 24
5! = 120
6! = 720
7! = 5040
8! = 40320
9! = 362880
10! = 3628800
```
