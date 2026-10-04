---
title: Java Syntax
nav: Syntax
description: The rules of Java syntax: class structure, main method, statements, blocks and semicolons.
section: Java Basics
order: 10
---

## The shape of every Java program

Every runnable Java program is built from **classes**, and execution always begins in a method called `main`.

```java title=MyProgram.java
public class MyProgram {
    public static void main(String[] args) {
        System.out.println("This is Java syntax");
    }
}
```

Line by line:

| Part | Meaning |
|---|---|
| `public class MyProgram` | Declares a public class; file must be `MyProgram.java` |
| `{ ... }` | A **block** grouping the class body |
| `public static void main(String[] args)` | The entry point the JVM looks for |
| `System.out.println(...)` | Prints a line to the console |
| `;` | Ends a statement (every statement needs one) |

## Blocks and scope

Curly braces define **blocks**. Variables declared inside a block are visible only until the block ends.

```java title=Blocks.java
public class Blocks {
    public static void main(String[] args) {
        int a = 1;          // visible from here to the end of main
        if (a > 0) {
            int b = 2;      // visible only inside this if-block
            System.out.println(b);
        }
        // System.out.println(b);  // ERROR: b is not in scope here
    }
}
```

## Statements, semicolons and whitespace

- Every statement ends with a **semicolon** `;`.
- Line breaks generally don't matter - Java ignores extra whitespace and indentation.
- Statements are usually one per line (the compiler doesn't care, but humans do).

```java title=OneLiner.java
public class OneLiner { public static void main(String[] a) { int x = 1; int y = 2; System.out.println(x + y); } }
```

That compiles fine - but nobody writes like that. Style matters.

> **Warning:** Forgetting the semicolon is the #1 beginner compiler error. `int x = 5` must become `int x = 5;`.

## Case sensitivity

Java is **case sensitive**. `MyClass`, `myclass` and `MYCLASS` are three different names.

```java title=CaseSensitive.java
public class CaseSensitive {
    public static void main(String[] args) {
        int Value = 10;
        int value = 20;     // different variable - this is legal
        System.out.println(Value + value);  // prints 30
    }
}
```

The class name convention is **UpperCamelCase** (`OrderService`); methods and variables use **lowerCamelCase** (`calculateTotal`).

## Keywords and identifiers

Words like `class`, `static`, `int` are **reserved keywords** and cannot be used as names. Everything else you invent (class names, variables, methods) is an **identifier**.

```java title=Identifiers.java
public class Identifiers {
    static int ordersCount = 5;   // OK: identifiers
    // int class = 3;   // ERROR: 'class' is a keyword

    public static void main(String[] args) {
        int total = ordersCount * 2;   // total is an identifier
        System.out.println(total);     // prints 10
    }
}
```

Rules for identifiers:

1. Letters, digits, `_` and `$` only
2. Cannot start with a digit
3. Cannot be a keyword
4. Case sensitive

See the full list on the [keywords reference](keywords.html).

## Comments

Comments are ignored by the compiler:

```java title=CommentsDemo.java
public class CommentsDemo {
    // a single-line comment

    /* a comment
       spanning several lines */

    /** Javadoc comment describing the class for tools and teammates */
    public static void main(String[] args) {
        System.out.println("Comments are ignored"); // like this one
    }
}
```

More detail in [Comments](comments.html).

## Your turn

Type this yourself, compile it, then change the text:

```java title=FirstProgram.java
public class FirstProgram {
    public static void main(String[] args) {
        String name = "Java";
        System.out.println("I am learning " + name + "!");
    }
}
```

```text title=Output
I am learning Java!
```

Next: [Comments](comments.html) and then [Variables](variables.html).
