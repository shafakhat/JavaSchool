---
title: Java Methods (Functions)
nav: Methods
description: Define methods with parameters and return values, plus overloading, recursion and scope rules.
section: Java Basics
order: 90
---

## Why methods?

A method is a **named block of code** that performs one job. Methods give you reuse, clarity, and testability.

```java title=FirstMethod.java
public class FirstMethod {
    // method definition
    static int add(int a, int b) {
        return a + b;
    }

    public static void main(String[] args) {
        int result = add(15, 27);     // method call
        System.out.println(result);   // 42
    }
}
```

Anatomy:

```text
static int add(int a, int b) { ... }
 |      |   |    |        |
 |      |   |    +--------+ parameters (inputs)
 |      |   +------------- method name
 |      +----------------- return type (void = no return)
 +------------------------ modifier (belongs to the class, not an object)
```

## Parameters and return values

```java title=Params.java
public class Params {
    static double areaOfCircle(double radius) {
        return Math.PI * radius * radius;
    }

    static void greet(String name) {      // void: no return value
        System.out.println("Hello, " + name + "!");
    }

    static boolean isEven(int n) {
        return n % 2 == 0;                // boolean return
    }

    public static void main(String[] args) {
        System.out.printf("area = %.2f%n", areaOfCircle(3));
        greet("Sara");
        System.out.println("17 even? " + isEven(17));
    }
}
```

Rules:

- Arguments must match parameter **order, count and types**.
- A method with a return type must `return` a value on **every** path.
- `void` methods may use bare `return;` to exit early.

## Call stack - what happens on a call

Each call pushes a **frame** onto the stack; returning pops it:

```text title=Call stack for main -> sum(2,3) -> double(5)
+------------------+
| main frame       |  <-- locals: x
+------------------+
| sum frame        |  <-- a=2, b=3
+------------------+
| double frame     |  <-- n=5   (top of stack)
+------------------+
```

```java title=StackDemo.java
public class StackDemo {
    static int square(int n) {
        System.out.println("  square(" + n + ")");
        return n * n;
    }

    static int sumOfSquares(int a, int b) {
        System.out.println(" sumOfSquares(" + a + ", " + b + ")");
        return square(a) + square(b);
    }

    public static void main(String[] args) {
        System.out.println(sumOfSquares(2, 3));
    }
}
```

```text title=Output
 sumOfSquares(2, 3)
  square(2)
  square(3)
13
```

If a method never returns, you get a **StackOverflowError** - the classic sign of runaway recursion.

## Value semantics

Java is **pass-by-value**: for primitives the value is copied; for objects the *reference* is copied (so the method can mutate the object, but reassigning the parameter doesn't affect the caller).

```java title=PassByValue.java
public class PassByValue {
    static void tryToChange(int n) {
        n = 999;                       // only the copy changes
    }

    static void appendBang(StringBuilder sb) {
        sb.append("!");                // mutates the shared object
    }

    static void reassign(StringBuilder sb) {
        sb = new StringBuilder("other");  // local reference only
    }

    public static void main(String[] args) {
        int x = 1;
        tryToChange(x);
        System.out.println(x);                 // 1

        StringBuilder name = new StringBuilder("hi");
        appendBang(name);
        System.out.println(name);              // hi!

        reassign(name);
        System.out.println(name);              // hi! - unchanged
    }
}
```

## Method overloading

Several methods may share a name if their **parameter lists differ**:

```java title=Overload.java
public class Overload {
    static int add(int a, int b) { return a + b; }
    static double add(double a, double b) { return a + b; }
    static int add(int a, int b, int c) { return a + b + c; }

    public static void main(String[] args) {
        System.out.println(add(2, 3));        // 5   -> int version
        System.out.println(add(2.5, 3.5));    // 6.0 -> double version
        System.out.println(add(1, 2, 3));     // 6   -> three-arg version
    }
}
```

The compiler picks the **most specific** matching overload. Return type alone can never distinguish overloads.

## Static vs instance methods

```java title=StaticMethod.java
public class StaticMethod {
    static int classCounter = 0;        // shared by the whole class

    static void bump() {                // callable without an object
        classCounter++;
    }

    void instanceMethod() { }           // needs: new StaticMethod().instanceMethod()

    public static void main(String[] args) {
        bump();
        bump();
        System.out.println(classCounter);   // 2
        // instanceMethod();                // ERROR: non-static
        StaticMethod obj = new StaticMethod();
        obj.instanceMethod();               // OK
    }
}
```

Use `static` for helpers that don't touch per-object state; instance methods when behavior depends on a particular object (the heart of [OOP](classes-objects.html)).

## Recursion

A method that calls itself needs a **base case**:

```java title=Recursion.java
public class Recursion {
    static long factorial(int n) {
        if (n <= 1) return 1;            // base case
        return n * factorial(n - 1);     // recursive case
    }

    static int fibonacci(int n) {
        if (n <= 1) return n;
        return fibonacci(n - 1) + fibonacci(n - 2);
    }

    public static void main(String[] args) {
        System.out.println(factorial(10));   // 3628800
        for (int i = 0; i < 8; i++) {
            System.out.print(fibonacci(i) + " ");  // 0 1 1 2 3 5 8 13
        }
        System.out.println();
    }
}
```

> **Warning:** Naive `fibonacci` recomputes the same values exponentially (it's fine for small n). For performance-critical code use iteration or memoization.

## Varargs - accepting any number of arguments

```java title=Varargs.java
public class Varargs {
    static int max(int... nums) {
        if (nums.length == 0) throw new IllegalArgumentException("need a value");
        int m = nums[0];
        for (int n : nums) {
            if (n > m) m = n;
        }
        return m;
    }

    public static void main(String[] args) {
        System.out.println(max(3, 9, 4));   // 9
        System.out.println(max(-1, -7));    // -1
    }
}
```

- The varargs parameter must be **last**.
- Only one per method.
- Callers can also pass an existing array.

Next: [Classes and Objects](classes-objects.html) - where Java really begins.
