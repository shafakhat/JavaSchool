---
title: Demonstrate a raw type.
nav: Demonstrate a raw type.
description: 1. A simple generic class with two type parameters: T and V.
section: Imported - java2s Archive
order: 1022
source: https://web.archive.org/web/20081201192141/http://www.java2s.com:80/Code/Java/Generics/Demonstratearawtype.htm
---
```java title=Example.java
class Gen<T> {
  T ob; // declare an object of type T
  Gen(T o) {
    ob = o;
  }
  T getob() {
    return ob;
  }
}
class RawDemo {
  public static void main(String args[]) {
    Gen<Integer> iOb = new Gen<Integer>(88);
    Gen<String> strOb = new Gen<String>("Generics Test");
    Gen raw = new Gen(new Double(98.6));
    double d = (Double) raw.getob();
    System.out.println("value: " + d);
    strOb = raw; // OK, but potentially wrong
    raw = iOb; // OK, but potentially wrong
  }
}
```

1.  A simple generic class with two type parameters: T and V.
---  ---
2.  Java generic: Hierarchy argument
3.  Boxing Generic Example
4.  Demonstrate a raw generic type.
5.  T is a type parameter that will be replaced by a real type when an object of type Gen is created.
6.  Create a generic class that can compute the average of an array of numbers of any given type.
7.  the type argument for T must be either Number, or a class derived from Number.
8.  A subclass can add its own type parameters.
