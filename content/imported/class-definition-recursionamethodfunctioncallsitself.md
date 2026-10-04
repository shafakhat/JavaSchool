---
title: Recursion
nav: Recursion
description: Method calls itself. When it calls itself, it solves a smaller problem. There is a smallest problem that the routine can solve it, and return, without calling itself.
section: Imported - java2s Archive
order: 1219
source: https://web.archive.org/web/20140829085847/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Recursionamethodfunctioncallsitself.htm
---
Characteristics of Recursive Methods:
Method calls itself. When it calls itself, it solves a smaller problem. There is a smallest problem that the routine can solve it, and return, without calling itself.

```java title=Example.java
public class MainClass {
  public static void main(String[] args) {
    int theAnswer = triangle(12);
    System.out.println("Triangle=" + theAnswer);
  }
  public static int triangle(int n) {
    if (n == 1)
      return 1;
    else
      return (n + triangle(n - 1));
  }
}
java title=Example.java
Triangle=78
```
