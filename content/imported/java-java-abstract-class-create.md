---
title: Java Abstract Class Create
nav: Java Abstract Class Create
description: Here is a simple example of a class with an abstract method, followed by a class which implements that method:
section: Imported - java2s Archive
order: 1016
source: https://web.archive.org/web/20210102113259/http://www.java2s.com/ref/java/java-abstract-class-create.html
---
## Introduction

Abstract class is for abstract idea.

Here is a simple example of a class with an abstract method, followed by a class which implements that method:

```java title=Example.java
// A Simple demonstration of abstract.abstractclass A {
  abstractvoid callme();
  // concrete methods are still allowed in abstract classesvoid callmetoo() {
    System.out.println("This is a concrete method.");
  }
}
class B extends A {
  void callme() {
    System.out.println("B's implementation of callme.");
  }
}
publicclass Main {
  publicstaticvoid main(String args[]) {
    B b = new B();
    b.callme();
    b.callmetoo();
  }
}
```

The following code shows how to use abstract class to define an abstract concept.

The Shape is an abstract concept. Its subclass provides a concrete implementation.

```java title=Example.java
// Using abstract methods and classes.abstractclassShape {
  double width;double height;
  Shape(double a, double b) {
    width = a;
    height = b;
  }
  // area is now an an abstract method abstractdouble area();
}
classRectangleextendsShape {
  Rectangle(double a, double b) {
    super(a, b);
  }
  // override area for rectangledouble area() {
    System.out.println("Inside Area for Rectangle.");
    return width * height;
  }
}
class Triangle extendsShape {
  Triangle(double a, double b) {
    super(a, b);
  }
  // override area for right triangledouble area() {
    System.out.println("Inside Area for Triangle.");
    return width * height / 2;
  }
}
publicclass Main {
  publicstaticvoid main(String args[]) {
    Rectangle r = newRectangle(9, 5);
    Triangle t = new Triangle(10, 8);
    Shape figref; // this is OK, no object is created
    figref = r;
    System.out.println("Area is " + figref.area());
    figref = t;
    System.out.println("Area is " + figref.area());
  }
}
```

PreviousNext

## Related

- Java autoboxing unboxing Boolean Values
- Java autoboxing unboxing Character Values
- Java autoboxing unboxing null pointer exception
- Java abstract final class Inheritance
- Java class Access Control
