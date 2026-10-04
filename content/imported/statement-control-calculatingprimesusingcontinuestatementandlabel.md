---
title: Calculating Primes
nav: Calculating Primes
description: continue may be followed by a label to identify which enclosing loop to continue to.
section: Imported - java2s Archive
order: 1187
source: https://web.archive.org/web/20140829084545/http://www.java2s.com/Tutorial/Java/0080__Statement-Control/CalculatingPrimesusingcontinuestatementandlabel.htm
---
continue may be followed by a label to identify which enclosing loop to continue to.

```java title=Example.java
public class MainClass {
  public static void main(String[] args) {
    int nValues = 50;
    OuterLoop: for (int i = 2; i <= nValues; i++) {
      for (int j = 2; j < i; j++) {
        if (i % j == 0) {
          continue OuterLoop;
        }
      }
      System.out.println(i);
    }
  }
}
java title=Example.java
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
```
