---
title: With concrete or abstract classes, inner classes are the only way to produce the effect
nav: With concrete or abstract ...
description: With concrete or abstract classes, inner classes are the only way to produce the effect
section: Imported - java2s Archive
order: 1102
source: https://web.archive.org/web/20090106012414/http://www.java2s.com:80/Code/Java/Class/Withconcreteorabstractclassesinnerclassesaretheonlywaytoproducetheeffect.htm
---
```java title=Example.java
// : c08:MultiImplementation.java
// of "multiple implementation inheritance."
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
class D {
}
abstract class E {
}
class Z extends D {
  E makeE() {
    return new E() {
    };
  }
}
public class MultiImplementation {
  static void takesD(D d) {
  }
  static void takesE(E e) {
  }
  public static void main(String[] args) {
    Z z = new Z();
    takesD(z);
    takesE(z.makeE());
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
8.  Creating a constructor for an anonymous inner class
9.  This file is to show what happens if you try to access an inner class created in another class
10.  Demonstrate an Inner Child class
11.  Demonstrate simple inner class
12.  Just to show that there is no such thing as inner methods in Java
13.  A named inner class is used to
14.  An inner class cannot be overriden like a method
15.  Proper inheritance of an inner class
16.  Using inner classes for callbacks
17.  Holds a sequence of Objects
18.  Nested Class Static
19.  Static Inner Class
20.  Compiler will generate a synthetic constructor since SyntheticConstructor() is private
