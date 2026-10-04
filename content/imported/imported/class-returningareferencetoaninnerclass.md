---
title: Returning a reference to an inner class
nav: Returning a reference to a...
description: // www.BruceEckel.com. See copyright notice in CopyRight.txt.
section: Imported - java2s Archive
order: 1064
source: https://web.archive.org/web/20090106013349/http://www.java2s.com:80/Code/Java/Class/Returningareferencetoaninnerclass.htm
---
```java title=Example.java
// : c08:Parcel2.java
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
public class Parcel2 {
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
  public Destination to(String s) {
    return new Destination(s);
  }
  public Contents cont() {
    return new Contents();
  }
  public void ship(String dest) {
    Contents c = cont();
    Destination d = to(dest);
    System.out.println(d.readLabel());
  }
  public static void main(String[] args) {
    Parcel2 p = new Parcel2();
    p.ship("Tanzania");
    Parcel2 q = new Parcel2();
    // Defining references to inner classes:
    Parcel2.Contents c = q.cont();
    Parcel2.Destination d = q.to("Borneo");
  }
} ///:~
```

1.  Nested classes can access all members of all levels of the classes they are nested within
---  ---
2.  Creating inner classes
3.  Creating instances of inner classes
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
