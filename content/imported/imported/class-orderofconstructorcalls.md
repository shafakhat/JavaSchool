---
title: Order of constructor calls
nav: Order of constructor calls
description: // www.BruceEckel.com. See copyright notice in CopyRight.txt.
section: Imported - java2s Archive
order: 1051
source: https://web.archive.org/web/20081006161245/http://www.java2s.com:80/Code/Java/Class/Orderofconstructorcalls.htm
---
Order of constructor calls

```java title=Example.java
// : c07:Sandwich.java
// Order of constructor calls.
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
class Meal {
  Meal() {
    System.out.println("Meal()");
  }
}
class Bread {
  Bread() {
    System.out.println("Bread()");
  }
}
class Cheese {
  Cheese() {
    System.out.println("Cheese()");
  }
}
class Lettuce {
  Lettuce() {
    System.out.println("Lettuce()");
  }
}
class Lunch extends Meal {
  Lunch() {
    System.out.println("Lunch()");
  }
}
class PortableLunch extends Lunch {
  PortableLunch() {
    System.out.println("PortableLunch()");
  }
}
public class Sandwich extends PortableLunch {
  private Bread b = new Bread();
  private Cheese c = new Cheese();
  private Lettuce l = new Lettuce();
  public Sandwich() {
    System.out.println("Sandwich()");
  }
  public static void main(String[] args) {
    new Sandwich();
  }
} ///:~
```

1.  Paying attention to exceptions in constructors
---  ---
2.  Constructors and polymorphism don't produce what you might expect
3.  Constructor initialization with composition
4.  Demonstration of a simple constructor
5.  Constructors can have arguments
6.  Show Constructors conflicting
7.  Show that if your class has no constructors, your superclass constructors still get called
8.  Constructor calls during inheritance
9.  A constructor for copying an object of the same
