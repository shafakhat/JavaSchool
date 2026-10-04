---
title: Recursive fibonacci method
nav: Recursive fibonacci method
description: System.out.printf("Fibonacci of %d is: %d\n", counter, fibonacci(counter));
section: Imported - java2s Archive
order: 1222
source: https://web.archive.org/web/20140829085856/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Recursivefibonaccimethod.htm
---
```java title=Example.java
public class MainClass {
  // recursive declaration of method fibonacci
  public static long fibonacci(long number) {
    if ((number == 0) || (number == 1)) // base cases
      return number;
    else
      // recursion step
      return fibonacci(number - 1) + fibonacci(number - 2);
  }
  public static void main(String[] args) {
    for (int counter = 0; counter <= 10; counter++)
      System.out.printf("Fibonacci of %d is: %d\n", counter, fibonacci(counter));
  }
}
java title=Example.java
Fibonacci of 0 is: 0
Fibonacci of 1 is: 1
Fibonacci of 2 is: 1
Fibonacci of 3 is: 2
Fibonacci of 4 is: 3
Fibonacci of 5 is: 5
Fibonacci of 6 is: 8
Fibonacci of 7 is: 13
Fibonacci of 8 is: 21
Fibonacci of 9 is: 34
Fibonacci of 10 is: 55
```
