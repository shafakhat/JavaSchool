---
title: Scala Tutorial - Scala Inheritance
nav: Scala Tutorial - Scala Inh...
description: The root of the Scala class hierarchy is Any, which has no parent.
section: Imported - java2s Archive
order: 50105
source: https://www.java2s.com/Tutorials/Java/Scala/3050__Scala_Inheritance.html
---
```java title=Example.java
```

Scala supports single inheritance, not multiple inheritance.

A child class can have one and only one parent class.

The root of the Scala class hierarchy is Any, which has no parent.

```java title=Example.java
class Vehicle (speed : Int){
    val mph :Int = speed
    def race() = println("Racing")
}
```

The Vehicle class takes one argument, which is the speed of the vehicle.

This argument must be passed when creating an instance of class Vehicle, as follows:

```java title=Example.java
new Vehicle(100)
```

The class contains one method, called race.

## Extending Class

Extending from a base class in Scala is similar to extending in Java except for two restrictions:

- method overriding requires the override keyword,
- only the primary constructor can pass parameters to the base constructor.

It is possible to override methods inherited from a super class in Scala as follows:

```java title=Example.java
class Car (speed : Int) extends Vehicle(speed) {
    override val mph: Int= speed
    override def race() = println("Racing Car")
}
```

The class Car extends Vehicle class using the keyword extends.

```java title=Example.java
The field mph and the method race
needs to be overridden using the keyword override.
```

## Note

The following code shows another class Bike that extends Vehicle.

```java title=Example.java
class Vehicle (speed : Int){
    val mph :Int = speed
    def race() = println("Racing")
}
class Car (speed : Int) extends Vehicle(speed) {
    override val mph: Int= speed
    override def race() = println("Racing Car")
}
class Bike(speed : Int) extends Vehicle(speed) {
    override val mph: Int = speed
    override def race() = println("Racing Bike")
}
object Main extends App {
    val vehicle1 = new Car(200)
    println(vehicle1.mph )
    vehicle1.race()
    val vehicle2 = new Bike(100)
    println(vehicle2.mph )
}
```

- « Previous
