---
title: Java generic
nav: Java generic
description: 2. Java generic: Ambiguity caused by erasure on overloaded methods.
section: Imported - java2s Archive
order: 1036
source: https://web.archive.org/web/20081009150900/http://www.java2s.com:80/Code/Java/Generics/JavagenericAsituationthatcreatesabridgemethod.htm
---
Java generic: A situation that creates a bridge method.

```java title=Example.java
/*
Java 2, v5.0 (Tiger) New Features
by Herbert Schildt
ISBN: 0072258543
Publisher: McGraw-Hill/Osborne, 2004
*/
//
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
// A subclass of Gen.
class Gen2 extends Gen<String> {
  Gen2(String o) {
    super(o);
  }
  // A String-specific override of getob().
  String getob() {
    System.out.print("You called String getob(): ");
    return ob;
  }
}
// Demonstrate a situation that requires a bridge method.
public class BridgeDemo {
  public static void main(String args[]) {
    // Create a Gen2 object for Strings.
    Gen2 strOb2 = new Gen2("Generics Test");
    System.out.println(strOb2.getob());
  }
}
```

1.  Demonstrate a simple generic method.
---  ---
2.  Java generic: Ambiguity caused by erasure on overloaded methods.
3.  Overriding a generic method in a generic class.
