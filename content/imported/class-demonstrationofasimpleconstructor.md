---
title: Demonstration of a simple constructor
nav: Demonstration of a simple ...
description: // www.BruceEckel.com. See copyright notice in CopyRight.txt.
section: Imported - java2s Archive
order: 1009
source: https://web.archive.org/web/20081006161240/http://www.java2s.com:80/Code/Java/Class/Demonstrationofasimpleconstructor.htm
---
Demonstration of a simple constructor

```java title=Example.java
// : c04:SimpleConstructor.java
// Demonstration of a simple constructor.
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
class Rock {
  Rock() { // This is the constructor
    System.out.println("Creating Rock");
  }
}
public class SimpleConstructor {
  public static void main(String[] args) {
    for (int i = 0; i < 10; i++)
      new Rock();
  }
} ///:~
```

1.  Paying attention to exceptions in constructors
---  ---
2.  Order of constructor calls
3.  Constructors and polymorphism don't produce what you might expect
4.  Constructor initialization with composition
5.  Constructors can have arguments
6.  Show Constructors conflicting
7.  Show that if your class has no constructors, your superclass constructors still get called
8.  Constructor calls during inheritance
9.  A constructor for copying an object of the same
