---
title: A nongeneric class can be the superclass of a generic subclass.
nav: A nongeneric class can be ...
description: A nongeneric class can be the superclass of a generic subclass. : Generic Class « Generics « Java
section: Imported - java2s Archive
order: 1004
source: https://web.archive.org/web/20090924204621/http://www.java2s.com:80/Code/Java/Generics/Anongenericclasscanbethesuperclassofagenericsubclass.htm
---
A nongeneric class can be the superclass of a generic subclass. : Generic Class « Generics « Java
A nongeneric class can be the superclass of a generic subclass.

```java title=Example.java
/*
Java 2, v5.0 (Tiger) New Features
by Herbert Schildt
ISBN: 0072258543
Publisher: McGraw-Hill/Osborne, 2004
*/
// A nongeneric class.
class NonGen {
  int num;
  NonGen(int i) {
    num = i;
  }
  int getnum() {
    return num;
  }
}
// A generic subclass.
class Gen<T> extends NonGen {
  T ob; // declare an object of type T
  // Pass the constructor a reference to
  // an object of type T.
  Gen(T o, int i) {
    super(i);
    ob = o;
  }
  // Return ob.
  T getob() {
    return ob;
  }
}
// Create a Gen object.
public class HierDemo2 {
  public static void main(String args[]) {
    // Create a Gen object for String.
    Gen<String> w = new Gen<String>("Hello", 47);
    System.out.print(w.getob() + " ");
    System.out.println(w.getnum());
  }
}
```

1.  A simple generic class.
---  ---
2.  Demonstrate the non generic class
3.  Stats attempts (unsuccessfully) to create a generic class
4.  A simple generic class hierarchy.
5.  Use the instanceof operator with a generic class hierarchy.
6.  Java hierarchy generic class
7.  Custom Generic Object Tester
8.  Pair of template arguments
