---
title: Java Variables and Data Types
nav: Variables
description: Primitive types, reference types, literals, variable scope, casting and constants in Java.
section: Java Basics
order: 30
---

## What is a variable?

A variable is a **named storage slot** in memory. In Java you must declare a variable's *type* before using it - Java is **statically typed**.

```java title=Declare.java
public class Declare {
    public static void main(String[] args) {
        int age = 25;            // declare + assign
        String name = "Priya";   // String is a class (reference type)
        double price = 199.5;    // decimal number
        boolean active = true;   // true or false

        System.out.println(name + " is " + age);
        System.out.println(price + " active=" + active);
    }
}
```

## The 8 primitive types

| Type | Size | Range / values | Example |
|---|---|---|---|
| `byte` | 8-bit | -128 to 127 | `byte b = 100;` |
| `short` | 16-bit | -32,768 to 32,767 | `short s = 1000;` |
| `int` | 32-bit | about -2.1e9 to 2.1e9 | `int i = 100_000;` |
| `long` | 64-bit | huge | `long l = 100_000L;` |
| `float` | 32-bit | ~7 decimal digits | `float f = 3.14f;` |
| `double` | 64-bit | ~15 decimal digits | `double d = 3.14159;` |
| `char` | 16-bit | one UTF-16 character | `char c = 'A';` |
| `boolean` | 1 bit (conceptually) | `true` / `false` | `boolean ok = true;` |

```java title=Primitives.java
public class Primitives {
    public static void main(String[] args) {
        byte bites = -128;
        short small = 32000;
        int million = 1_000_000;
        long big = 9_000_000_000L;       // note the L suffix
        float ratio = 0.75f;             // note the f suffix
        double pi = 3.141592653589793;
        char letter = 'Z';
        boolean ready = true;

        System.out.println(bites + small + million);
        System.out.println(big + " " + ratio + " " + pi);
        System.out.println(letter + " ready=" + ready);
    }
}
```

> **Remember:** Integer literals are `int` by default and floating-point literals are `double` by default. That's why `float f = 3.14;` fails - you must write `3.14f`.

## Reference types

Everything that is not primitive is a **reference** - the variable holds an *address* of an object, not the object itself.

```java title=ReferenceTypes.java
public class ReferenceTypes {
    public static void main(String[] args) {
        String city = "Hyderabad";      // String object
        int[] nums = {1, 2, 3};        // array object
        java.util.Date now = new java.util.Date();  // Date object

        System.out.println(city.length() + " " + nums.length + " " + now);
    }
}
```

Key difference: two primitives with the same value are equal; two references with the same value point to the *same object*.

## Declaration, initialization, assignment

```java title=Lifecycle.java
public class Lifecycle {
    public static void main(String[] args) {
        int score;          // declaration (no value yet)
        score = 10;         // assignment (initialization)
        score = score + 5;  // re-assignment: now 15
        System.out.println(score);
    }
}
```

Using a local variable before initializing it is a **compile error** - Java enforces definite assignment.

## Scope and lifetime

A variable's **scope** is the region where its name is usable - from its declaration to the end of the enclosing block.

```java title=Scope.java
public class Scope {
    static int instanceLevel = 7;   // field: lives with the object

    public static void main(String[] args) {
        int outer = 1;              // scope: rest of main
        {
            int inner = 2;          // scope: this inner block only
            System.out.println(outer + inner);
        }
        // System.out.println(inner);  // ERROR: out of scope
        System.out.println(instanceLevel);
    }
}
```

## Type casting

**Widening** (implicit, safe) happens automatically for smaller-to-larger:

```java title=Widening.java
public class Widening {
    public static void main(String[] args) {
        int i = 42;
        double d = i;          // int -> double, automatic
        System.out.println(d); // 42.0
    }
}
```

**Narrowing** (explicit, may lose data) needs a cast:

```java title=Narrowing.java
public class Narrowing {
    public static void main(String[] args) {
        double pi = 3.99;
        int truncated = (int) pi;    // 3 - fractional part is cut off
        System.out.println(truncated);

        byte tooBig = (byte) 200;    // wraps around: -56
        System.out.println(tooBig);
    }
}
```

Also beware **integer division**:

```java title=Divide.java
public class Divide {
    public static void main(String[] args) {
        System.out.println(7 / 2);        // 3 (integer division!)
        System.out.println(7.0 / 2);      // 3.5
        System.out.println(7 / 2.0);      // 3.5
    }
}
```

## Literals and sugar

```java title=Literals.java
public class Literals {
    public static void main(String[] args) {
        int readable = 1_000_000;     // underscores for readability (Java 7+)
        int hex = 0xFF;               // 255
        int octal = 017;              // 15
        int binary = 0b1010;          // 10
        char hash = '\u0023';         // '#' via unicode escape
        System.out.println(readable + " " + hex + " " + octal + " " + binary + " " + hash);
    }
}
```

## Constants with `final`

A `final` variable can be assigned exactly once. Use it for values that must never change.

```java title=Constants.java
public class Constants {
    public static final double TAX_RATE = 0.18;   // convention: UPPER_SNAKE_CASE

    public static void main(String[] args) {
        final int seatCount = 40;
        // seatCount = 50;   // ERROR: cannot assign a final variable twice
        System.out.println(1000 * (1 + TAX_RATE) + " seats=" + seatCount);
    }
}
```

> **Tip:** Anything reused across the codebase - rates, limits, SQL queries - should be a `static final` constant, never a magic number sprinkled around.

Next: [Operators](operators.html) to work with these values.
