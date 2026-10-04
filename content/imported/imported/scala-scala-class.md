---
title: Scala Tutorial - Scala Class
nav: Scala Tutorial - Scala Class
description: A class is a blueprint for creating objects that are the concrete instances of a class.
section: Imported - java2s Archive
order: 50099
source: https://www.java2s.com/Tutorials/Java/Scala/3000__Scala_Class.html
---
```java title=Example.java
« Previous
```

- Next »

A class is a blueprint for creating objects that are the concrete instances of a class.

A class definition consists of field declarations and method definitions.

Fields are used to store the state of an object and methods may provide access to fields, and alter the state of an object.

Let's start with a simple example of a blueprint for creating Book objects:

```java title=Example.java

class Book
```

The preceding Scala declaration corresponds to this Java declaration:

```java title=Example.java

public class Book {
}
```

Once you've defined a class, you can create objects from the class with the keyword new.

To create an instance of Book, you can type the following:

```java title=Example.java

new Book
```

This works just as well as the follows:

```java title=Example.java

new Book()
```

## Example

The following code create a class to represent shapes.

We defined a super type called Shape that has a method area that computes the area of the shape.

```java title=Example.java

class Shape {
   def area:Double = 0.0
}
```

The following code create classes for Rectangle and Circle.

```java title=Example.java

class Rectangle(val width:Double,val height:Double) extends Shape {
   override def area:Double = width*height
}
class Circle(val radius:Double) extends Shape {
   override def area:Double = math.Pi*radius*radius
}
```

Each of these classes takes some arguments and extends Shape, then overrides the method of Shape.

A subtype is guaranteed to have all the members of the supertype.

Changing the implementation of a method of the supertype is called overriding.

## Note

We cannot alter the width and the height of a Rectangle and the radius of the Circle objects because if the field is a val, Scala generates only a getter method for it.

This is an example of encapsulation. In encapsulation, the fields of an object are accessible only through its methods.

We can write code that takes an instance of Shape and then pass to it an instance of either Rectangle or Circle:

```java title=Example.java

def draw(s:Shape)
```

Now, consider two calls made to this function, like so:

```java title=Example.java

val circle = draw(new Circle(3))
val rectangle = draw(new Rectangle(2,3))
```

Inheritance guarantees that any method we could call on an instance of Shape will be defined in the subtypes.

- Next »
- « Previous
