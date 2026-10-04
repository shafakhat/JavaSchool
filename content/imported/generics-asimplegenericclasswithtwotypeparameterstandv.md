---
title: A simple generic class with two type parameters
nav: A simple generic class wit...
description: System.out.println("Type of T is " + ob1.getClass().getName());
section: Imported - java2s Archive
order: 1008
source: https://web.archive.org/web/20090520052407/http://www.java2s.com:80/Code/Java/Generics/AsimplegenericclasswithtwotypeparametersTandV.htm
---
A simple generic class with two type parameters: T and V.

```java title=Example.java
class TwoGen<T, V> {
  T ob1;
  V ob2;
  TwoGen(T o1, V o2) {
    ob1 = o1;
    ob2 = o2;
  }
  void showTypes() {
    System.out.println("Type of T is " + ob1.getClass().getName());
    System.out.println("Type of V is " + ob2.getClass().getName());
  }
  T getob1() {
    return ob1;
  }
  V getob2() {
    return ob2;
  }
}
public class SimpGen {
  public static void main(String args[]) {
    TwoGen<Integer, String> tgObj = new TwoGen<Integer, String>(88, "Generics");
    tgObj.showTypes();
    int v = tgObj.getob1();
    System.out.println("value: " + v);
    String str = tgObj.getob2();
    System.out.println("value: " + str);
  }
}
```

1.  Java generic: Hierarchy argument
---  ---
2.  Boxing Generic Example
3.  Demonstrate a raw generic type.
4.  T is a type parameter that will be replaced by a real type when an object of type Gen is created.
5.  Create a generic class that can compute the average of an array of numbers of any given type.
6.  the type argument for T must be either Number, or a class derived from Number.
7.  Demonstrate a raw type.
8.  A subclass can add its own type parameters.
