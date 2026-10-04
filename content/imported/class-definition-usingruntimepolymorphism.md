---
title: Using run-time polymorphism.
nav: Using run-time polymorphism.
description: Imported from the java2s.com archive: Using run-time polymorphism.
section: Imported - java2s Archive
order: 1116
source: https://web.archive.org/web/20140829082212/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Usingruntimepolymorphism.htm
---
```java title=Example.java
class Figure {
  double dim1;
  double dim2;
  Figure(double a, double b) {
    dim1 = a;
    dim2 = b;
  }
  double area() {
    System.out.println("Area for Figure is undefined.");
    return 0;
  }
}
class Rectangle extends Figure {
  Rectangle(double a, double b) {
    super(a, b);
  }
  // override area for rectangle
  double area() {
    System.out.println("Inside Area for Rectangle.");
    return dim1 * dim2;
  }
}
class Triangle extends Figure {
  Triangle(double a, double b) {
    super(a, b);
  }
  // override area for right triangle
  double area() {
    System.out.println("Inside Area for Triangle.");
    return dim1 * dim2 / 2;
  }
}
class FindAreas {
  public static void main(String args[]) {
    Figure f = new Figure(10, 10);
    Rectangle r = new Rectangle(9, 5);
    Triangle t = new Triangle(10, 8);
    Figure figref;
    figref = r;
    System.out.println("Area is " + figref.area());
    figref = t;
    System.out.println("Area is " + figref.area());
    figref = f;
    System.out.println("Area is " + figref.area());
  }
}
```

| 5.24.1. | Polymorphism |
|---|---|
| 5.24.2. | An example of polymorphism |
| 5.24.3. | Downcasting and Run-Time Type Identification (RTTI) |
| 5.24.4. | Constructors and polymorphism don't produce what you might expect |
| 5.24.5. | Dynamic Method Dispatch |
| 5.24.6. | Using run-time polymorphism. |
