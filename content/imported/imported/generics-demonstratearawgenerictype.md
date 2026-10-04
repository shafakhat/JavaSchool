---
title: Demonstrate a raw generic type.
nav: Demonstrate a raw generic ...
description: 1. A simple generic class with two type parameters: T and V.
section: Imported - java2s Archive
order: 1021
source: https://web.archive.org/web/20100213125851/http://java2s.com/Code/Java/Generics/Demonstratearawgenerictype.htm
---
Demonstrate a raw generic type.

```java title=Example.java
/*
Java 2, v5.0 (Tiger) New Features
by Herbert Schildt
ISBN: 0072258543
Publisher: McGraw-Hill/Osborne, 2004
*/
class Gen<T> {
  T ob; // declare an object of type T
  // Pass the constructor a reference to
  // an object of type T.
  Gen(T o) {
    ob = o;
  }
  // Return ob.
  T getob() {
    return ob;
  }
}
// Demonstrate raw type.
public class RawDemo {
  public static void main(String args[]) {
    // Create a Gen object for Integers.
    Gen<Integer> iOb = new Gen<Integer>(88);
    // Create a Gen object for Strings.
    Gen<String> strOb = new Gen<String>("Generics Test");
    // Create a raw-type Gen object and give it
    // a Double value.
    Gen raw = new Gen(new Double(98.6));
    // Cast here is necessary because type is unknown.
    double d = (Double) raw.getob();
    System.out.println("value: " + d);
    // The use of a raw type can lead to runtime.
    // exceptions.  Here are some examples.
    // The following cast causes a runtime error!
//    int i = (Integer) raw.getob(); // runtime error
    // This assigment overrides type safety.
    strOb = raw; // OK, but potentially wrong
//    String str = strOb.getob(); // runtime error
    // This assignment also overrides type safety.
    raw = iOb; // OK, but potentially wrong
//    d = (Double) raw.getob(); // runtime error
  }
}
```

1.  A simple generic class with two type parameters: T and V.
---  ---
2.  Java generic: Hierarchy argument
3.  Boxing Generic Example
4.  T is a type parameter that will be replaced by a real type when an object of type Gen is created.
5.  Create a generic class that can compute the average of an array of numbers of any given type.
6.  the type argument for T must be either Number, or a class derived from Number.
7.  Demonstrate a raw type.
8.  A subclass can add its own type parameters.
