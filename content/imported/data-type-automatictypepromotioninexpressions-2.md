---
title: Automatic Type Promotion in Expressions
nav: Automatic Type Promotion i...
description: System.out.println((f * b) + " + " + (i / c) + " - " + (d * s));
section: Imported - java2s Archive
order: 1011
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/AutomaticTypePromotioninExpressions.htm
---
```java title=Example.java
byte b = 50;
   b = (byte)(b * 2);
java title=Example.java
publicclass MainClass {
  publicstaticvoid main(String args[]) {
    byte b = 42;
    char c = 'a';
    short s = 1024;
    int i = 50000;
    float f = 5.67f;
    double d = .1234;
    double result = (f * b) + (i / c) - (d * s);
    System.out.println((f * b) + " + " + (i / c) + " - " + (d * s));
    System.out.println("result = " + result);
  }
}
java title=Example.java
238.14 + 515 - 126.3616
result = 626.7784146484375
```
