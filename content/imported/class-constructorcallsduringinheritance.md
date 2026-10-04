---
title: Constructor calls during inheritance
nav: Constructor calls during i...
description: // www.BruceEckel.com. See copyright notice in CopyRight.txt.
section: Imported - java2s Archive
order: 1150
source: https://web.archive.org/web/20081006161218/http://www.java2s.com:80/Code/Java/Class/Constructorcallsduringinheritance.htm
---
```java title=Example.java
// : c06:Cartoon.java
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
class Art {
  Art() {
    System.out.println("Art constructor");
  }
}
class Drawing extends Art {
  Drawing() {
    System.out.println("Drawing constructor");
  }
}
public class Cartoon extends Drawing {
  public Cartoon() {
    System.out.println("Cartoon constructor");
  }
  public static void main(String[] args) {
    Cartoon x = new Cartoon();
  }
} ///:~
```

1.  Paying attention to exceptions in constructors
---  ---
2.  Order of constructor calls
3.  Constructors and polymorphism don't produce what you might expect
4.  Constructor initialization with composition
5.  Demonstration of a simple constructor
6.  Constructors can have arguments
7.  Show Constructors conflicting
8.  Show that if your class has no constructors, your superclass constructors still get called
9.  A constructor for copying an object of the same
