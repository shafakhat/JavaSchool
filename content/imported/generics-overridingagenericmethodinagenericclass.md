---
title: Overriding a generic method in a generic class.
nav: Overriding a generic metho...
description: 2. Java generic: Ambiguity caused by erasure on overloaded methods.
section: Imported - java2s Archive
order: 1042
source: https://web.archive.org/web/20081009150905/http://www.java2s.com:80/Code/Java/Generics/Overridingagenericmethodinagenericclass.htm
---
Overriding a generic method in a generic class.

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
    System.out.print("Gen's getob(): " );
    return ob;
  }
}
// A subclass of Gen that overrides getob().
class Gen2<T> extends Gen<T> {
  Gen2(T o) {
    super(o);
  }
  // Override getob().
  T getob() {
    System.out.print("Gen2's getob(): ");
    return ob;
  }
}
// Demonstrate generic method override.
public class OverrideDemo {
  public static void main(String args[]) {
    // Create a Gen object for Integers.
    Gen<Integer> iOb = new Gen<Integer>(88);
    // Create a Gen2 object for Integers.
    Gen2<Integer> iOb2 = new Gen2<Integer>(99);
    // Create a Gen2 object for Strings.
    Gen2<String> strOb2 = new Gen2<String>("Generics Test");
    System.out.println(iOb.getob());
    System.out.println(iOb2.getob());
    System.out.println(strOb2.getob());
  }
}
```

1.  Demonstrate a simple generic method.
---  ---
2.  Java generic: Ambiguity caused by erasure on overloaded methods.
3.  Java generic: A situation that creates a bridge method.
