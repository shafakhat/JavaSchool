---
title: Creating a constructor for an anonymous inner class
nav: Creating a constructor for...
description: // www.BruceEckel.com. See copyright notice in CopyRight.txt.
section: Imported - java2s Archive
order: 1156
source: https://web.archive.org/web/20090106045121/http://www.java2s.com:80/Code/Java/Class/Creatingaconstructorforananonymousinnerclass.htm
---
Creating a constructor for an anonymous inner class

```java title=Example.java
// : c08:AnonymousConstructor.java
// Creating a constructor for an anonymous inner class.
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
abstract class Base {
  public Base(int i) {
    System.out.println("Base constructor, i = " + i);
  }
  public abstract void f();
}
public class AnonymousConstructor {
  public static Base getBase(int i) {
    return new Base(i) {
      {
        System.out.println("Inside instance initializer");
      }
      public void f() {
        System.out.println("In anonymous f()");
      }
    };
  }
  public static void main(String[] args) {
    Base base = getBase(47);
    base.f();
  }
} ///:~
```

1.  Nested classes can access all members of all levels of the classes they are nested within
---  ---
2.  Creating inner classes
3.  Creating instances of inner classes
4.  Returning a reference to an inner class
5.  Nesting a class within a scope
6.  Putting test code in a nested class
7.  Inheriting an inner class
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
