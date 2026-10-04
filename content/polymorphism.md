---
title: Java Polymorphism
nav: Polymorphism
description: Compile-time and runtime polymorphism, dynamic method dispatch, abstract classes and interfaces in action.
section: Object Oriented
order: 40
---

## One name, many forms

**Polymorphism** lets you treat objects of different classes through a single reference type, while each object responds in its own way.

```text title=The idea
   Shape ref
      |
      +--> Circle  : area() = pi*r*r
      +--> Square  : area() = side*side
      +--> Triangle: area() = 0.5*b*h
```

There are two flavors:

| Kind | Also called | Resolved by |
|---|---|---|
| Compile-time | static, overloading | argument types at the call site |
| Runtime | dynamic, overriding | actual object type at runtime |

## Runtime polymorphism (overriding)

This is the important one. A parent reference can point to any child object, and calls dispatch to the **actual object's** implementation (dynamic method dispatch):

```java title=Polymorphism.java
class Animal {
    void speak() {
        System.out.println("...");
    }
}

class Cat extends Animal {
    @Override
    void speak() {
        System.out.println("Meow");
    }
}

class Dog extends Animal {
    @Override
    void speak() {
        System.out.println("Woof");
    }
}

public class Polymorphism {
    static void makeItSpeak(Animal a) {     // one parameter type...
        a.speak();                          // ...many behaviors
    }

    public static void main(String[] args) {
        makeItSpeak(new Cat());   // Meow
        makeItSpeak(new Dog());   // Woof
        makeItSpeak(new Animal()); // ...

        Animal a = new Dog();     // parent reference, child object
        a.speak();                // Woof - runtime type wins
        // a.fetch();             // ERROR: compiler only knows 'Animal'
    }
}
```

### Why it matters

- **New subtypes don't break old code.** Add `class Parrot extends Animal` and every `Animal`-taking method works unchanged.
- **Tests can substitute fakes** (e.g. a `MockRepository implements Repository`).

## Arrays and collections of supertypes

```java title=ShapeDemo.java
abstract class Shape {
    abstract double area();

    @Override
    public String toString() {
        return getClass().getSimpleName() + "(" + String.format("%.2f", area()) + ")";
    }
}

class Circle extends Shape {
    double r;
    Circle(double r) { this.r = r; }
    @Override double area() { return Math.PI * r * r; }
}

class Square extends Shape {
    double side;
    Square(double side) { this.side = side; }
    @Override double area() { return side * side; }
}

public class ShapeDemo {
    public static void main(String[] args) {
        Shape[] shapes = { new Circle(2), new Square(3), new Circle(0.5) };

        double total = 0;
        for (Shape s : shapes) {
            total += s.area();          // correct version called per object
            System.out.println(s);      // uses overridden toString()
        }
        System.out.printf("total area = %.2f%n", total);
    }
}
```

```text title=Output
Circle(12.57)
Square(9.00)
Circle(0.79)
total area = 22.35
```

## Compile-time polymorphism (overloading)

Resolved by the compiler from the **static** argument types - see [Methods](methods.html):

```java title=Overloading.java
public class Overloading {
    static String describe(int x)        { return "int: " + x; }
    static String describe(double x)     { return "double: " + x; }
    static String describe(String x)     { return "String: " + x; }

    public static void main(String[] args) {
        System.out.println(describe(1));        // int: 1     (picked at compile time)
        System.out.println(describe(1.5));      // double: 1.5
        System.out.println(describe("hi"));     // String: hi

        Object o = 1;
        System.out.println(describe((String) o)); // compile error - types don't match
    }
}
```

## The rules of the game

1. **Overload** = same method name, different parameters; chosen by the compiler.
2. **Override** = same signature in subclass; chosen by the runtime object.
3. Private/static/final methods are not polymorphic (they are hidden or sealed).
4. The reference type controls what you can **call**; the object type controls what **runs**.

```java title=ReferenceVsObject.java
class Parent {
    void hello() { System.out.println("Parent says hi"); }
}

class Child extends Parent {
    @Override
    void hello() { System.out.println("Child says hi"); }

    void extra() { System.out.println("Child-only feature"); }
}

public class ReferenceVsObject {
    public static void main(String[] args) {
        Parent ref = new Child();     // compile-time type: Parent
                                      // runtime type:      Child
        ref.hello();                  // Child says hi  (runtime wins)
        // ref.extra();               // ERROR: Parent doesn't declare extra()

        ((Child) ref).extra();        // explicit downcast works when safe
    }
}
```

## Downcasting and `instanceof`

```java title=DowncastSafe.java
public class DowncastSafe {
    static class Parent {
        void hello() { System.out.println("Parent says hi"); }
    }

    static class Child extends Parent {
        void extra() { System.out.println("Child-only feature"); }
    }

    public static void main(String[] args) {
        Parent ref = new Child();

        if (ref instanceof Child c) {   // safe check + cast in one step (Java 16+)
            c.extra();
        }
        // Child c2 = (Child) ref;      // would work here, but throws
        //                             // ClassCastException if wrong type
    }
}
```

> **Warning:** Casting to the wrong runtime type throws `ClassCastException`. Always guard with `instanceof` first (or use the pattern form shown above).

## When polymorphism isn't possible

```java title=Gotchas.java
class P {
    String field = "P.field";
    static void helloStatic() { System.out.println("Parent static"); }
}

class C extends P {
    String field = "C.field";        // shadows P.field
    static void helloStatic() { System.out.println("Child static"); }
}

public class Gotchas {
    public static void main(String[] args) {
        // 1) static methods are hidden, not overridden - picked by reference type
        P ref = new C();
        P.helloStatic();             // Parent static (compile-time type wins)

        // 2) fields are shadowed, not polymorphic
        System.out.println(ref.field);        // P.field
        System.out.println(((C) ref).field);  // C.field
    }
}
```

For static methods and fields, the **compile-time** type decides. This is a classic interview trap.

## Design tip

If you find yourself writing long chains of `if (x instanceof A) ... else if (x instanceof B)`, push each branch into the class where it belongs:

```text title=Before -> after
before:  if (shape instanceof Circle) area = pi*r*r;      // one god-method
         else if (shape instanceof Square) area = side*side;

after:   area = shape.area();      // each class knows its own math
```

That is the Open/Closed principle: **open for extension, closed for modification**.

Next: [Encapsulation](encapsulation.html) - protecting the data behind methods.
