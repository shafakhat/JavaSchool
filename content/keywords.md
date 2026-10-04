---
title: Java Keywords Reference
nav: Keywords
description: Complete list of Java reserved keywords with one-line meanings and short examples.
section: Reference
order: 10
---

## All 50+ reserved words

Java keywords cannot be used as identifiers (names of classes, variables, methods). They are always lowercase (except literal constants `true`, `false`, `null` which are reserved too).

### Class and object

| Keyword | Meaning |
|---|---|
| `class` | declare a class |
| `interface` | declare an interface |
| `extends` | inherit from a superclass |
| `implements` | implement interface(s) |
| `new` | create a new object / array |
| `this` | current object reference |
| `super` | parent class reference |
| `record` | declare a record (Java 16+) |
| `sealed` / `permits` | restrict who can extend/implement (Java 17+) |

### Access and modifiers

| Keyword | Meaning |
|---|---|
| `public` | visible everywhere |
| `protected` | visible in package + subclasses |
| `private` | visible only inside the class |
| *(none)* | package-private (default) |
| `static` | belongs to the class, not instances |
| `final` | cannot be changed (variable/method/class) |
| `abstract` | no body / cannot be instantiated |
| `native` | implemented in platform-specific code |
| `synchronized` | thread-safe block/method |
| `volatile` | always read/write main memory |
| `transient` | skip during serialization |
| `strictfp` | strict floating point (legacy) |

### Data types

| Keyword | Meaning |
|---|---|
| `int` `long` `short` `byte` | integer primitives |
| `float` `double` | floating point primitives |
| `char` | single UTF-16 character |
| `boolean` | `true` / `false` |
| `void` | no return value |

### Control flow

| Keyword | Meaning |
|---|---|
| `if` `else` | conditional |
| `switch` `case` `default` | multi-way branch |
| `for` `while` `do` | loops |
| `break` | exit loop/switch |
| `continue` | skip to next iteration |
| `return` | exit method (optionally with value) |
| `try` `catch` `finally` | exception handling |
| `throw` | raise an exception |
| `throws` | declare possible exceptions |
| `instanceof` | type check (pattern matching in Java 16+) |

### Packages and imports

| Keyword | Meaning |
|---|---|
| `package` | namespace declaration |
| `import` | resolve a type name |

### Reserved but unused / special

| Keyword | Status |
|---|---|
| `const` | reserved, **not used** - `final` took its job |
| `goto` | reserved, **not used** - the famous no-op keyword |
| `var` | since Java 10: local variable type inference (not reserved as a type name) |
| `yield` | since Java 14: yield a value from a switch expression |
| `assert` | since Java 1.4: runtime assertions (`-ea` flag) |
| `enum` | enumerate a fixed set of constants |
| `true` `false` `null` | reserved literals |

## Mini examples

```java title=KeywordDemo.java
abstract class Shape {              // abstract: no direct instantiation
    abstract double area();         // no body here
}

enum Direction { NORTH, EAST, SOUTH, WEST }   // enum: fixed constants

public class KeywordDemo extends Shape {      // extends: inheritance
    private final int id = 1;                 // private + final
    static int shared = 0;                    // class-level

    @Override
    double area() {                           // implements parent contract
        return 0;
    }

    Direction dir = Direction.NORTH;

    void classify(Object o) {
        if (o instanceof String s) {          // instanceof + pattern
            System.out.println("string of length " + s.length());
        }
    }

    String grade(int n) {
        return switch (n / 10) {              // switch expression (Java 14+)
            case 10, 9 -> "A";
            case 8, 7 -> "B";
            default -> "C";
        };
    }

    public static void main(String[] args) throws Exception {
        assert shared == 0 : "must start at zero";
        new KeywordDemo().classify("hi");
        System.out.println(new KeywordDemo().grade(85));
    }
}
```

## Punctuation partners

Not keywords, but you'll use them constantly:

| Symbol | Role |
|---|---|
| `{ }` | blocks |
| `( )` | calls, conditions, parameter lists |
| `[ ]` | array access |
| `;` | statement terminator |
| `:` | labels, enhanced-for, switch cases, ternary |
| `->` | lambdas and switch rules |
| `::` | method references |
| `@` | annotation marker (`@Override`) |

## Quick quiz

```text title=Self-check
1. Can a variable be named `class`?            -> No (keyword)
2. Is `True` a keyword?                        -> No - keywords are lowercase; `true` is the literal
3. What does `goto` do in Java?                 -> Nothing - it's reserved and unused
4. Is `var` a keyword?                         -> Special: used for local type inference since Java 10
5. Which keyword stops a loop?                 -> break (continue skips one round instead)
```

See also: [String methods](string-methods.html) · [Useful Java classes](java-api.html) · [Quiz](quiz.html)
