---
title: A subclass can add its own type parameters.
nav: A subclass can add its own...
description: // A subclass of Gen that defines a second type parameter, called V.
section: Imported - java2s Archive
order: 1009
source: https://web.archive.org/web/20100213125932/http://java2s.com/Code/Java/Generics/Asubclasscanadditsowntypeparameters.htm
---
A subclass can add its own type parameters.

```java title=Example.java
class Gen<T> {
  T ob; // declare an object of type T
  Gen(T o) {
    ob = o;
  }
  // Return ob.
  T getob() {
    return ob;
  }
}
// A subclass of Gen that defines a second type parameter, called V.
class Gen2<T, V> extends Gen<T> {
  V ob2;
  Gen2(T o, V o2) {
    super(o);
    ob2 = o2;
  }
  V getob2() {
    return ob2;
  }
}
class HierDemo {
  public static void main(String args[]) {
    Gen2<String, Integer> x = new Gen2<String, Integer>("Value is: ", 99);
    System.out.print(x.getob());
    System.out.println(x.getob2());
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
8.  Demonstrate a raw type.
