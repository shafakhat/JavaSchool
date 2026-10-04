---
title: Java Object Oriented Design - Java Abstract Classes and Methods
nav: Java Object Oriented Desig...
description: Its purpose is just to represent an idea, which is common to objects of other classes.
section: Imported - java2s Archive
order: 50169
source: https://www.java2s.com/Tutorials/Java/Java_Object_Oriented_Design/0340__Java_Abstract_Classes_Methods.html
---
```java title=Example.java
```

Java can define a class whose objects cannot be created.

Its purpose is just to represent an idea, which is common to objects of other classes.

Such a class is called an abstract class.

## Syntax

We need to use the abstract keyword in the class declaration to declare an abstract class.

For example, the following code declares a Shape class abstract:

```java title=Example.java
publicabstractclass Shape  {
}
```

The following code adds a draw() method to Shape class.

```java title=Example.java
publicabstractclass Shape  {
    public  Shape() {
    }
    publicabstract  void  draw();
}
```

A abstract class does not necessarily mean that it has at least one abstract method.

If a class has an abstract method either declared or inherited, it must be declared abstract.

An abstract method is declared the same way as any other methods, except that its body is indicated by a semicolon.

## Example

The following Shape class has both abstract and non-abstract methods.

```java title=Example.java
abstractclass Shape {
  private String name;
public Shape() {
    this.name = "Unknown  shape";
  }
  public Shape(String name) {
    this.name = name;
  }
  public String getName() {
    return this.name;
  }
  publicvoid setName(String name) {
    this.name = name;
  }
  // Abstract methods
publicabstractvoid draw();
  publicabstractdouble getArea();
  publicabstractdouble getPerimeter();
}
```

The following code shows how to create a Rectangle class, which inherits from the Shape class.

```java title=Example.java
class Rectangle extends Shape {
  private double width;
  private double height;
  public Rectangle(double width, double height) {
    // Set the shape name as"Rectangle"
    super("Rectangle");
    this.width = width;
    this.height = height;
  }
  // Provide an implementation for inherited abstract draw() method
  public void draw() {
    System.out.println("Drawing a  rectangle...");
  }
  // Provide an implementation for inherited abstract getArea() method
  public double getArea() {
    return width * height;
  }
  // Provide an implementation for inherited abstract getPerimeter() method
  public double getPerimeter() {
    return 2.0 * (width + height);
  }
}
```

- « Previous
