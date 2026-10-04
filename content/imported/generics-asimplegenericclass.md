---
title: A simple generic class.
nav: A simple generic class.
description: System.out.println("Type of T is " + ob.getClass().getName());
section: Imported - java2s Archive
order: 1005
source: https://web.archive.org/web/20090409005917/http://www.java2s.com:80/Code/Java/Generics/Asimplegenericclass.htm
---
A simple generic class.

```java title=Example.java
class Gen<T> {
  T ob; // declare an object of type T
  Gen(T o) {
    ob = o;
  }
  T getob() {
    return ob;
  }
  void showType() {
    System.out.println("Type of T is " + ob.getClass().getName());
  }
}
public class GenDemo {
  public static void main(String args[]) {
    Gen<Integer> iOb;
    iOb = new Gen<Integer>(88);
    iOb.showType();
    int v = iOb.getob();
    System.out.println("value: " + v);
    System.out.println();
    Gen<String> strOb = new Gen<String>("Generics Test");
    strOb.showType();
    String str = strOb.getob();
    System.out.println("value: " + str);
  }
}
```

1.  Demonstrate the non generic class
---  ---
2.  Stats attempts (unsuccessfully) to create a generic class
3.  A simple generic class heirarchy.
4.  A nongeneric class can be the superclass of a generic subclass.
5.  Use the instanceof operator with a generic class hierarchy.
6.  Java hierarchy generic class
7.  Custom Generic Object Tester
