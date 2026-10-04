---
title: OCA Java SE 8 Class Design - Java Class Design
nav: OCA Java SE 8 Class Design...
description: When creating a new class in Java, you can create the class to inherit from an existing class.
section: Imported - java2s Archive
order: 1012
source: https://web.archive.org/web/2016/https://www.java2s.com/Tutorials/Java/OCA_Java_SE_8_Class_Design/index.html
---
When creating a new class in Java, you can create the class to inherit from an existing class.

During class inheritance the new child subclass includes any public or protected primitives, objects, or methods defined in the parent class.

We refer to class that inherits from another class as a child class, or a descendent of that class.

We refer to the class that the child inherits from as the parent class, or an ancestor of the class.

If child X inherits from class Y, which inherits from class Z, then X would be considered an indirect child, or descendent, of class Z.

Java supports single inheritance: a class may inherit from only one direct parent class.

Java supports multiple levels of inheritance: one class may extend another class, which in turn extends another class.

You can extend a class any number of times.

To prevent a class from being extended by marking the class with the final modifier.

## Extending a Class

In Java, you can extend a class by adding the parent class name in the definition using the extends keyword.

The following code shows how to create class inheritance in Java.

```java title=Example.java
class Shape {
  private int edge;
  public int getEdge() {
    return edge;
  }
  public void setAge(int edge) {
    this.edge = edge;
  }
}
class Rectangle extends Shape {
  private void output() {
    System.out.println("The "+getEdge()+" is 4!");
  }
}
```

extends keyword indicates that the Rectangle class extends from the Shape class.

In this example, we see that getEdge() and setAge() are accessible by subclass Rectangle, since they are marked as public in the parent class.

The primitive edge is marked as private and therefore not accessible from the subclass Rectangle, as the following would not compile:

```java title=Example.java
class Rectangle extends Shape {
  private void output() {
    System.out.println(edge);   // DOES NOT COMPILE
  }
}
```

Even though edge variable is inaccessible by the child class, there is an edge value that exists within the instance.

The edge value cannot be directly referenced by the child class nor any instance of the class.

## Applying Class Access Modifiers

The public access modifier applied to a class says that the class can be referenced and used in any class.

The default package private modifier, which is the lack of any access modifier, says that the class can be accessed only by a subclass or class within the same package.

A Java file can have many classes but at most one public class.

In fact, it may have no public class at all.

One feature of using the default package private modifier is that you can define many classes within the same Java file.

```java title=Example.java
class A {}
public class G extends A{}
```

There can be at most one public class or interface in a Java file.

Top-level interfaces can also be declared with the public or default modifiers.

## java.lang.Object

In Java, all classes inherit from a single class, java.lang.Object.

java.lang.Object is the only class that doesn't have any parent classes.

The compiler automatically inserts code into any class you write that doesn't extend a specific class.

For example, consider the following two equivalent class definitions:

```java title=Example.java
public class Main {
}
public class Main extends java.lang.Object {
}
```

when Java sees you define a class without extending another class, it adds the syntax extends java.lang.Object to the class definition.
