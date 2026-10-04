---
title: Autoboxing/unboxing occurs inside expressions
nav: Autoboxing/unboxing occurs...
description: Imported from the java2s.com archive: Autoboxing/unboxing occurs inside expressions
section: Imported - java2s Archive
order: 1114
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Autoboxingunboxingoccursinsideexpressions.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String args[]) {
    Integer intObject, intObject2;
    int i;
    intObject = 100;
    System.out.println("Original value of iOb: " + intObject);
    ++intObject;
    System.out.println("After ++iOb: " + intObject);
    intObject2 = intObject + (intObject / 3);
    System.out.println("iOb2 after expression: " + intObject2);
    i = intObject + (intObject / 3);
    System.out.println("i after expression: " + i);
  }
}
java title=Example.java
Original value of iOb: 100
After ++iOb: 101
iOb2 after expression: 134
i after expression: 134
```
