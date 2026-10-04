---
title: Java Abstract Class Create
nav: Java Abstract Class Create
description: Here is a simple example of a class with an abstract method, followed by a class which implements that method:
section: Imported - java2s Archive
order: 1016
source: https://web.archive.org/web/20210102113259/http://www.java2s.com/ref/java/java-abstract-class-create.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Introduction

Abstract class is for abstract idea.

Here is a simple example of a class with an abstract method, followed by a class which implements that method:

```java title=Example.java
// A Simple demonstration of abstract.abstractclass A {
  abstractvoid callme();

  // concrete methods are still allowed in abstract classesvoid callmetoo() {
    System.out.println("This is a concrete method.");
  }/*fromwww.java2s.com*/
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
  double width;//fromwww.java2s.comdouble height;

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
