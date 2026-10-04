---
title: Demonstrate Run-Time Type Information.
nav: Demonstrate Run-Time Type ...
description: System.out.println("x is object of type: " + clObj.getName());
section: Imported - java2s Archive
order: 1251
source: https://web.archive.org/web/20140829090205/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/DemonstrateRunTimeTypeInformation.htm
---
```java title=Example.java
class X {
  int a;
  float b;
}
class Y extends X {
  double c;
}
class MainClass {
  public static void main(String args[]) {
    X x = new X();
    Y y = new Y();
    Class<?> clObj;
    clObj = x.getClass();
    System.out.println("x is object of type: " + clObj.getName());
    clObj = y.getClass();
    System.out.println("y is object of type: " + clObj.getName());
    clObj = clObj.getSuperclass();
    System.out.println("y's superclass is " + clObj.getName());
  }
}
```
