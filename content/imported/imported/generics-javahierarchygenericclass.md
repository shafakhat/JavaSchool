---
title: Java hierarchy generic class
nav: Java hierarchy generic class
description: 3. Stats attempts (unsuccessfully) to create a generic class
section: Imported - java2s Archive
order: 1041
source: https://web.archive.org/web/20090409005927/http://www.java2s.com:80/Code/Java/Generics/Javahierarchygenericclass.htm
---
Java hierarchy generic class

```java title=Example.java
/*
Java 2, v5.0 (Tiger) New Features
by Herbert Schildt
ISBN: 0072258543
Publisher: McGraw-Hill/Osborne, 2004
*/
// Here, T is bound by Object by default.
class Gen<T> {
  T ob; // here, T will be replaced by Object
  Gen(T o) {
    ob = o;
  }
  // Return ob.
  T getob() {
    return ob;
  }
}
// Here, T is bound by String.
class GenStr<T extends String> {
  T str; // here, T will be replaced by String
  GenStr(T o) {
    str = o;
  }
  T getstr() { return str; }
}
public class GenTypeDemo {
  public static void main(String args[]) {
    Gen<Integer> iOb = new Gen<Integer>(99);
    Gen<Float> fOb = new Gen<Float>(102.2F);
    System.out.println(iOb.getClass().getName());
    System.out.println(fOb.getClass().getName());
  }
}
```

1.  A simple generic class.
---  ---
2.  Demonstrate the non generic class
3.  Stats attempts (unsuccessfully) to create a generic class
4.  A simple generic class heirarchy.
5.  A nongeneric class can be the superclass of a generic subclass.
6.  Use the instanceof operator with a generic class hierarchy.
7.  Custom Generic Object Tester
