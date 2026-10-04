---
title: Constructors can have arguments
nav: Constructors can have argu...
description: // www.BruceEckel.com. See copyright notice in CopyRight.txt.
section: Imported - java2s Archive
order: 1153
source: https://web.archive.org/web/20081006161234/http://www.java2s.com:80/Code/Java/Class/Constructorscanhavearguments.htm
---
Constructors can have arguments

```java title=Example.java
// : c04:SimpleConstructor2.java
// Constructors can have arguments.
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
class Rock2 {
  Rock2(int i) {
    System.out.println("Creating Rock number " + i);
  }
}
public class SimpleConstructor2 {
  public static void main(String[] args) {
    for (int i = 0; i < 10; i++)
      new Rock2(i);
  }
} ///:~
```

1.  Paying attention to exceptions in constructors
---  ---
2.  Order of constructor calls
3.  Constructors and polymorphism don't produce what you might expect
4.  Constructor initialization with composition
5.  Demonstration of a simple constructor
6.  Show Constructors conflicting
7.  Show that if your class has no constructors, your superclass constructors still get called
8.  Constructor calls during inheritance
9.  A constructor for copying an object of the same
