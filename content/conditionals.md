---
title: Java Conditions (if, else, switch)
nav: Conditions
description: if, else if, nested conditions, switch expressions and the ternary operator in Java.
section: Java Basics
order: 60
---

## The `if - else` family

Conditions control which code runs:

```java title=IfElse.java
public class IfElse {
    public static void main(String[] args) {
        int marks = 78;

        if (marks >= 90) {
            System.out.println("Grade A");
        } else if (marks >= 75) {
            System.out.println("Grade B");
        } else if (marks >= 60) {
            System.out.println("Grade C");
        } else {
            System.out.println("Grade D");
        }
    }
}
```

```text title=Output
Grade C
```

Rules:

1. The condition must be a `boolean` (unlike C/C++, numbers are not allowed here).
2. `else if` chains are evaluated top to bottom - first match wins.
3. Braces `{}` are optional for single statements, but **always use them** - they prevent the famous dangling-else bug.

## Truthy myths - Java has none

```java title=Strict.java
public class Strict {
    public static void main(String[] args) {
        int x = 5;
        // if (x) { }             // ERROR: int is not boolean
        if (x != 0) { }           // OK - explicit comparison
        boolean b = (x == 5);
        if (b) {
            System.out.println("only booleans in conditions");
        }
    }
}
```

## Nested conditions

```java title=Nested.java
public class Nested {
    public static void main(String[] args) {
        boolean loggedIn = true;
        boolean isAdmin = false;

        if (loggedIn) {
            if (isAdmin) {
                System.out.println("Admin dashboard");
            } else {
                System.out.println("User dashboard");
            }
        } else {
            System.out.println("Please log in");
        }
    }
}
```

Prefer **guard clauses** (return early) over deep nesting:

```java title=Guard.java
public class Guard {
    static void process(int amount) {
        if (amount <= 0) { System.out.println("invalid"); return; }
        if (amount > 10_000) { System.out.println("too large"); return; }
        System.out.println("processing " + amount);   // main path stays flat
    }

    public static void main(String[] args) {
        process(250);
        process(-1);
    }
}
```

## Combining conditions

```java title=Combine.java
public class Combine {
    public static void main(String[] args) {
        int age = 25;
        boolean hasId = true;

        if (age >= 18 && hasId) {
            System.out.println("Entry allowed");
        }
        if (age < 13 || age > 60) {
            System.out.println("Concession fare");
        }
        if (!(age < 0)) {
            System.out.println("Age looks valid");
        }
    }
}
```

`&&` and `||` **short-circuit**: the right side is only evaluated when needed (see [Operators](operators.html)).

## `switch` statements

`switch` is cleaner than long `else if` chains when comparing **one value against many constants**:

```java title=Switch.java
public class Switch {
    public static void main(String[] args) {
        String day = "Tue";

        switch (day) {
            case "Mon":
                System.out.println("Start of the work week");
                break;
            case "Tue":
            case "Wed":
            case "Thu":
                System.out.println("Midweek");
                break;
            case "Fri":
                System.out.println("Almost there");
                break;
            default:
                System.out.println("Weekend!");
        }
    }
}
```

> **Warning:** Without `break`, execution **falls through** to the next case. The stacked `Tue/Wed/Thu` cases above rely on that intentionally.

### Modern switch expressions (Java 14+)

```java title=SwitchExpression.java
public class SwitchExpression {
    public static void main(String[] args) {
        int dayNum = 3;

        String type = switch (dayNum) {
            case 6, 7 -> "weekend";
            case 1, 2, 3, 4, 5 -> "weekday";
            default -> "invalid";
        };
        System.out.println(type);

        // arrow form never falls through, so break is unnecessary
        switch (dayNum) {
            case 1 -> System.out.println("Monday");
            case 5 -> System.out.println("Friday");
            default -> System.out.println("Other");
        }
    }
}
```

Bonus: the arrow form lets you use patterns and multiple labels (`case 6, 7 ->`) and can `yield` a value.

## Ternary in conditions

```java title=Ternary.java
public class Ternary {
    public static void main(String[] args) {
        int age = 17;
        String verdict = (age >= 18) ? "eligible" : "too young";
        System.out.println(verdict);

        // nested ternaries are legal but hard to read - use sparingly
        int score = 85;
        String grade = score >= 90 ? "A" : score >= 80 ? "B" : "C";
        System.out.println(grade);
    }
}
```

## Common beginner pitfalls

```java title=Pitfalls.java
public class Pitfalls {
    public static void main(String[] args) {
        // 1) assignment (=) instead of comparison (==)
        int x = 5;
        // if (x = 5) { }     // ERROR - won't compile in Java (good!)

        // 2) comparing boxed Integers with ==
        Integer a = 127, b = 127;
        Integer c = 128, d = 128;
        System.out.println(a == b);   // true (cached)
        System.out.println(c == d);   // false! - always use .equals()

        // 3) float equality - use a tolerance instead
        double v = 0.1 + 0.2;
        System.out.println(v == 0.3);                       // false
        System.out.println(Math.abs(v - 0.3) < 1e-9);       // true
    }
}
```

Next: [Loops](loops.html) - repeating work the smart way.
