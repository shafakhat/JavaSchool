---
title: Overloading based on the order of the arguments
nav: Overloading based on the o...
description: Imported from the java2s.com archive: Overloading based on the order of the arguments
section: Imported - java2s Archive
order: 1037
source: https://web.archive.org/web/20070707111841/http://www.java2s.com:80/Tutorial/Java/0100__Class-Definition/Overloadingbasedontheorderofthearguments.htm
---
```java title=Example.java
public class MainClass {
  static void print(String s, int i) {
    System.out.println("String: " + s + ", int: " + i);
  }
  static void print(int i, String s) {
    System.out.println("int: " + i + ", String: " + s);
  }
  public static void main(String[] args) {
    print("String first", 11);
    print(99, "Int first");
  }
}
```

```java title=Example.java
String: String first, int: 11
int: 99, String: Int first
```
