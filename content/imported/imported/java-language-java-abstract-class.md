---
title: Java Tutorial - Java Abstract Class
nav: Java Tutorial - Java Abstr...
description: Abstract class is for abstract idea or concept. For example, int data type is a concrete data type and double is another concrete data type. They are both numbers. Here n
section: Imported - java2s Archive
order: 50447
source: https://www.java2s.com/Tutorials/Java/Java_Language/5090__Java_Abstract_Class.html
---
```java title=Example.java
« Previous
```

- Next »

Abstract class is for abstract idea or concept. For example, int data type is a concrete data type and double is another concrete data type. They are both numbers. Here number is an abstract concept. Shape is another example. We can have spare, rectangle or triangle or circle. They are all concrete while shape is an abstract class.

In Java we use abstract class to define the abstract concept. Abstract concept must have some abstract aspects. For example, the abstract concept is the Shape while the abstract aspect is how to calculate area. The abstract concept becomes abstract class in Java and the abstract aspect becomes the abstract method.

## Syntax

You can require that certain methods be overridden by subclasses by specifying the abstract type modifier. To declare an abstract method, use this general form:

```java title=Example.java
abstract type name(parameter-list);
```

No method body is present for abstract method. Any class that contains one or more abstract methods must also be declared abstract.

```java title=Example.java
abstractclass MyAbstractClass{
   abstract type name(parameter-list);
}
```

Here is an abstract class, followed by a class which implements its abstract method.

```java title=Example.java
abstractclass MyAbstractClass {
  abstractvoid callme();
/*fromwww.java2s.com*/void callmetoo() {
    System.out.println("This is a concrete method.");
  }
}
class B extends MyAbstractClass {
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

The output:

## Example

The following code defines Shape class as abstract. Shape class has abstract method called area(). Rectangle class extends abstract class Shape and implements the area() method for itself.

```java title=Example.java
abstractclass Shape {
  double height;/*www.java2s.com*/double width;
  Shape(double a, double b) {
    height = a;
    width = b;
  }
  abstractdouble area();
}
class Rectangle extends Shape{
  Rectangle(double a, double b) {
    super(a, b);
  }
  double area() {
    System.out.println("Inside Area for Rectangle.");
    return height * width;
  }
}
class Triangle extends Shape{
  Triangle(double a, double b) {
    super(a, b);
  }
  double area() {
    System.out.println("Inside Area for Triangle.");
    return height * width / 2;
  }
}
publicclass Main {
  publicstaticvoid main(String args[]) {
    Rectangle r = new Rectangle(10, 5);
    Triangle t = new Triangle(10, 8);
    Shape figref;
    figref = r;
    System.out.println("Area is " + figref.area());
    figref = t;
    System.out.println("Area is " + figref.area());
  }
}
```

The output:

- Next »
- « Previous
