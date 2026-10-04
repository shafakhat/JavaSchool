---
title: Passing objects to methods
nav: Passing objects to methods
description: Imported from the java2s.com archive: Passing objects to methods
section: Imported - java2s Archive
order: 1216
source: https://web.archive.org/web/20140829080359/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Passingobjectstomethods.htm
---
```java title=Example.java
class Letter {
  char c;
}
public class MainClass {
  static void f(Letter y) {
    y.c = 'z';
  }
  public static void main(String[] args) {
    Letter x = new Letter();
    x.c = 'a';
    System.out.println("1: x.c: " + x.c);
    f(x);
    System.out.println("2: x.c: " + x.c);
  }
}
java title=Example.java
1: x.c: a
2: x.c: z
```
