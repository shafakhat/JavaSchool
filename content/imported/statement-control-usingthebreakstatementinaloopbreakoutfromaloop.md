---
title: Using the break Statement in a Loop
nav: Using the break Statement ...
description: Imported from the java2s.com archive: Using the break Statement in a Loop
section: Imported - java2s Archive
order: 1190
source: https://web.archive.org/web/20140829093242/http://www.java2s.com/Tutorial/Java/0080__Statement-Control/UsingthebreakStatementinaLoopbreakoutfromaloop.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String[] args) {
    int count = 50;
    for (int j = 1; j < count; j++) {
      if (count % j == 0) {
        System.out.println("Breaking!!");
        break;
      }
    }
  }
}
java title=Example.java
Breaking!!
```
