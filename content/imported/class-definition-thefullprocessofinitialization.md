---
title: The full process of initialization
nav: The full process of initia...
description: private static int x1 = print("static Insect.x1 initialized");
section: Imported - java2s Archive
order: 1258
source: https://web.archive.org/web/20140829090553/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Thefullprocessofinitialization.htm
---
```java title=Example.java
class Insect {
  private int i = 1;
  protected int j;
  Insect() {
    System.out.println("i = " + i + ", j = " + j);
    j = 1;
  }
  private static int x1 = print("static Insect.x1 initialized");
  static int print(String s) {
    System.out.println(s);
    return 0;
  }
}
class Beetle extends Insect {
  private int k = print("Beetle.k initialized");
  public Beetle() {
    System.out.println("k = " + k);
    System.out.println("j = " + j);
  }
  private static int x2 = print("static Beetle.x2 initialized");
}
public class MainClass {
  public static void main(String[] args) {
    Beetle b = new Beetle();
  }
}
java title=Example.java
static Insect.x1 initialized
static Beetle.x2 initialized
i = 1, j = 0
Beetle.k initialized
k = 0
j = 1
```
