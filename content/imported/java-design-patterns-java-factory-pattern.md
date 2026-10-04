---
title: Java Design Patterns Tutorial - Java Design Pattern - Factory Pattern
nav: Java Design Patterns Tutor...
description: Factory pattern is a creational pattern as this pattern provides better ways to create an object.
section: Imported - java2s Archive
order: 50112
source: https://www.java2s.com/Tutorials/Java/Java_Design_Patterns/0010__Java_Factory_Pattern.html
---
```java title=Example.java
```

Factory pattern is a creational pattern as this pattern provides better ways to create an object.

In Factory pattern, we create object without exposing the creation logic to the client.

## Example

In the following sections we will show how to use Factory Pattern to create objects.

The objects created by the factory pattern would be shape objects, such as Circle, Rectangle.

First we design an interface to represent Shape.

```java title=Example.java
publicinterface Shape {
   void draw();
}
```

Then we create concrete classes implementing the interface.

The following code is for Rectangle.java

```java title=Example.java
publicclass Rectangle implements Shape {
   @Override
   public void draw() {
      System.out.println("Inside Rectangle::draw() method.");
   }
}
```

Square.java

```java title=Example.java
publicclass Square implements Shape {
   @Override
   public void draw() {
      System.out.println("Inside Square::draw() method.");
   }
}
```

Circle.java

```java title=Example.java
publicclass Circle implements Shape {
   @Override
   public void draw() {
      System.out.println("Inside Circle::draw() method.");
   }
}
```

The core factory pattern is a Factory class. The following code shows how to create a Factory class for Shape objects.

The ShapeFactory class creates Shape object based on the String value passed in to the getShape() method. If the String value is CIRCLE, it will create a Circle object.

```java title=Example.java
publicclass ShapeFactory {
   //use getShape method to get object of type shape
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
}
```

The following code has main method and it uses the Factory class to get object of concrete class by passing an information such as type.

```java title=Example.java
publicclass Main {
   publicstatic void main(String[] args) {
      ShapeFactory shapeFactory = new ShapeFactory();
      //get an object of Circle and call its draw method.
      Shape shape1 = shapeFactory.getShape("CIRCLE");
      //call draw method of Circle
      shape1.draw();
      //get an object of Rectangle and call its draw method.
      Shape shape2 = shapeFactory.getShape("RECTANGLE");
      //call draw method of Rectangle
      shape2.draw();
      //get an object of Square and call its draw method.
      Shape shape3 = shapeFactory.getShape("SQUARE");
      //call draw method of circle
      shape3.draw();
   }
}
```

The code above generates the following result.

- « Previous
