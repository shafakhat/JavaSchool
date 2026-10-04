---
title: Java Design Patterns Tutorial - Java Design Pattern - Bridge Pattern
nav: Java Design Patterns Tutor...
description: Bridge pattern decouples an definition from its implementation. It is a structural pattern.
section: Imported - java2s Archive
order: 50118
source: https://www.java2s.com/Tutorials/Java/Java_Design_Patterns/0070__Java_Bridge_Pattern.html
---
```java title=Example.java
```

Bridge pattern decouples an definition from its implementation. It is a structural pattern.

This pattern involves an interface which acts as a bridge. The bridge makes the concrete classes independent from interface implementer classes.

Both types of classes can be altered without affecting each other.

## Example

```java title=Example.java
interface Printer {
   publicvoid print(int radius, int x, int y);
}/*www.java2s.com*/class ColorPrinter implements Printer {
   @Override
   publicvoid print(int radius, int x, int y) {
      System.out.println("Color: " + radius +", x: " +x+", "+ y +"]");
   }
}
class BlackPrinter implements Printer {
   @Override
   publicvoid print(int radius, int x, int y) {
      System.out.println("Black: " + radius +", x: " +x+", "+ y +"]");
   }
}
abstractclass Shape {
   protected Printer print;
   protected Shape(Printer p){
      this.print = p;
   }
   publicabstractvoid draw();
}
class Circle extends Shape {
   privateint x, y, radius;
   public Circle(int x, int y, int radius, Printer draw) {
      super(draw);
      this.x = x;
      this.y = y;
      this.radius = radius;
   }
   publicvoid draw() {
      print.print(radius,x,y);
   }
}
publicclass Main {
   publicstaticvoid main(String[] args) {
      Shape redCircle = new Circle(100,100, 10, new ColorPrinter());
      Shape blackCircle = new Circle(100,100, 10, new BlackPrinter());
      redCircle.draw();
      blackCircle.draw();
   }
}
```

The code above generates the following result.

- « Previous
