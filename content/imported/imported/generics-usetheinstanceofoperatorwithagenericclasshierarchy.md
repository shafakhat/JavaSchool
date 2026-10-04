---
title: Use the instanceof operator with a generic class hierarchy.
nav: Use the instanceof operato...
description: // Demonstrate runtime type ID implications of generic class hierarchy.
section: Imported - java2s Archive
order: 1001
source: https://web.archive.org/web/20090129173435/http://java2s.com:80/Code/Java/Generics/Usetheinstanceofoperatorwithagenericclasshierarchy.htm
---
Use the instanceof operator with a generic class hierarchy.

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
// A subclass of Gen.
class Gen2<T> extends Gen<T> {
  Gen2(T o) {
    super(o);
  }
}
 // Demonstrate runtime type ID implications of generic class hierarchy.
public class HierDemo3 {
  public static void main(String args[]) {
    // Create a Gen object for Integers.
    Gen<Integer> iOb = new Gen<Integer>(88);
    // Create a Gen2 object for Integers.
    Gen2<Integer> iOb2 = new Gen2<Integer>(99);
    // Create a Gen2 object for Strings.
    Gen2<String> strOb2 = new Gen2<String>("Generics Test");
    // See if iOb2 is some form of Gen2.
    if(iOb2 instanceof Gen2<?>)
      System.out.println("iOb2 is instance of Gen2");
    // See if iOb2 is some form of Gen.
    if(iOb2 instanceof Gen<?>)
      System.out.println("iOb2 is instance of Gen");
    System.out.println();
    // See if strOb2 is a Gen2.
    if(strOb2 instanceof Gen2<?>)
      System.out.println("strOb is instance of Gen2");
    // See if strOb2 is a Gen.
    if(strOb2 instanceof Gen<?>)
      System.out.println("strOb is instance of Gen");
    System.out.println();
    // See if iOb is an instance of Gen2, which its not.
    if(iOb instanceof Gen2<?>)
      System.out.println("iOb is instance of Gen2");
    // See if iOb is an instance of Gen, which it is.
    if(iOb instanceof Gen<?>)
      System.out.println("iOb is instance of Gen");
    // The following can't be compiled because
    // generic type info does not exist at runtime.
//    if(iOb2 instanceof Gen2<Integer>)
//      System.out.println("iOb2 is instance of Gen2<Integer>");
  }
}
```

1.  A simple generic class.
---  ---
2.  Demonstrate the non generic class
3.  Stats attempts (unsuccessfully) to create a generic class
4.  A simple generic class heirarchy.
5.  A nongeneric class can be the superclass of a generic subclass.
6.  Java hierarchy generic class
7.  Custom Generic Object Tester
