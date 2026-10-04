---
title: Breaking Indefinite Loops
nav: Breaking Indefinite Loops
description: Imported from the java2s.com archive: Breaking Indefinite Loops
section: Imported - java2s Archive
order: 1191
source: https://web.archive.org/web/20140829091017/http://www.java2s.com/Tutorial/Java/0080__Statement-Control/BreakingIndefiniteLoops.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String[] args) {
    OuterLoop: for (int i = 2;; i++) {
      for (int j = 2; j < i; j++) {
        if (i % j == 0) {
          continue OuterLoop;
        }
      }
      System.out.println(i);
      if (i == 107) {
        break;
      }
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
53
59
61
67
71
73
79
83
89
97
101
103
107
```
