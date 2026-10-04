---
title: A simple generic class heirarchy.
nav: A simple generic class hei...
description: 3. Stats attempts (unsuccessfully) to create a generic class
section: Imported - java2s Archive
order: 1006
source: https://web.archive.org/web/20090409010242/http://www.java2s.com:80/Code/Java/Generics/Asimplegenericclassheirarchy.htm
---
```java title=Example.java
/*
Java 2, v5.0 (Tiger) New Features
by Herbert Schildt
ISBN: 0072258543
Publisher: McGraw-Hill/Osborne, 2004
*/
class Gen<T> {
  T ob;
  Gen(T o) {
    ob = o;
  }
  // Return ob.
  T getob() {
    return ob;
  }
}
// A subclass of Gen that defines a second
// type parameter, called V.
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
// Create an object of type Gen2.
public class HierDemo {
  public static void main(String args[]) {
    // Create a Gen2 object for String and Integer.
    Gen2<String, Integer> x =
      new Gen2<String, Integer>("Value is: ", 99);
    System.out.print(x.getob());
    System.out.println(x.getob2());
  }
}
```

1.  A simple generic class.
---  ---
2.  Demonstrate the non generic class
3.  Stats attempts (unsuccessfully) to create a generic class
4.  A nongeneric class can be the superclass of a generic subclass.
5.  Use the instanceof operator with a generic class hierarchy.
6.  Java hierarchy generic class
7.  Custom Generic Object Tester
