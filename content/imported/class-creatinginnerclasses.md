---
title: Creating inner classes
nav: Creating inner classes
description: // www.BruceEckel.com. See copyright notice in CopyRight.txt.
section: Imported - java2s Archive
order: 1158
source: https://web.archive.org/web/20090106230535/http://www.java2s.com:80/Code/Java/Class/Creatinginnerclasses.htm
---
```java title=Example.java
// : c08:Parcel1.java
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
public class Parcel1 {
  class Contents {
    private int i = 11;
    public int value() {
      return i;
    }
  }
  class Destination {
    private String label;
    Destination(String whereTo) {
      label = whereTo;
    }
    String readLabel() {
      return label;
    }
  }
  // Using inner classes looks just like
  // using any other class, within Parcel1:
  public void ship(String dest) {
    Contents c = new Contents();
    Destination d = new Destination(dest);
    System.out.println(d.readLabel());
  }
  public static void main(String[] args) {
    Parcel1 p = new Parcel1();
    p.ship("Tanzania");
  }
} ///:~
```

1.  Nested classes can access all members of all levels of the classes they are nested within
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
