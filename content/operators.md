---
title: Java Operators
nav: Operators
description: Arithmetic, assignment, comparison, logical, bitwise, ternary and instanceof operators in Java.
section: Java Basics
order: 40
---

## Overview

Operators are the symbols that perform computations. Java groups them into families:

| Category | Operators |
|---|---|
| Arithmetic | `+ - * / %` |
| Assignment | `= += -= *= /= %= ` |
| Comparison | `== != < > <= >=` |
| Logical | `&& \|\| !` |
| Bitwise | `& \| ^ ~ << >> >>>` |
| Conditional | `? :` (ternary) |
| Misc | `instanceof`, casts, `++ --` |

## Arithmetic operators

```java title=Arithmetic.java
public class Arithmetic {
    public static void main(String[] args) {
        int a = 17, b = 5;
        System.out.println(a + b);   // 22
        System.out.println(a - b);   // 12
        System.out.println(a * b);   // 85
        System.out.println(a / b);   // 3   - integer division truncates
        System.out.println(a % b);   // 2   - remainder (modulo)
        System.out.println(9.0 / 2); // 4.5 - if either side is double, result is double
    }
}
```

The **modulo** operator is handy for even/odd checks and wrapping indexes:

```java title=Modulo.java
public class Modulo {
    public static void main(String[] args) {
        for (int i = 0; i < 6; i++) {
            System.out.println(i + " is " + (i % 2 == 0 ? "even" : "odd"));
        }
    }
}
```

## Increment and decrement

```java title=Increment.java
public class Increment {
    public static void main(String[] args) {
        int n = 5;
        System.out.println(n++);   // 5 - post-increment: value used first
        System.out.println(n);     // 6
        System.out.println(++n);   // 7 - pre-increment: incremented first
        System.out.println(n--);   // 7
        System.out.println(n);     // 6
    }
}
```

> **Warning:** `int y = x++;` and `int y = ++x;` differ. And combining several `++`/`--` on the same variable in *one* expression is a readability trap - avoid it.

## Assignment operators

Compound assignments bundle arithmetic and assignment:

```java title=Compound.java
public class Compound {
    public static void main(String[] args) {
        int x = 10;
        x += 5;    // x = x + 5  -> 15
        x -= 3;    // 12
        x *= 2;    // 24
        x /= 4;    // 6
        x %= 4;    // 2
        System.out.println(x);
    }
}
```

## Comparison operators

Comparison always yields a `boolean`:

```java title=Compare.java
public class Compare {
    public static void main(String[] args) {
        int a = 10, b = 20;
        System.out.println(a == b);   // false
        System.out.println(a != b);   // true
        System.out.println(a < b);    // true
        System.out.println(a >= 10);  // true

        String s1 = "hello", s2 = "hello";
        System.out.println(s1 == s2);       // may be false! (different objects)
        System.out.println(s1.equals(s2));  // true - always use this for text
    }
}
```

> **Warning:** Never use `==` to compare `String` content - use `.equals()`. `==` compares references (or primitive values).

## Logical operators

```java title=Logical.java
public class Logical {
    public static void main(String[] args) {
        boolean adult = true;
        boolean hasTicket = false;

        System.out.println(adult && hasTicket);  // false - AND
        System.out.println(adult || hasTicket);  // true  - OR
        System.out.println(!adult);              // false - NOT
    }
}
```

**Short-circuiting:** `&&` stops at the first `false`, `||` stops at the first `true`. That makes guards safe:

```java title=ShortCircuit.java
public class ShortCircuit {
    public static void main(String[] args) {
        String s = null;
        // s.length() would throw NPE, but it is never evaluated:
        if (s != null && s.length() > 0) {
            System.out.println("non-empty");
        } else {
            System.out.println("safe - no NullPointerException");
        }
    }
}
```

## Ternary operator

`condition ? valueIfTrue : valueIfFalse` - a compact `if/else` for expressions:

```java title=Ternary.java
public class Ternary {
    public static void main(String[] args) {
        int age = 20;
        String status = age >= 18 ? "adult" : "minor";
        System.out.println(status);

        int score = 72;
        String grade = score >= 60 ? "pass" : "fail";
        System.out.println(grade);
    }
}
```

## Bitwise and shift operators

Used mostly with flags, hashes and low-level code:

```java title=Bits.java
public class Bits {
    public static void main(String[] args) {
        int a = 0b1100;   // 12
        int b = 0b1010;   // 10
        System.out.println(a & b);    // 8   (1000)
        System.out.println(a | b);    // 14  (1110)
        System.out.println(a ^ b);    // 6   (0110)
        System.out.println(1 << 4);   // 16  (shift left  = x16)
        System.out.println(16 >> 2);  // 4   (shift right = /4)
        System.out.println(-8 >>> 1); // big positive number (unsigned shift)
    }
}
```

## Operator precedence (most useful rows)

| Priority | Operators |
|---|---|
| 1 (highest) | postfix `++ --`, method calls `()` |
| 2 | unary `+ - ! ++ -- (cast)` |
| 3 | `* / %` |
| 4 | `+ -` |
| 5 | `<< >> >>>` |
| 6 | `< <= > >= instanceof` |
| 7 | `== !=` |
| 8 | `&` `^` `\|` |
| 9 | `&&` `\|\|` |
| 10 (lowest) | `?:` and assignment `= += ...` |

When unsure, add parentheses - clarity beats cleverness:

```java title=Precedence.java
public class Precedence {
    public static void main(String[] args) {
        System.out.println(2 + 3 * 4);    // 14  (* binds tighter)
        System.out.println((2 + 3) * 4);  // 20  (forced order)
        System.out.println(10 - 3 - 2);   // 5   (left to right)
    }
}
```

Next: [Strings](strings.html) - Java's most used type.
