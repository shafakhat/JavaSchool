---
title: Java Design Patterns Tutorial - Java Design Pattern - Facade Pattern
nav: Java Design Patterns Tutor...
description: It provides a simple interface to the client and the client uses the interface to interact with the system.
section: Imported - java2s Archive
order: 50122
source: https://www.java2s.com/Tutorials/Java/Java_Design_Patterns/0120__Java_Facade_Pattern.html
---
```java title=Example.java
« Previous
```

- Next »

Facade pattern hides the complexities of a system.

It provides a simple interface to the client and the client uses the interface to interact with the system.

Facade pattern is a structural pattern.

## Example

```java title=Example.java
class ShapeFacade {
  interface Shape {
    void draw();//www.java2s.com
  }
  class Rectangle implements Shape {
    @Override
    publicvoid draw() {
      System.out.println("Rectangle::draw()");
    }
  }
  class Square implements Shape {
    @Override
    publicvoid draw() {
      System.out.println("Square::draw()");
    }
  }
  class Circle implements Shape {
    @Override
    publicvoid draw() {
      System.out.println("Circle::draw()");
    }
  }
  private Shape circle = new Circle();
  private Shape rectangle = new Rectangle();
  private Shape square = new Square();
  public ShapeFacade() {
  }
  publicvoid drawCircle() {
    circle.draw();
  }
  publicvoid drawRectangle() {
    rectangle.draw();
  }
  publicvoid drawSquare() {
    square.draw();
  }
}
publicclass Main {
  publicstaticvoid main(String[] args) {
    ShapeFacade shapeFacade = new ShapeFacade();
    shapeFacade.drawCircle();
    shapeFacade.drawRectangle();
    shapeFacade.drawSquare();
  }
}
```

The code above generates the following result.

- Next »
- « Previous
