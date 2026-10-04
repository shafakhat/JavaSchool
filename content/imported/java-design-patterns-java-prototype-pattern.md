---
title: Java Design Patterns Tutorial - Java Design Pattern - Prototype Pattern
nav: Java Design Patterns Tutor...
description: Prototype pattern helps create duplicate object with better performance.
section: Imported - java2s Archive
order: 50116
source: https://www.java2s.com/Tutorials/Java/Java_Design_Patterns/0050__Java_Prototype_Pattern.html
---
Prototype pattern is one of the creational patterns.

Prototype pattern helps create duplicate object with better performance.

In Prototype Pattern a clone of an existing object is returned instead of creating new one.

We use Prototype Design Pattern, if the cost of creating a new object is expensive and resource intensive.

## Example

The following code shows how to use Prototype Pattern to create objects.

First it create a Shape abstract class which implements the Cloneable interface.

```java title=Example.java
abstractclass Shape implements Cloneable {
   private String id;
   protected String type;
   abstract void draw();
   public String getType(){
      return type;
   }
   public String getId() {
      return id;
   }
   public void setId(String id) {
      this.id = id;
   }
   public Object clone() {
      Object clone = null;
      try {
         clone = super.clone();
      } catch (CloneNotSupportedException e) {
         e.printStackTrace();
      }
      return clone;
   }
}
```

Then it creates three concrete classes extending the Shape class.

```java title=Example.java
class Rectangle extends Shape {
   public Rectangle(){
     type = "Rectangle";
   }
   @Override
   public void draw() {
      System.out.println("Inside Rectangle::draw() method.");
   }
}
class Square extends Shape {
   public Square(){
     type = "Square";
   }
   @Override
   public void draw() {
      System.out.println("Inside Square::draw() method.");
   }
}
class Circle extends Shape {
   public Circle(){
     type = "Circle";
   }
   @Override
   public void draw() {
      System.out.println("Inside Circle::draw() method.");
   }
}
```

After that it creates a ShapeProtoType class to return the prototype of shapes.

```java title=Example.java
class ShapeProtoType{
  privatestatic Hashtable<String, Shape> shapeMap
      = new Hashtable<String, Shape>();
   publicstatic Shape getShape(String shapeId) {
      Shape cachedShape = shapeMap.get(shapeId);
      return (Shape) cachedShape.clone();
   }
   publicstaticvoid loadCache() {
      Circle circle = new Circle();
      circle.setId("1");
      shapeMap.put(circle.getId(),circle);
      Square square = new Square();
      square.setId("2");
      shapeMap.put(square.getId(),square);
      Rectangle rectangle = new Rectangle();
      rectangle.setId("3");
      shapeMap.put(rectangle.getId(),rectangle);
   }
}
publicclass Main{
   publicstaticvoid main(String[] args) {
      ShapeProtoType.loadCache();
      Shape clonedShape = (Shape) ShapeProtoType.getShape("1");
      System.out.println("Shape : " + clonedShape.getType());
      Shape clonedShape2 = (Shape) ShapeProtoType.getShape("2");
      System.out.println("Shape : " + clonedShape2.getType());
      Shape clonedShape3 = (Shape) ShapeProtoType.getShape("3");
      System.out.println("Shape : " + clonedShape3.getType());
   }
}
```

The code above generates the following result.

- « Previous
