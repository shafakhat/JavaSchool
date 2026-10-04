---
title: Nested classes can access all members of all levels of the classes they are nested within
nav: Nested classes can access ...
description: Nested classes can access all members of all levels of the classes they are nested within
section: Imported - java2s Archive
order: 1045
source: https://web.archive.org/web/20090106160637/http://www.java2s.com:80/Code/Java/Class/Nestedclassescanaccessallmembersofalllevelsoftheclassestheyarenestedwithin.htm
---
Nested classes can access all members of all levels of the classes they are nested within

```java title=Example.java
// : c08:MultiNestingAccess.java
// Nested classes can access all members of all levels of the classes they are nested within.
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
public class MultiNestingAccess {
  public static void main(String[] args) {
    MNA mna = new MNA();
    MNA.A mnaa = mna.new A();
    MNA.A.B mnaab = mnaa.new B();
    mnaab.h();
  }
} ///:~
class MNA {
  private void f() {
  }
  class A {
    private void g() {
    }
    public class B {
      void h() {
        g();
        f();
      }
    }
  }
}
```

1.  Creating inner classes
---  ---
2.  Creating instances of inner classes
3.  Returning a reference to an inner class
4.  Nesting a class within a scope
5.  Putting test code in a nested class
6.  Inheriting an inner class
7.  Creating a constructor for an anonymous inner class
8.  This file is to show what happens if you try to access an inner class created in another class
9.  Demonstrate an Inner Child class
10.  Demonstrate simple inner class
11.  Just to show that there is no such thing as inner methods in Java
12.  A named inner class is used to
13.  An inner class cannot be overriden like a method
14.  Proper inheritance of an inner class
15.  Using inner classes for callbacks
16.  Holds a sequence of Objects
17.  With concrete or abstract classes, inner classes are the only way to produce the effect
18.  Nested Class Static
19.  Static Inner Class
20.  Compiler will generate a synthetic constructor since SyntheticConstructor() is private
