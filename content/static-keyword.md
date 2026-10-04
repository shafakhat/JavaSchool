---
title: The static Keyword
nav: static Keyword
description: Static fields, methods, blocks and nested classes - members that belong to the class, not instances.
section: Object Oriented
order: 80
---

## Class-level, not object-level

Anything marked `static` belongs to the **class itself**. There is exactly one copy, shared by every instance. Non-static members exist once **per object**.

```text title=One static, many instance
        Counter (class)
        +--------------------+
        static total = 0      |   <- one copy, shared
        +--------------------+
             ^
   +---------+---------+
   | instance 1        |  instance 2
   | +--------------+  |  +--------------+
   | | id, name...  |  |  | id, name...  |  <- each object gets its own
   +-------------------+  +---------------+
```

## Static fields (shared state)

```java title=StaticField.java
public class StaticField {
    private static int instances = 0;   // shared by ALL objects
    private final int myNumber;

    public StaticField() {
        instances++;
        myNumber = instances;
    }

    public static int getInstanceCount() { return instances; }

    public static void main(String[] args) {
        new StaticField();
        new StaticField();
        StaticField third = new StaticField();
        System.out.println("total = " + StaticField.getInstanceCount());  // 3
        System.out.println("this one is #" + third.myNumber);             // 3
    }
}
```

That is how counters, caches, configuration and connection pools work.

## Static methods

A static method has **no `this`** - it cannot touch instance fields:

```java title=StaticMethod.java
public class StaticMethod {
    int value = 10;

    static int square(int n) { return n * n; }

    // static void broken() { System.out.println(value); }  // ERROR: no instance

    public static void main(String[] args) {
        System.out.println(square(7));            // called on the class
        StaticMethod obj = new StaticMethod();
        System.out.println(obj.square(7));        // legal, but style-wise: prefer ClassName.method()
    }
}
```

Characteristics:

- Called as `ClassName.method(...)`
- Cannot call instance methods or reference instance fields directly
- Can be overloaded, and can be hidden by a subclass (not overridden)
- Perfect for **utilities** (`Math.max`, `Integer.parseInt`, `Arrays.sort`)

## The static block

Static initializers run **once, when the class is first loaded** - ideal for complex setup:

```java title=StaticBlock.java
import java.util.Map;

public class StaticBlock {
    static final Map<String, String> CONFIG;

    static {
        // runs before the first use of this class
        Map<String, String> m = new java.util.HashMap<>();
        m.put("env", "production");
        m.put("region", "ap-south-1");
        CONFIG = java.util.Collections.unmodifiableMap(m);
    }

    public static void main(String[] args) {
        System.out.println(CONFIG);
        System.out.println("loaded at last");
    }
}
```

Multiple static blocks run in file order. They may not reference instance members (nothing exists yet).

## Static variables vs constants

```java title=Constants.java
public class Constants {
    public static final double PI = 3.141592653589793;   // constant - shared + immutable
    public static int counter = 0;                        // mutable shared state - use carefully

    public static void main(String[] args) {
        System.out.println(PI * 2);
        counter++;
        counter++;
        System.out.println(counter);   // 2 - still only one copy
    }
}
```

`static final` = compile-time constant when the value is a literal; `public static final` with UPPER_SNAKE_CASE is the universal constant style.

## Static vs instance - side by side

```java title=SideBySide.java
public class SideBySide {
    static int shared = 0;      // one for the class
    int own = 0;                // one per object

    void touch() {
        shared++;               // all objects add to the SAME counter
        own++;                  // each object has its OWN counter
    }

    public static void main(String[] args) {
        SideBySide a = new SideBySide();
        SideBySide b = new SideBySide();

        a.touch();
        a.touch();
        b.touch();

        System.out.println("shared = " + SideBySide.shared);  // 3
        System.out.println("a.own = " + a.own);               // 2
        System.out.println("b.own = " + b.own);               // 1
    }
}
```

## Static nested classes

A static nested class doesn't hold a reference to the outer instance - it behaves like a top-level class grouped for convenience:

```java title=Nested.java
public class Nested {
    private String name = "outer";

    static class Engine {
        int horsepower;
        Engine(int horsepower) { this.horsepower = horsepower; }
        void specs() { System.out.println(horsepower + " hp"); }
        // System.out.println(name);    // ERROR: no outer instance
    }

    public static void main(String[] args) {
        Engine e = new Engine(150);   // no need for a Nested instance
        e.specs();
    }
}
```

Compare with **inner** classes (non-static) that *do* capture the outer object - covered in [Inner Classes](inner-classes.html).

## Common mistakes

```java title=Mistakes.java
public class Mistakes {
    static int a = 5;
    int b = 6;

    // static void noThis() { System.out.println(b); }   // ERROR: instance field

    static void setA(int v) { a = v; }

    public static void main(String[] args) {
        // 1) calling an instance method statically
        // printB();                   // ERROR

        // 2) thinking static means "shared but private" -
        //    static just means ONE copy; visibility is a separate keyword
        setA(9);
        System.out.println(a);        // 9 - one copy, changed for everyone
    }
}
```

> **Remember:** `static` answers *"does this belong to the class or to each object?"* - it has nothing to do with access control (that's `private`/`public`).

Next: [Inner Classes](inner-classes.html) - classes defined inside other classes.
