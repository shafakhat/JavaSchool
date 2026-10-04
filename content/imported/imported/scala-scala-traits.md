---
title: Scala Tutorial - Scala Traits
nav: Scala Tutorial - Scala Tra...
description: Traits are like interfaces in Java, which can also contain code.
section: Imported - java2s Archive
order: 50104
source: https://www.java2s.com/Tutorials/Java/Scala/3040__Scala_Traits.html
---
```java title=Example.java
« Previous
```

- Next »

Traits are like interfaces in Java, which can also contain code.

In Scala, when a class inherits from a trait, it implements the interface of the trait, and inherits all the code contained in the trait.

In Scala, traits can inherit classes.

The keyword extends is also used when a class inherits a trait as its parent.

The keyword extends is also used even when the class mixes in other traits using the with keyword.

Also, extends is used when one trait is the child of another trait or class.

## Example

```java title=Example.java

trait flying {
    def fly() = println("flying")
}
trait gliding {
    def gliding() = println("gliding")
}
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
class AirCraft(speed : Int) extends Vehicle(speed) with flying with gliding{
    override val mph: Int = speed
    override def race() = println("Racing")
    override def fly() = println("Flying")
    override def gliding() = println("Gliding")
}
object Main extends App {
   val vehicle1 = new Car(200)
   val vehicle2 = new Bike(100)
   val vehicle3 = new AirCraft(300)
   vehicle3.fly()
   val vehicleList = List(vehicle1, vehicle2, vehicle3)
   println(vehicleList);
   val fastestVehicle = vehicleList.maxBy(_.mph)
   println(fastestVehicle);
}
```

- Next »
- « Previous
