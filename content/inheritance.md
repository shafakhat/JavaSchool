---
title: Java Inheritance
nav: Inheritance
description: extends, super, method overriding, constructors in hierarchies, final classes and the Object class.
section: Object Oriented
order: 30
---

## The `extends` keyword

Inheritance lets a **subclass** reuse and specialize the fields and methods of a **superclass**.

```java title=Inheritance.java
class Animal {
    String name;

    void eat() {
        System.out.println(name + " eats");
    }

    void sleep() {
        System.out.println(name + " sleeps");
    }
}

class Dog extends Animal {
    void fetch() {                       // new behavior, only on Dog
        System.out.println(name + " fetches the ball");
    }
}

public class Inheritance {
    public static void main(String[] args) {
        Dog d = new Dog();
        d.name = "Rex";                  // inherited field
        d.eat();                         // inherited method
        d.fetch();                       // own method
    }
}
```

```text title=Output
Rex eats
Rex fetches the ball
```

Java has **single inheritance** - one `extends` only. (Multiple *interface* inheritance is allowed; see [Abstraction](abstraction.html).)

## `super` - reaching the parent

`super` refers to the immediate parent class:

```java title=Super.java
class Vehicle {
    int speed;

    Vehicle(int speed) {
        this.speed = speed;
        System.out.println("Vehicle built with speed " + speed);
    }

    void move() {
        System.out.println("moving at " + speed);
    }
}

class Bike extends Vehicle {
    boolean hasBell;

    Bike(int speed, boolean hasBell) {
        super(speed);        // run parent constructor FIRST
        this.hasBell = hasBell;
    }

    @Override
    void move() {            // override parent behavior
        super.move();        // optionally reuse parent logic
        System.out.println("(and it is silent!)");
    }

    public static void main(String[] args) {
        Bike b = new Bike(30, true);
        b.move();
    }
}
```

```text title=Output
Vehicle built with speed 30
moving at 30
(and it is silent!)
```

## Method overriding

A subclass can provide its own version of a parent method when signatures match:

| Requirement | Meaning |
|---|---|
| Same name | `move()` in both classes |
| Same parameters | parameter types and order must match |
| Compatible return | same type or a subtype (covariant returns) |
| Not `private`/`static` | those are *hidden*, not overridden |

The `@Override` annotation is optional but strongly recommended - the compiler then catches signature mismatches.

```java title=OverrideDemo.java
class Shape {
    double area() { return 0; }
}

class Circle extends Shape {
    double r;
    Circle(double r) { this.r = r; }

    @Override
    double area() { return Math.PI * r * r; }
}

class Rectangle extends Shape {
    double w, h;
    Rectangle(double w, double h) { this.w = w; this.h = h; }

    @Override
    double area() { return w * h; }
}

public class OverrideDemo {
    public static void main(String[] args) {
        Shape[] shapes = { new Circle(1), new Rectangle(2, 3) };
        for (Shape s : shapes) {
            System.out.println(s.area());   // each shape computes its OWN way
        }
    }
}
```

That last pattern - one variable type, many behaviors - is [polymorphism](polymorphism.html).

## Inheriting constructors

```java title=CtorInherit.java
class Base {
    String who;
    Base(String who) { this.who = who; }
}

class Child extends Base {
    Child(String who) {
        super(who);        // explicit call - Java has no implicit parent chaining
    }

    public static void main(String[] args) {
        System.out.println(new Child("Mira").who);
    }
}
```

- If the parent has a no-arg constructor and you write none, the compiler inserts `super()` automatically.
- Otherwise you must call `super(...)` explicitly as the first line.

## `final` - stopping inheritance

```java title=FinalClass.java
final class Money {
    double amount;
    Money(double amount) { this.amount = amount; }
}

// class MoreMoney extends Money { }   // ERROR: cannot extend a final class

class Account {
    final void close() {                // subclasses cannot override this
        System.out.println("account closed");
    }
}

public class FinalClass {
    public static void main(String[] args) {
        new Account().close();
    }
}
```

Use `final` on classes/methods when overriding would be dangerous (`String`, `Integer`, `Math` are all final in the JDK).

## The `Object` class

Every class inherits from `java.lang.Object`, so all objects have these methods:

| Method | Purpose |
|---|---|
| `toString()` | text representation |
| `equals(Object)` | logical equality |
| `hashCode()` | hash bucket (must match `equals`) |
| `clone()` | copy (requires `Cloneable`) |
| `getClass()` | runtime class info |

```java title=OverrideObject.java
class User {
    String email;

    User(String email) { this.email = email; }

    @Override
    public String toString() { return "User(" + email + ")"; }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof User other)) return false;
        return email.equals(other.email);
    }

    @Override
    public int hashCode() { return email.hashCode(); }

    public static void main(String[] args) {
        User a = new User("a@x.com");
        User b = new User("a@x.com");
        System.out.println(a);                  // User(a@x.com) - custom toString
        System.out.println(a.equals(b));        // true - custom equals
    }
}
```

> **Remember:** If you override `equals`, you **must** override `hashCode` with the same fields - otherwise `HashMap`/`HashSet` will treat equal objects as different.

## The `instanceof` pattern

Use `instanceof` to check type safely (Java 16+ can even pattern-match):

```java title=InstanceOf.java
public class InstanceOf {
    public static void main(String[] args) {
        Object v = "hello";

        if (v instanceof String s) {          // pattern variable 's' is in scope below
            System.out.println(s.length());   // 5
        }
        if (v instanceof Number) {
            System.out.println("a number");
        } else {
            System.out.println("not a number");
        }
    }
}
```

Too many `instanceof` checks in one method often signal missing polymorphism - consider moving the behavior into an overridden method instead.

Next: [Polymorphism](polymorphism.html) - one interface, many forms.
