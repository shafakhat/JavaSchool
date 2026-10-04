---
title: The Labeled continue statement
nav: The Labeled continue state...
description: Imported from the java2s.com archive: The Labeled continue statement
section: Imported - java2s Archive
order: 1185
source: https://web.archive.org/web/20140829090306/http://www.java2s.com/Tutorial/Java/0080__Statement-Control/TheLabeledcontinuestatement.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String[] args) {
    int limit = 20;
    int factorial = 1;
    OuterLoop: for (int i = 1; i <= limit; i++) {
      factorial = 1;
      for (int j = 2; j <= i; j++) {
        if (i > 10 && i % 2 == 1) {
          continue OuterLoop;
        }
        factorial *= j;
      }
      System.out.println(i + "! is " + factorial);
    }
  }
}
java title=Example.java
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
12! is 479001600
14! is 1278945280
16! is 2004189184
18! is -898433024
20! is -2102132736
```
