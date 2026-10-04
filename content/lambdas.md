---
title: Java Lambda Expressions
nav: Lambdas
description: Write anonymous functions with lambdas, method references and the core functional interfaces.
section: Core Java
order: 40
---

## Behavior as a value

A **lambda** is a compact anonymous function. It lets you pass *code* (comparisons, filters, callbacks) the same way you pass data.

```text title=Before and after Java 8
before:  new Runnable() { public void run() { System.out.println("hi"); } }
after:   () -> System.out.println("hi")
```

## Syntax

```text title=lambda anatomy
 (Type a, Type b) -> expression          // expression body (result returned)
 (a, b) -> { statements; return r; }     // block body (explicit return)
 () -> doSomething()                     // no parameters
 a -> a * 2                              // one parameter: no parens needed
```

Parameter types are almost always inferrable - add them only when the compiler needs them.

## Lambda vs anonymous class

```java title=Compare.java
import java.util.function.Consumer;

public class Compare {
    public static void main(String[] args) {
        // anonymous class
        Consumer<String> a = new Consumer<String>() {
            @Override
            public void accept(String s) {
                System.out.println("anon: " + s);
            }
        };

        // lambda - same behavior, far less noise
        Consumer<String> b = s -> System.out.println("lambda: " + s);

        a.accept("x");
        b.accept("x");
    }
}
```

Two semantic differences worth knowing:

- In a lambda, `this` refers to the **enclosing** instance (an anonymous class gets its own).
- A lambda can only implement a **functional interface** (an interface with exactly one abstract method).

## The functional interfaces you'll actually use

| Interface | Method | Signature intuition |
|---|---|---|
| `Predicate<T>` | `boolean test(T)` | a condition |
| `Function<T,R>` | `R apply(T)` | a transformation |
| `Consumer<T>` | `void accept(T)` | a side effect |
| `Supplier<T>` | `T get()` | a factory |
| `BiFunction<T,U,R>` | `R apply(T,U)` | two-input transform |
| `Runnable` | `void run()` | no args, no return |
| `Comparator<T>` | `int compare(T,T)` | ordering |

```java title=CoreInterfaces.java
import java.util.function.*;
import java.util.List;

public class CoreInterfaces {
    public static void main(String[] args) {
        Predicate<Integer> isEven = n -> n % 2 == 0;
        Function<String, Integer> len = String::length;
        Consumer<String> shout = s -> System.out.println(s.toUpperCase() + "!");
        Supplier<List<String>> factory = () -> List.of("fresh", "list");

        System.out.println(isEven.test(4));       // true
        System.out.println(len.apply("java"));    // 4
        shout.accept("quiet");                    // QUIET!
        System.out.println(factory.get());        // [fresh, list]
    }
}
```

## Lambdas with JDK collections

```java title=WithCollections.java
import java.util.*;

public class WithCollections {
    public static void main(String[] args) {
        List<String> names = new ArrayList<>(List.of("Nina", "Omar", "Priya", "Bo"));

        // sort with an explicit rule
        names.sort((a, b) -> a.length() - b.length());
        System.out.println(names);              // [Bo, Nina, Omar, Priya]

        // sort by length, then alphabetically (composed comparators)
        names.sort(Comparator.comparingInt(String::length)
                             .thenComparing(Comparator.naturalOrder()));
        System.out.println(names);

        // filter / transform with streams (next page)
        names.stream()
             .filter(n -> n.startsWith("P"))
             .map(String::toUpperCase)
             .forEach(System.out::println);     // PRIYA
    }
}
```

## Method references

`ClassName::method` is sugar for a lambda that calls that method:

| Lambda | Method reference |
|---|---|
| `s -> s.length()` | `String::length` |
| `s -> System.out.println(s)` | `System.out::println` |
| `() -> new ArrayList<>()` | `ArrayList::new` |
| `n -> Integer.parseInt(n)` | `Integer::parseInt` |
| `(a, b) -> a.compareTo(b)` | `String::compareTo` |

```java title=MethodRefs.java
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class MethodRefs {
    public static void main(String[] args) {
        List<Integer> nums = List.of(3, 1, 4, 1, 5);

        // instance method used as a mapper
        System.out.println(nums.stream()
                               .map(String::valueOf)
                               .collect(Collectors.joining(",")));   // 3,1,4,1,5

        // constructor reference: builds a new ArrayList of the same values
        List<Integer> copy = nums.stream()
                                 .collect(Collectors.toCollection(ArrayList::new));
        System.out.println(copy);

        // bound instance method reference: the receiver is pre-bound
        String prefix = "id-";
        java.util.function.Function<String, String> label = prefix::concat;
        System.out.println(label.apply("7"));    // id-7
    }
}
```

If a lambda is *only* a call to one method, replace it with `::` - it reads better.

## Closures - capturing variables

Lambdas may read **effectively final** local variables (assigned once, explicitly or implicitly):

```java title=Closure.java
public class Closure {
    public static void main(String[] args) {
        String prefix = "log: ";            // effectively final - captured by value
        int factor = 10;                    // effectively final

        Runnable r = () -> System.out.println(prefix + (7 * factor));

        // factor = 20;                     // ERROR: would break the capture
        r.run();
    }
}
```

For counters shared with a lambda, use an `AtomicInteger`, a one-element array, or an instance field.

## When a lambda throws

Checked exceptions don't flow through functional interfaces silently - wrap them:

```java title=LambdaThrows.java
import java.util.function.Consumer;

public class LambdaThrows {
    public static void main(String[] args) {
        Consumer<String> risky = s -> {
            try {
                Integer.parseInt(s);
            } catch (NumberFormatException e) {
                throw new IllegalArgumentException("bad input: " + s, e);
            }
        };

        try {
            risky.accept("12x");
        } catch (IllegalArgumentException e) {
            System.out.println(e.getMessage());
            System.out.println("cause: " + e.getCause());
        }
    }
}
```

## Style tips

- **One line?** Keep it on one line. If it grows past ~3 lines, extract a named method and use `ClassName::thatMethod`.
- **Name the intent.** `(user) -> user.isActive()` reads great as `.filter(User::isActive)` when possible.
- Don't fight type inference with redundant type declarations.

Next: [Streams](streams.html) - process collections declaratively.
