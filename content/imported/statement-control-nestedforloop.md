---
title: Nested for Loop
nav: Nested for Loop
description: Imported from the java2s.com archive: Nested for Loop
section: Imported - java2s Archive
order: 1007
source: https://web.archive.org/web/20070716023441/http://www.java2s.com:80/Tutorial/Java/0080__Statement-Control/NestedforLoop.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String[] args) {
    long limit = 20L;
    long factorial = 1L;
    for (long i = 1L; i <= limit; i++) {
      factorial = 1L;
      for (long factor = 2; factor <= i; factor++) {
        factorial *= factor;
      }
      System.out.println(i + "! is " + factorial);
    }
  }
}
```

```java title=Example.java
1! is 1
2! is 2
3! is 6
4! is 24
5! is 120
6! is 720
7! is 5040
8! is 40320
9! is 362880
10! is 3628800
11! is 39916800
12! is 479001600
13! is 6227020800
14! is 87178291200
15! is 1307674368000
16! is 20922789888000
17! is 355687428096000
18! is 6402373705728000
19! is 121645100408832000
20! is 2432902008176640000
```
