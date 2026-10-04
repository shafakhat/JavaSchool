---
title: Java Loops
nav: Loops
description: for, while, do-while, enhanced for loops, break and continue in Java.
section: Java Basics
order: 70
---

## The `for` loop

Use `for` when you know **how many times** to repeat:

```java title=ForLoop.java
public class ForLoop {
    public static void main(String[] args) {
        for (int i = 1; i <= 5; i++) {
            System.out.println("count " + i);
        }
    }
}
```

```text title=Output
count 1
count 2
count 3
count 4
count 5
```

Structure: `for (initialization; condition; update)`

1. **initialization** runs once (`int i = 1`)
2. **condition** is checked before *each* run - loop stops when false
3. **update** runs after each iteration (`i++`)

```java title=ForParts.java
public class ForParts {
    public static void main(String[] args) {
        // counting down
        for (int i = 3; i >= 1; i--) {
            System.out.print(i + " ");
        }
        System.out.println("liftoff!");

        // step of 2
        for (int i = 0; i <= 10; i += 2) {
            System.out.print(i + " ");   // 0 2 4 6 8 10
        }
        System.out.println();

        // several variables in one loop
        for (int i = 0, j = 10; i < j; i++, j--) {
            System.out.println(i + " / " + j);
        }
    }
}
```

## The `while` loop

Use `while` when the number of repeats **depends on a condition** you can't predict:

```java title=WhileLoop.java
import java.util.Random;

public class WhileLoop {
    public static void main(String[] args) {
        Random rand = new Random();
        int attempts = 0;
        int roll;

        do {
            roll = rand.nextInt(6) + 1;   // 1..6
            attempts++;
            System.out.println("rolled " + roll);
        } while (roll != 6);              // wait, this is do-while - see below

        System.out.println("got a 6 after " + attempts + " tries");
    }
}
```

A pure `while` (condition checked **first**):

```java title=WhileFirst.java
public class WhileFirst {
    public static void main(String[] args) {
        int n = 1024;
        int steps = 0;
        while (n > 1) {
            n /= 2;
            steps++;
        }
        System.out.println("halvings: " + steps);   // 10

        int none = 5;
        while (none > 10) {           // never runs - condition false up front
            System.out.println("unreachable");
        }
    }
}
```

## The `do-while` loop

The body runs **at least once**, then the condition is checked:

```java title=DoWhile.java
import java.util.Scanner;

public class DoWhile {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int number;
        do {
            System.out.print("Enter a positive number: ");
            number = sc.nextInt();
        } while (number <= 0);
        System.out.println("You entered " + number);
        sc.close();
    }
}
```

| Loop | Check happens | Use when |
|---|---|---|
| `for` | before each iteration | fixed count / range |
| `while` | before each iteration | condition-driven, may run 0 times |
| `do-while` | after each iteration | must run at least once (menus, input prompts) |

## Enhanced `for` (for-each)

Iterating over arrays and collections is cleaner with the for-each form:

```java title=ForEach.java
public class ForEach {
    public static void main(String[] args) {
        int[] nums = {3, 6, 9, 12};

        for (int n : nums) {
            System.out.print(n + " ");
        }
        System.out.println();

        String[] fruits = {"mango", "kiwi", "fig"};
        for (String f : fruits) {
            System.out.println(f.toUpperCase());
        }
    }
}
```

You can't easily modify the collection while iterating, and you don't get the index - use a classic `for` when you need either.

## `break` and `continue`

```java title=BreakContinue.java
public class BreakContinue {
    public static void main(String[] args) {
        for (int i = 1; i <= 10; i++) {
            if (i == 3) continue;      // skip 3
            if (i == 7) break;         // stop entirely at 7
            System.out.print(i + " ");
        }
        System.out.println();          // 1 2 4 5 6
    }
}
```

`break` also exits a `switch` (in the old statement form). A `break` inside nested loops only leaves the **innermost** loop - use a flag or extract a method instead:

```java title=Find.java
public class Find {
    public static void main(String[] args) {
        int[][] grid = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };
        int target = 5;
        boolean found = false;

        outer:
        for (int[] row : grid) {
            for (int cell : row) {
                if (cell == target) {
                    found = true;
                    break outer;      // labeled break jumps out of both loops
                }
            }
        }
        System.out.println("found=" + found);
    }
}
```

## Infinite loops

An infinite loop is sometimes intentional (event servers, GUIs):

```java title=Forever.java
public class Forever {
    public static void main(String[] args) {
        int i = 0;
        while (true) {                 // runs until break
            i++;
            if (i >= 3) {
                System.out.println("done after " + i + " rounds");
                break;
            }
        }
        // for (;;) { }                // same idea, classic form
    }
}
```

> **Warning:** A `while` loop with a condition you never update (`while (x > 0)` without changing `x`) is a hang, not a loop. Watch for it in interviews.

## Loops with common patterns

```java title=Patterns.java
public class Patterns {
    public static void main(String[] args) {
        // multiplication table
        for (int i = 1; i <= 5; i++) {
            StringBuilder row = new StringBuilder();
            for (int j = 1; j <= 5; j++) {
                row.append(String.format("%4d", i * j));
            }
            System.out.println(row);
        }

        // sum of digits
        int n = 2026, sum = 0;
        for (int t = n; t > 0; t /= 10) {
            sum += t % 10;
        }
        System.out.println("digit sum of " + n + " = " + sum);
    }
}
```

Next: [Arrays](arrays.html) - storing many values of the same type.
