---
title: Scala Tutorial - Scala Companion Objects
nav: Scala Tutorial - Scala Com...
description: In Scala, both a class and an object can share the same name.
section: Imported - java2s Archive
order: 50107
source: https://www.java2s.com/Tutorials/Java/Scala/3070__Scala_Companion_Objects.html
---
In Scala, both a class and an object can share the same name.

When an object shares a name with a class, it's called a companion object, and the class is called a companion class.

A companion object is an object that shares the same name and source file with another class or trait.

A trait could be seen as a Java interface.

This approach allows us to create static members on a class.

The companion object is useful for implementing helper methods and factory.

To implement a factory that creates different types of shapes, we can create a shape factory in Scala.

## Example

We use a companion class Shape and a companion object Shape, which acts as a factory.

```java title=Example.java
trait Shape {
    def area :Double
}
object Shape {
    privateclass Circle(radius: Double) extends Shape{
        override val area = 3.14*radius*radius
    }
    privateclass Rectangle (height: Double, length: Double)extends Shape{
        override val area = height * length
    }
    def apply(height :Double , length :Double ) : Shape = new Rectangle(height,length)
    def apply(radius :Double) : Shape = new Circle(radius)
}
object Main extends App {
    val circle = Shape(2)
    println(circle.area)
    val rectangle = Shape(2,3)
    println(rectangle.area)
}
```

## Note

A singleton object that does not share the same name with a companion class is called a standalone object.

- « Previous
