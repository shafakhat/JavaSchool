---
title: Java Constructors
nav: Constructors
description: Default, parameterized and copy constructors, constructor chaining and the this() call.
section: Object Oriented
order: 20
---

## What is a constructor?

A constructor is a special method that **runs when an object is created**. It has the class's name, no return type, and its job is to leave the new object in a valid state.

```java title=Constructor.java
public class Constructor {
    String name;
    int age;

    // parameterized constructor
    Constructor(String name, int age) {
        this.name = name;
        this.age = age;
        System.out.println("Created " + name);
    }

    public static void main(String[] args) {
        Constructor p = new Constructor("Aarav", 25);   // constructor runs here
        System.out.println(p.name + " is " + p.age);
    }
}
```

```text title=Output
Created Aarav
Aarav is 25
```

## The default constructor

If you write **no** constructor at all, the compiler inserts a no-argument one:

```java title=DefaultCtor.java
public class DefaultCtor {
    int x;

    public static void main(String[] args) {
        DefaultCtor a = new DefaultCtor();   // implicit default constructor
        System.out.println(a.x);             // 0
    }
}
```

> **Warning:** As soon as you write *any* constructor, the default one **disappears**. `new DefaultCtor()` then fails to compile unless you provide it yourself.

## Multiple constructors (overloading)

```java title=Overloaded.java
public class Overloaded {
    String model;
    int year;

    Overloaded() {
        this("unknown", 2000);       // delegate to the other constructor
    }

    Overloaded(String model) {
        this(model, 2026);
    }

    Overloaded(String model, int year) {
        this.model = model;
        this.year = year;
    }

    public static void main(String[] args) {
        Overloaded a = new Overloaded();
        Overloaded b = new Overloaded("Octavia");
        Overloaded c = new Overloaded("Octavia", 2024);
        System.out.println(a.model + "/" + a.year);   // unknown/2000
        System.out.println(b.model + "/" + b.year);   // Octavia/2026
        System.out.println(c.model + "/" + c.year);   // Octavia/2024
    }
}
```

Rules for `this(...)` chaining:

- It must be the **first statement** in the constructor.
- A constructor may chain **once** (no cycles).

## Constructor chaining between classes: `super`

Every constructor (except `Object`'s) must call another constructor of *its own* class (`this(...)`) or the **parent's** constructor (`super(...)`), implicitly if you don't write it:

```java title=SuperChain.java
class Animal {
    String kind;

    Animal(String kind) {
        this.kind = kind;
        System.out.println("Animal ctor: " + kind);
    }
}

class Dog extends Animal {
    String name;

    Dog(String name) {
        super("canine");        // must be first line - parent initializes first
        this.name = name;
        System.out.println("Dog ctor: " + name);
    }

    public static void main(String[] args) {
        new Dog("Rex");
    }
}
```

```text title=Output
Animal ctor: canine
Dog ctor: Rex
```

## The copy constructor

Java has no built-in copy constructor - you write it yourself:

```java title=CopyCtor.java
public class CopyCtor {
    String label;
    int[] data;

    CopyCtor(String label, int[] data) {
        this.label = label;
        this.data = data.clone();          // defensive copy
    }

    // copy constructor
    CopyCtor(CopyCtor other) {
        this(other.label, other.data);
    }

    public static void main(String[] args) {
        CopyCtor original = new CopyCtor("first", new int[]{1, 2});
        CopyCtor copy = new CopyCtor(original);
        copy.data[0] = 99;
        System.out.println(original.data[0]);   // 1 - unaffected
        System.out.println(copy.data[0]);       // 99
    }
}
```

Copying `data` by reference instead of `clone()` would make the two objects silently share state - usually a bug.

## Validation in constructors

Constructors are the right place to **refuse invalid objects**:

```java title=Validate.java
public class Validate {
    private final int age;

    Validate(int age) {
        if (age < 0 || age > 150) {
            throw new IllegalArgumentException("age out of range: " + age);
        }
        this.age = age;
    }

    public static void main(String[] args) {
        Validate ok = new Validate(30);
        System.out.println("stored age = " + ok.age);
        try {
            new Validate(-5);
        } catch (IllegalArgumentException e) {
            System.out.println("rejected: " + e.getMessage());
        }
    }
}
```

An object that exists is always valid - no "half-built" states to defend against later.

## Static initializer vs constructor

```java title=StaticInit.java
public class StaticInit {
    static int shared;                 // class-level

    static {
        shared = 100;                  // runs ONCE when class loads
        System.out.println("class loaded");
    }

    int own;                           // object-level

    StaticInit() {
        own = 1;                       // runs for EVERY object
        System.out.println("object made");
    }

    public static void main(String[] args) {
        System.out.println("start");
        new StaticInit();
        new StaticInit();
        System.out.println("shared=" + shared);
    }
}
```

```text title=Output
start
class loaded      (exact order may vary with lazy class loading)
object made
object made
shared=100
```

## Checklist

- Initialize every field on all paths.
- Chain with `this(...)` to avoid duplicated setup.
- Validate inputs early and throw meaningful exceptions.
- Copy mutable arguments (`arrays`, `lists`) if the object must own them.

Next: [Inheritance](inheritance.html).
