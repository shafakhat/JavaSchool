---
title: A named inner class is used to
nav: A named inner class is use...
description: 1. Nested classes can access all members of all levels of the classes they are nested within
section: Imported - java2s Archive
order: 1129
source: https://web.archive.org/web/20090106051326/http://www.java2s.com:80/Code/Java/Class/Anamedinnerclassisusedto.htm
---
```java title=Example.java
/** Demonstrate inner-inner class. A named inner class
 * is used to show that it can access non-local variables
 * in the enclosing object.
 */
public class InnerClass3 {
  static String msg = "Hello";
  public static void main(String[] av) {
    class Inner {
      public void doTheWork() {
        // print member of enclosing class
        System.out.println(msg);
      }
    }
    Inner p = new Inner();
    p.doTheWork();
  }
}
```

1.  Nested classes can access all members of all levels of the classes they are nested within
---  ---
2.  Creating inner classes
3.  Creating instances of inner classes
4.  Returning a reference to an inner class
5.  Nesting a class within a scope
6.  Putting test code in a nested class
7.  Inheriting an inner class
8.  Creating a constructor for an anonymous inner class
9.  This file is to show what happens if you try to access an inner class created in another class
10.  Demonstrate an Inner Child class
11.  Demonstrate simple inner class
12.  Just to show that there is no such thing as inner methods in Java
13.  An inner class cannot be overriden like a method
14.  Proper inheritance of an inner class
15.  Using inner classes for callbacks
16.  Holds a sequence of Objects
17.  With concrete or abstract classes, inner classes are the only way to produce the effect
18.  Nested Class Static
19.  Static Inner Class
20.  Compiler will generate a synthetic constructor since SyntheticConstructor() is private
