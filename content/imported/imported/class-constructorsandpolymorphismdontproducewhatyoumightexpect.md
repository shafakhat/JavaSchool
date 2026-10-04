---
title: Constructors and polymorphism don't produce what you might expect
nav: Constructors and polymorph...
description: Constructors and polymorphism don't produce what you might expect
section: Imported - java2s Archive
order: 1152
source: https://web.archive.org/web/20081006161229/http://www.java2s.com:80/Code/Java/Class/Constructorsandpolymorphismdontproducewhatyoumightexpect.htm
---
```java title=Example.java
// : c07:PolyConstructors.java
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
abstract class Glyph {
  abstract void draw();
  Glyph() {
    System.out.println("Glyph() before draw()");
    draw();
    System.out.println("Glyph() after draw()");
  }
}
class RoundGlyph extends Glyph {
  private int radius = 1;
  RoundGlyph(int r) {
    radius = r;
    System.out.println("RoundGlyph.RoundGlyph(), radius = " + radius);
  }
  void draw() {
    System.out.println("RoundGlyph.draw(), radius = " + radius);
  }
}
public class PolyConstructors {
  public static void main(String[] args) {
    new RoundGlyph(5);
  }
} ///:~
```

1.  Paying attention to exceptions in constructors
---  ---
2.  Order of constructor calls
3.  Constructor initialization with composition
4.  Demonstration of a simple constructor
5.  Constructors can have arguments
6.  Show Constructors conflicting
7.  Show that if your class has no constructors, your superclass constructors still get called
8.  Constructor calls during inheritance
9.  A constructor for copying an object of the same
