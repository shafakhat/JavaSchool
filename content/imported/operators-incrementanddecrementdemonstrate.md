---
title: Increment and Decrement
nav: Increment and Decrement
description: Imported from the java2s.com archive: Increment and Decrement
section: Imported - java2s Archive
order: 1114
source: https://web.archive.org/web/20140829074643/http://www.java2s.com/Tutorial/Java/0060__Operators/IncrementandDecrementDemonstrate.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String args[]) {
    int a = 1;
    int b = 2;
    int c;
    int d;
    c = ++b;
    d = a++;
    c++;
    System.out.println("a = " + a);
    System.out.println("b = " + b);
    System.out.println("c = " + c);
    System.out.println("d = " + d);
  }
}
java title=Example.java
a = 2
b = 3
c = 4
d = 1
```
