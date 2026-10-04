---
title: Modern Java Features
nav: Modern Java
description: Records, sealed classes, switch expressions, pattern matching, text blocks and other modern Java features.
section: Advanced Java
order: 60
---

## Why modern Java matters

Since Java 9 the language has been releasing on a 6-month cadence. If you learned Java "at 8", these are the features you'll meet in today's codebases (17/21 are the current LTS baselines).

## `var` - local variable type inference (Java 10)

```java title=VarDemo.java
import java.util.ArrayList;
import java.util.Map;

public class VarDemo {
    public static void main(String[] args) {
        var numbers = new ArrayList<Integer>();      // type inferred: ArrayList<Integer>
        var lookup = Map.of("a", 1, "b", 2);         // Map<String, Integer>
        var first = numbers.size() + lookup.get("a"); // int

        System.out.println(numbers.getClass().getSimpleName() + " " + first);
        // var x = null;    // useless - no type to infer (error)
    }
}
```

`var` is only for **local variables with an initializer** - fields, parameters and returns stay explicit.

## Text blocks (Java 15)

```java title=TextBlocks.java
public class TextBlocks {
    public static void main(String[] args) {
        String json = """
                {
                    "name": "Ada",
                    "age": 36
                }
                """;

        String sql = """
                SELECT id, name
                FROM users
                WHERE active = true
                """;

        System.out.println(json);
        System.out.println(sql);
    }
}
```

Incidental indentation is stripped automatically; no more `\n` soup.

## Switch expressions and patterns (Java 14/17/21)

```java title=SwitchDemo.java
import java.util.Locale;

public class SwitchDemo {
    enum Size { SMALL, MEDIUM, LARGE }

    public static void main(String[] args) {
        // arrow form: no fall-through, can yield a value
        int numLetters = switch ("java".toLowerCase(Locale.ROOT)) {
            case "one" -> 3;
            case "two" -> 3;
            case "three" -> 5;
            default -> 0;
        };
        System.out.println(numLetters);

        Size s = Size.MEDIUM;
        String desc = switch (s) {                  // statement form with yield
            case SMALL -> "small";
            case MEDIUM -> {
                System.out.println("medium chosen");
                yield "medium";
            }
            case LARGE -> "large";
        };
        System.out.println(desc);
    }
}
```

## Pattern matching

### `instanceof` with a binding variable (Java 16)

```java title=PatternInstance.java
public class PatternInstance {
    static String describe(Object o) {
        if (o instanceof String s) {         // check AND cast in one
            return "string of length " + s.length();
        }
        if (o instanceof Integer i && i > 100) {
            return "big int " + i;
        }
        return o == null ? "null" : o.toString();
    }

    public static void main(String[] args) {
        System.out.println(describe("hello"));
        System.out.println(describe(250));
        System.out.println(describe(42));
    }
}
```

No more unchecked casts + `ClassCastException` waiting to happen.

### Pattern matching for `switch` (Java 21)

```java title=SwitchPatterns.java
public class SwitchPatterns {
    static String type(Object o) {
        return switch (o) {
            case null -> "null";
            case String s -> "String(" + s.length() + ")";
            case Integer i when i < 0 -> "negative int";
            case Integer i -> "int " + i;
            case int[] arr -> "int[] of " + arr.length;
            default -> "something else";
        };
    }

    public static void main(String[] args) {
        System.out.println(type("hi"));
        System.out.println(type(-5));
        System.out.println(type(7));
        System.out.println(type(new int[]{1, 2}));
        System.out.println(type(3.14));
    }
}
```

## Records (Java 16)

```java title=Records.java
import java.util.List;

public class Records {
    // compact, immutable data carrier - equals/hashCode/toString included
    record Point(int x, int y) { }
    record User(String name, List<String> tags) {
        User {                              // compact constructor: validation hook
            if (name == null || name.isBlank()) throw new IllegalArgumentException("name");
            tags = List.copyOf(tags);       // defensive copy -> truly immutable
        }
    }

    public static void main(String[] args) {
        Point p = new Point(3, 4);
        Point q = new Point(3, 4);
        System.out.println(p.equals(q));    // true - value equality
        System.out.println(p);              // Point[x=3, y=4]

        User u = new User("Ada", List.of("math", "code"));
        System.out.println(u.name() + " " + u.tags());
    }
}
```

Records are `final`, can't extend anything, and expose accessors named `x()` (not `getX()`).

## Sealed types (Java 17)

```java title=SealedTypes.java
public class SealedTypes {
    sealed interface Shape permits Circle, Square, Triangle { }
    record Circle(double r) implements Shape { }
    record Square(double side) implements Shape { }
    record Triangle(double base, double h) implements Shape { }

    static double area(Shape s) {
        return switch (s) {                     // compiler knows all subtypes
            case Circle c -> Math.PI * c.r() * c.r();
            case Square sq -> sq.side() * sq.side();
            case Triangle t -> 0.5 * t.base() * t.h();
        };
    }

    public static void main(String[] args) {
        Shape[] shapes = { new Circle(1), new Square(2), new Triangle(2, 3) };
        for (Shape s : shapes) System.out.println(area(s));
    }
}
```

`sealed` + exhaustive `switch` gives you safe, compiler-checked hierarchies - a lightweight alternative to enums when subtypes carry data.

## Other features worth knowing

| Feature | Since | Use |
|---|---|---|
| `Optional` returns | 8 | explicit "maybe" values |
| Streams / lambdas / method refs | 8 | declarative collection processing |
| `List.of` / `Map.of` | 9 | immutable collection literals |
| `String.lines()`, `strip()`, `repeat()` | 11 | nicer string handling |
| `HttpClient` | 11 | modern HTTP (see [Networking](networking.html)) |
| `Stream.toList()` | 16 | `collect(toList())` shorthand |
| Enhanced `random` API | 17 | `RandomGenerator` |
| Virtual threads (preview → final 21) | 21 | huge thread counts, cheap blocking |

## Upgrade checklist for teams

1. Standardize on an **LTS** (17 or 21).
2. Turn on newer **lint** checks in the build.
3. Replace boilerplate: DTOs → `records`, `instanceof` chains → patterns, string concat → text blocks/`formatted`.
4. Keep dependencies current - frameworks assume modern bytecode.

Next: [Design Patterns](design-patterns.html) · Test yourself: [OCJP Practice Test](ocjp-practice.html)
