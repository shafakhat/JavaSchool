---
title: Java abstract final class Inheritance
nav: Java abstract final class ...
description: Imported from the java2s.com archive: Java abstract final class Inheritance
section: Imported - java2s Archive
order: 1017
source: https://web.archive.org/web/20210102113259/http://www.java2s.com/ref/java/java-abstract-final-class-inheritance.html
---
## Question

What is the output of the following code?

```java title=Example.java
abstractfinalclassShape {
  double width;/*fromwww.java2s.com*/double height;

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

```java title=Example.java
Compile time error
The class Shape can be either abstract or final, not both
```

## Note

A class cannot be both abstract and final.

An abstract class has to be extended by its subclasses.

PreviousNext

## Related

- Java autoboxing unboxing Character Values
- Java autoboxing unboxing null pointer exception
- Java Abstract Class Create
- Java class Access Control
- Java class Access field from inner class from its outer class
