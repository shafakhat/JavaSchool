---
title: Java generic
nav: Java generic
description: Java generic: Ambiguity caused by erasure on overloaded methods.
section: Imported - java2s Archive
order: 1035
source: https://web.archive.org/web/20081009154701/http://www.java2s.com:80/Code/Java/Generics/JavagenericAmbiguitycausedbyerasureonoverloadedmethods.htm
---
Java generic: Ambiguity caused by erasure on overloaded methods.

```java title=Example.java
/*
Java 2, v5.0 (Tiger) New Features
by Herbert Schildt
ISBN: 0072258543
Publisher: McGraw-Hill/Osborne, 2004
*/
class MyGenClass<T, V> {
  T ob1;
  V ob2;
  // ...
  // These two overloaded methods are ambiguous.
  // and will not compile.
  void set(T o) {
    ob1 = o;
  }
  void set(V o) {
    ob2 = o;
  }
}
// Can't create an instance of T.
class Gen<T> {
  T ob;
  Gen() {
    ob = new T(); // Illegal!!!
  }
}
public class Wrong<T> {
  // Wrong, no static variables of type T.
  static T ob;
  // Wrong, no static method can use T.
  static T getob() {
    return ob;
  }
  // Wrong, no static method can access object
  // of type T.
  static void showob() {
    System.out.println(ob);
 }
}
```

1.  Demonstrate a simple generic method.
---  ---
2.  Overriding a generic method in a generic class.
3.  Java generic: A situation that creates a bridge method.
