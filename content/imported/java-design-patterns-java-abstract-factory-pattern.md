---
title: Java Design Patterns Tutorial - Java Design Pattern - Abstract Factory Pattern
nav: Java Design Patterns Tutor...
description: Abstract Factory patterns, also called as Factory of factories, have a factory which creates other factories.
section: Imported - java2s Archive
order: 50113
source: https://www.java2s.com/Tutorials/Java/Java_Design_Patterns/0020__Java_Abstract_Factory_Pattern.html
---
```java title=Example.java
```

Abstract Factory pattern is another creational pattern.

Abstract Factory patterns, also called as Factory of factories, have a factory which creates other factories.

When using Abstract Factory pattern, we first use super factory to create factory, then use the created factory to create objects.

## Example

The following code shows how to use abstract factory pattern.

We are going to create shapes and Printers. For shapes, we would have circle, rectangle and square. For printers we will have paper Printer, Web Printer and screen Printer.

For shape we will create Shape interface, as follows

```java title=Example.java
interface Shape {
   void draw();
}
```

Then we create concrete classes implementing the Shape interface.

```java title=Example.java
class Rectangle implements Shape {
   @Override
   public void draw() {
      System.out.println("Inside Rectangle::draw() method.");
   }
}
class Square implements Shape {
   @Override
   public void draw() {
      System.out.println("Inside Square::draw() method.");
   }
}
class Circle implements Shape {
   @Override
   public void draw() {
      System.out.println("Inside Circle::draw() method.");
   }
}
```

After that we create an interface for Printers.

```java title=Example.java
interface Printer{
   void print();
}
```

Then we create concrete classes implementing the Printer interface.

```java title=Example.java
class PaperPrinter implements Printer{
   @Override
   public void print() {
      System.out.println("paper");
   }
}
class WebPrinter implements Printer{
   @Override
   public void print() {
      System.out.println("web");
   }
}
class ScreenPrinter implements Printer{
   @Override
   public void print() {
      System.out.println("screen");
   }
}
```

Finally we create an abstract class to get factories for Printer and Shape Objects.

```java title=Example.java
abstractclass AbstractFactory {
   abstract Printer getPrinter(String type);
   abstract Shape getShape(String shape) ;
}
```

Finally we create Factory classes extending AbstractFactory to generate object of concrete class based on given information.

```java title=Example.java
class ShapeFactory extends AbstractFactory {
   @Override
   public Shape getShape(String shapeType){
      if(shapeType == null){
         return null;
      }
      if(shapeType.equalsIgnoreCase("CIRCLE")){
         return new Circle();
      } elseif(shapeType.equalsIgnoreCase("RECTANGLE")){
         return new Rectangle();
      } elseif(shapeType.equalsIgnoreCase("SQUARE")){
         return new Square();
      }
      return null;
   }
   @Override
   Printer getPrinter(String type) {
      return null;
   }
}
class PrinterFactory extends AbstractFactory {
   @Override
   public Shape getShape(String shapeType){
      return null;
   }
   @Override
   Printer getPrinter(String type) {
   if(type == null){
      return null;
    }
  if(type.equalsIgnoreCase("paper")){
      return new PaperPrinter();
  } elseif(type.equalsIgnoreCase("web")){
      return new WebPrinter();
  } elseif(type.equalsIgnoreCase("Screen")){
      return new ScreenPrinter();
  }
  return null;
 }
}
```

Create a Factory generator/producer class to get factories by passing an information such as Shape or Printer

```java title=Example.java
class FactoryProducer {
   publicstatic AbstractFactory getFactory(String choice){
      if(choice.equalsIgnoreCase("SHAPE")){
         return new ShapeFactory();
      } elseif(choice.equalsIgnoreCase("Printer")){
         return new PrinterFactory();
      }
      return null;
   }
}
```

The following code shows how to use the abstract factory patterns.

```java title=Example.java
publicclass Main {
   publicstatic void main(String[] args) {
      //get shape factory
      AbstractFactory shapeFactory = FactoryProducer.getFactory("SHAPE");
      //get an object of Shape Circle
      Shape shape1 = shapeFactory.getShape("CIRCLE");
      //call draw method of Shape Circle
      shape1.draw();
      //get an object of Shape Rectangle
      Shape shape2 = shapeFactory.getShape("RECTANGLE");
      //call draw method of Shape Rectangle
      shape2.draw();
      //get an object of Shape Square
      Shape shape3 = shapeFactory.getShape("SQUARE");
      //call draw method of Shape Square
      shape3.draw();
      //get printer factory
      AbstractFactory printerFactory = FactoryProducer.getFactory("printer");
    Printer printer1 = printerFactory.getPrinter("Paper");
    printer1.print();
    Printer printer2 = printerFactory.getPrinter("Web");
    printer2.print();
    Printer printer3 = printerFactory.getPrinter("Screen");
    printer3.print();
   }
}
```

The code above generates the following result.

- « Previous
