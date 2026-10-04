---
title: Constructor initialization with composition
nav: Constructor initialization...
description: // www.BruceEckel.com. See copyright notice in CopyRight.txt.
section: Imported - java2s Archive
order: 1151
source: https://web.archive.org/web/20081006161223/http://www.java2s.com:80/Code/Java/Class/Constructorinitializationwithcomposition.htm
---
Constructor initialization with composition

```java title=Example.java
// : c06:Bath.java
// Constructor initialization with composition.
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
class Soap {
  private String s;
  Soap() {
    System.out.println("Soap()");
    s = new String("Constructed");
  }
  public String toString() {
    return s;
  }
}
public class Bath {
  private String // Initializing at point of definition:
      s1 = new String("Happy"), s2 = "Happy", s3, s4;
  private Soap castille;
  private int i;
  private float toy;
  public Bath() {
    System.out.println("Inside Bath()");
    s3 = new String("Joy");
    i = 47;
    toy = 3.14f;
    castille = new Soap();
  }
  public String toString() {
    if (s4 == null) // Delayed initialization:
      s4 = new String("Joy");
    return "s1 = " + s1 + "\n" + "s2 = " + s2 + "\n" + "s3 = " + s3 + "\n"
        + "s4 = " + s4 + "\n" + "i = " + i + "\n" + "toy = " + toy
        + "\n" + "castille = " + castille;
  }
  public static void main(String[] args) {
    Bath b = new Bath();
    System.out.println(b);
  }
} ///:~
```

1.  Paying attention to exceptions in constructors
---  ---
2.  Order of constructor calls
3.  Constructors and polymorphism don't produce what you might expect
4.  Demonstration of a simple constructor
5.  Constructors can have arguments
6.  Show Constructors conflicting
7.  Show that if your class has no constructors, your superclass constructors still get called
8.  Constructor calls during inheritance
9.  A constructor for copying an object of the same
