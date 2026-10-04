---
title: Using || in if statement
nav: Using || in if statement
description: Imported from the java2s.com archive: Using || in if statement
section: Imported - java2s Archive
order: 1018
source: https://web.archive.org/web/20070714012016/http://www.java2s.com:80/Tutorial/Java/0080__Statement-Control/Usinginifstatement.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String[] arg) {
    int value = 8;
    int count = 10;
    int limit = 11;
    if (++value % 2 != 0 || ++count < limit) {
      System.out.println("here");
      System.out.println(value);
      System.out.println(count);
    }
    System.out.println("there");
    System.out.println(value);
    System.out.println(count);
  }
}
```

```java title=Example.java
here
9
10
there
9
10
```
