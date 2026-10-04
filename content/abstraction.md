---
title: Java Abstraction (Abstract Classes & Interfaces)
nav: Abstraction
description: Abstract classes vs interfaces, default methods, functional interfaces and when to use each.
section: Object Oriented
order: 60
---

## Hiding the "how"

**Abstraction** exposes *what* an object does, and hides *how* it does it. In Java you get two tools:

| Tool | Use when |
|---|---|
| `abstract class` | you share state and partial implementation among related classes |
| `interface` | you define a contract that unrelated classes can implement |

```text title=Abstraction in one picture
        <<interface>> PaymentGateway            (contract)
              ^
   +----------+----------+
   |                     |
 CardGateway        UpiGateway                (implementations)
 (does the how)     (does the how)
```

## Abstract classes

An `abstract` class cannot be instantiated; it may mix abstract methods (no body) with concrete ones:

```java title=AbstractDemo.java
abstract class Employee {
    private String name;

    protected Employee(String name) {
        this.name = name;
    }

    public String getName() { return name; }

    // every employee earns something - but each type differs:
    abstract double monthlyPay();

    // shared, concrete behavior
    void printPayslip() {
        System.out.printf("%s: pay = %.0f%n", name, monthlyPay());
    }
}

class Salaried extends Employee {
    private double monthly;

    Salaried(String name, double monthly) {
        super(name);
        this.monthly = monthly;
    }

    @Override
    double monthlyPay() { return monthly; }
}

class Contractor extends Employee {
    private double dayRate;
    private int days;

    Contractor(String name, double dayRate, int days) {
        super(name);
        this.dayRate = dayRate;
        this.days = days;
    }

    @Override
    double monthlyPay() { return dayRate * days; }
}

public class AbstractDemo {
    public static void main(String[] args) {
        // Employee e = new Employee("x");    // ERROR: abstract class
        Employee[] staff = {
            new Salaried("Noor", 90000),
            new Contractor("Dev", 4500, 14)
        };
        for (Employee e : staff) {
            e.printPayslip();              // shared method, per-class pay
        }
    }
}
```

```text title=Output
Noor: pay = 90000
Dev: pay = 63000
```

## Interfaces - the contract

An interface declares *capabilities*. Fields in interfaces are implicitly `public static final`; methods are `public abstract` by default.

```java title=Interface.java
interface Printable {
    void print();                       // public abstract by default
}

interface Searchable {
    boolean matches(String query);
}

class Document implements Printable, Searchable {
    private String text;

    Document(String text) { this.text = text; }

    @Override
    public void print() {
        System.out.println("--- " + text + " ---");
    }

    @Override
    public boolean matches(String query) {
        return text.toLowerCase().contains(query.toLowerCase());
    }

    public static void main(String[] args) {
        Document d = new Document("Quarterly revenue grew 12%");
        d.print();
        System.out.println("found revenue? " + d.matches("revenue"));
    }
}
```

Because Java has single *class* inheritance but unlimited interface implementation, interfaces are how you get "multiple inheritance of type".

## Default methods (Java 8+)

Interfaces can ship concrete methods - you evolve the API without breaking existing implementors:

```java title=DefaultMethodsClean.java
interface Greeter {
    String name();

    default void greet() {
        System.out.println("Hello, " + name() + "!");
    }
}

class Human implements Greeter {
    @Override
    public String name() { return "Ada"; }
}

class Robot implements Greeter {
    @Override
    public String name() { return "R2-D2"; }
}

public class DefaultMethodsClean {
    public static void main(String[] args) {
        Greeter[] gs = { new Human(), new Robot() };
        for (Greeter g : gs) {
            g.greet();            // default method runs for both
        }
    }
}
```

```text title=Output
Hello, Ada!
Hello, R2-D2!
```

An implementing class only provides the abstract methods - inherited `default` methods come for free:

```java title=DefaultRules.java
interface Shape2D {
    double area();

    default void printArea() {
        System.out.printf("area = %.2f%n", area());
    }

    static boolean isPositive(double v) {   // static interface method
        return v > 0;
    }
}

public class DefaultRules implements Shape2D {
    private final double w, h;
    DefaultRules(double w, double h) { this.w = w; this.h = h; }

    @Override
    public double area() { return w * h; }

    public static void main(String[] args) {
        DefaultRules r = new DefaultRules(3, 4);
        r.printArea();                                   // inherited default
        System.out.println(Shape2D.isPositive(r.area())); // interface static
    }
}
```

Rules: `default` methods may be overridden; `static` interface methods are called on the interface itself; interfaces still cannot declare instance fields.

## Abstract class vs interface - choosing

|  | Abstract class | Interface |
|---|---|---|
| Fields | instance fields allowed | only constants |
| Constructors | yes | no |
| State sharing | yes (common fields) | no |
| Multiple inheritance | one class only | many interfaces |
| Typical role | "is-a" base with shared state | "can-do" capability |
| Evolving safely | adding methods can break subclasses | `default` methods don't |

Rules of thumb:

- Modeling **identity** ("every `Car` is a `Vehicle`") → abstract class.
- Modeling **capability** ("things that can `Swim`/`Fly`") → interface.
- Start with an interface when unsure; promote to abstract class if you need shared state.

## Functional interfaces

An interface with exactly **one** abstract method can be used as a lambda target:

```java title=FuncInt.java
interface Transformer {
    String apply(String input);
}

public class FuncInt {
    static String transform(String in, Transformer t) {
        return t.apply(in);
    }

    public static void main(String[] args) {
        System.out.println(transform("java", s -> s.toUpperCase()));  // JAVA
        System.out.println(transform("java", String::valueOf));      // java

        // JDK built-ins: Runnable, Comparator, Predicate, Function...
        Runnable r = () -> System.out.println("lambda implements Runnable");
        r.run();
    }
}
```

That single trick powers all of [lambdas and streams](lambdas.html).

## Sealed interfaces (Java 17+)

When you must control who can implement:

```java title=Sealed.java
sealed interface Result permits Success, Failure { }
record Success(String data) implements Result { }
record Failure(String error) implements Result { }

public class Sealed {
    public static void main(String[] args) {
        Result r = new Success("42");
        String out = switch (r) {          // compiler knows all subtypes
            case Success s -> "ok: " + s.data();
            case Failure f -> "err: " + f.error();
        };
        System.out.println(out);
    }
}
```

Exhaustive `switch` over sealed types is one of modern Java's nicest features.

Next: [Packages](packages.html) - organizing classes into namespaces.
