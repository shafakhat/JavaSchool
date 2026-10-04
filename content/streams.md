---
title: Java Streams
nav: Streams
description: Process collections declaratively with map, filter, collect, groupingBy and more.
section: Core Java
order: 50
---

## Collections vs streams

- A **collection** is data (usually stored in memory).
- A **stream** is a *pipeline of computations* over data - lazy, declarative, one-pass.

You describe **what** you want (`filter adults, sort by name, take emails`) instead of writing loops with flags.

```text title=Stream pipeline
 source -> intermediate ops -> terminal op
 [list]    filter/map/sort     collect/forEach/count
           (lazy, do nothing)  (actually runs)
```

## Your first pipeline

```java title=FirstStream.java
import java.util.List;
import java.util.stream.Collectors;

public class FirstStream {
    public static void main(String[] args) {
        List<String> names = List.of("Asha", "Ben", "Chitra", "Dev", "Elena");

        List<String> result = names.stream()          // 1. source
            .filter(n -> n.length() > 3)              // 2. keep long names
            .map(String::toUpperCase)                 // 3. transform each
            .sorted()                                 // 4. order
            .collect(Collectors.toList());            // 5. terminal: gather result

        System.out.println(result);                   // [ASHA, CHITRA, ELENA]
        System.out.println(names);                    // original untouched
    }
}
```

Key properties:

- **Lazy** - nothing runs until a terminal operation.
- **No storage** - a stream is not a data structure.
- **Single use** - once consumed, a stream is dead; create a new one.
- **Non-mutating** - the source collection is never modified.

## Creating streams

```java title=Sources.java
import java.util.List;
import java.util.Map;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class Sources {
    public static void main(String[] args) {
        List<String> list = List.of("a", "b", "c");
        list.stream();                                  // from a collection
        Stream.of(1, 2, 3);                             // from values
        Stream.of(new String[]{"x", "y"});              // from an array
        "text".chars();                                 // int stream of char codes
        IntStream.rangeClosed(1, 5);                    // 1..5
        Map<String, Integer> m = Map.of("k", 1);
        m.entrySet().stream();                          // from map entries
    }
}
```

## The operators you need day to day

### Intermediate (return a new stream, lazy)

| Operator | Does |
|---|---|
| `filter(pred)` | keep elements matching a condition |
| `map(fn)` | transform each element (1 -> 1) |
| `flatMap(fn)` | transform then flatten (1 -> many) |
| `distinct()` | remove duplicates |
| `sorted()` / `sorted(cmp)` | order |
| `limit(n)` / `skip(n)` | cut the stream |
| `peek(fn)` | observe without changing (debugging) |
| `boxed()` | int stream -> Stream\<Integer\> |

### Terminal (consume the stream)

| Operator | Returns |
|---|---|
| `forEach(fn)` | void |
| `collect(...)` | anything (list, map, string, joining...) |
| `count()` | long |
| `reduce(identity, op)` | single value |
| `anyMatch` / `allMatch` / `noneMatch` | boolean |
| `findFirst` / `findAny` | Optional |
| `min` / `max` | Optional |
| `toArray()` | Object[] |

## Practical recipes

```java title=Recipes.java
import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Recipes {
    record Person(String name, int age, String city) {}

    public static void main(String[] args) {
        List<Person> people = List.of(
            new Person("Asha", 34, "Hyderabad"),
            new Person("Ben", 22, "Pune"),
            new Person("Chitra", 45, "Hyderabad"),
            new Person("Dev", 29, "Delhi"),
            new Person("Esha", 29, "Pune")
        );

        // 1. filter + collect
        List<String> over30 = people.stream()
            .filter(p -> p.age() > 30)
            .map(Person::name)
            .collect(Collectors.toList());
        System.out.println(over30);                     // [Asha, Chitra]

        // 2. anyMatch - exists?
        boolean anyPune = people.stream().anyMatch(p -> p.city().equals("Pune"));
        System.out.println("any from Pune? " + anyPune);

        // 3. grouping
        Map<String, List<Person>> byCity = people.stream()
            .collect(Collectors.groupingBy(Person::city));
        System.out.println(byCity.keySet());

        // 4. counting per group
        Map<String, Long> countPerCity = people.stream()
            .collect(Collectors.groupingBy(Person::city, Collectors.counting()));
        System.out.println(countPerCity);               // {Hyderabad=2, Pune=2, Delhi=1}

        // 5. joining into one string
        String all = people.stream()
            .map(Person::name)
            .collect(Collectors.joining(", ", "[", "]"));
        System.out.println(all);                        // [Asha, Ben, Chitra, Dev, Esha]

        // 6. sum / average
        double avgAge = people.stream()
            .mapToInt(Person::age)
            .average()
            .orElse(0);
        System.out.printf("avg age = %.1f%n", avgAge);

        // 7. toMap
        Map<String, Integer> ages = people.stream()
            .collect(Collectors.toMap(Person::name, Person::age));
        System.out.println(ages.get("Ben"));

        // 8. reduce - product of 1..5
        int product = IntStream.rangeClosed(1, 5)
            .reduce(1, (a, b) -> a * b);
        System.out.println("1*2*3*4*5 = " + product);
    }
}
```

## flatMap - flattening nested data

```java title=FlatMap.java
import java.util.List;
import java.util.stream.Collectors;

public class FlatMap {
    record Order(String id, List<String> items) {}

    public static void main(String[] args) {
        List<Order> orders = List.of(
            new Order("o1", List.of("pen", "book")),
            new Order("o2", List.of("book", "stapler")),
            new Order("o3", List.of("tape"))
        );

        List<String> allItems = orders.stream()
            .flatMap(o -> o.items().stream())    // List<String> -> Stream<String>
            .distinct()
            .sorted()
            .collect(Collectors.toList());

        System.out.println(allItems);            // [book, pen, stapler, tape]
    }
}
```

Without `flatMap` you'd collect nested lists and write another loop.

## Optional in pipelines

```java title=Optionals.java
import java.util.List;
import java.util.Optional;

public class Optionals {
    public static void main(String[] args) {
        List<String> emails = List.of("a@x.com", "", "c@x.com");

        Optional<String> firstReal = emails.stream()
            .filter(e -> !e.isBlank())
            .findFirst();

        firstReal.ifPresent(e -> System.out.println("found " + e));
        System.out.println(firstReal.orElse("none@example.com"));

        int len = emails.stream()
            .filter(e -> !e.isBlank())
            .findFirst()
            .map(String::length)
            .orElse(0);
        System.out.println(len);
    }
}
```

Never `get()` an `Optional` without checking - use `ifPresent`, `orElse`, `orElseGet`, or `map`.

## Parallel streams - handle with care

```java title=Parallel.java
import java.util.stream.LongStream;

public class Parallel {
    public static void main(String[] args) {
        long sum = LongStream.rangeClosed(1, 1_000_000)
            .parallel()                 // split across common pool threads
            .sum();
        System.out.println(sum);

        // .sequential() switches back
    }
}
```

Use parallel only for **large, CPU-heavy, stateless** pipelines. For small lists or heavy I/O it's usually *slower*.

## Debug tip

Streams hide inside loops - when something's wrong, use `peek` temporarily:

```java title=Peek.java
import java.util.List;

public class Peek {
    public static void main(String[] args) {
        List<Integer> out = List.of(1, 2, 3, 4).stream()
            .peek(n -> System.out.println("before: " + n))
            .filter(n -> n % 2 == 0)
            .peek(n -> System.out.println("after : " + n))
            .toList();                      // Java 16+: toList() shortcut
        System.out.println(out);
    }
}
```

> **Remember:** Streams shine for *transforming data you already have*. For shared mutable state or side-effect-heavy logic, plain loops are clearer.

Next: [Generics](generics.html) - type-safe reusable code.
