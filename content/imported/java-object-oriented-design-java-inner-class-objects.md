---
title: Java Object Oriented Design - Java Inner Class Objects
nav: Java Object Oriented Desig...
description: Objects of a local inner class are created using the new operator inside the block, which declares the class.
section: Imported - java2s Archive
order: 50163
source: https://www.java2s.com/Tutorials/Java/Java_Object_Oriented_Design/0270__Java_Inner_Class_Objects.html
---
```java title=Example.java
```

Objects of a local inner class are created using the new operator inside the block, which declares the class.

An object of an anonymous class is created at the same time the class is declared.

A static member class is another type of top-level class.

You create objects of a static member class the same way you create objects of a top-level class.

An instance of a member inner class always exists within an instance of its enclosing class.

## Syntax

The general syntax to create an instance of a member inner class is as follows:

```java title=Example.java
OuterClassReference.new MemberInnerClassConstructor()
```

OuterClassReference is the reference of the enclosing class followed by a dot that is followed by the new operator.

## Example

The member inner class's constructor call follows the new operator.

```java title=Example.java
class Outer  {
    publicclass  Inner {
    }
}
```

To create an instance of the Inner member inner class, you must first create an instance of its enclosing class Outer.

```java title=Example.java
Outer  out  = new Outer();
```

Now, you need to use the new operator on the out reference variable to create an object of the Inner class.

```java title=Example.java
out.new Inner();
```

To store the reference of the instance of the Inner member inner class in a reference variable, we can write the following statement:

```java title=Example.java
Outer.Inner in = out.new   Inner();
```

The following code shows how to create Objects of a Member Inner Class

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
    Car c = new Car();
    Car.Tire t = c.new Tire(9);
  }
}
class Car {
  publicclass Tire {
    privateint size;
    public Tire(int size) {
      this.size = size;
    }
    public String toString() {
      return"Monitor   - Size:" + this.size + "  inch";
    }
  }
}
```

- « Previous
