---
title: Enumeration, Enums and Iterators
nav: Enumerations
description: java.lang.enum types and the legacy java.util.Enumeration - how to model fixed sets, and Enumeration vs Iterator in collections.
section: Collections
order: 40
---

## Two things called "enumeration"

Java uses the word twice - they are unrelated:

| Type | Package | What it is |
|---|---|---|
| `enum` types | `java.lang` (keyword) | closed set of constants with behavior (since Java 5) |
| `Enumeration` | `java.util` | **legacy iterator** for Vector/Hashtable (pre-1.2) |
| `EnumSet`/`EnumMap` | `java.util` | high-performance specializations for enum keys/values |

## Modern `enum` - the right tool

```java title=Severity.java
import java.util.EnumMap;
import java.util.EnumSet;

public class Severity {
    public enum Level {
        LOW("info", 1),
        MEDIUM("warn", 2),
        HIGH("error", 3);

        private final String label;
        private final int rank;

        Level(String label, int rank) {   // constants get constructor args
            this.label = label;
            this.rank = rank;
        }

        public String label() { return label; }
        public int rank() { return rank; }

        public boolean isAtLeast(Level other) {
            return this.rank >= other.rank;
        }
    }

    public static void main(String[] args) {
        Level l = Level.HIGH;
        System.out.println(l.label() + " -> " + l.ordinal());   // error -> 2

        // exhaustive values() / valueOf()
        for (Level v : Level.values()) {
            System.out.printf("%s(%d)%n", v, v.rank());
        }

        // switch - pattern-friendly and (with arrow form) expression-able
        String sound = switch (l) {
            case LOW -> "tick";
            case MEDIUM -> "beep";
            case HIGH -> "ALARM";
        };
        System.out.println(sound);

        // EnumSet/EnumMap: bit-set fast, null-hostile, insertion-order options
        EnumSet<Level> urgent = EnumSet.of(Level.MEDIUM, Level.HIGH);
        EnumMap<Level, String> tips = new EnumMap<>(Level.class);
        tips.put(Level.LOW, "check logs");
        System.out.println(urgent + " / " + tips.get(Level.LOW));
    }
}
```

Why enums beat `int` constants: type safety, switch support, per-constant behavior, safe serialization (identity guaranteed!), EnumSet/EnumMap performance, no "5 is not a valid color" bugs.

**Interfaces with enums** (one constant overriding methods):

```java title=Planet.java
public enum Planet {
    EARTH   { double surfaceGravity() { return 9.8; } },
    MARS    { double surfaceGravity() { return 3.7; } };

    abstract double surfaceGravity();
    double weight(double massKg) { return massKg * surfaceGravity(); }
}
```

## Legacy `Enumeration`

```java title=EnumerationDemo.java
import java.util.Vector;
import java.util.Enumeration;
import java.util.Hashtable;

public class EnumerationDemo {
    public static void main(String[] args) {
        Vector<String> v = new Vector<>(java.util.List.of("a", "b", "c"));

        Enumeration<String> e = v.elements();       // legacy traversal
        while (e.hasMoreElements()) {
            System.out.print(e.nextElement() + " ");   // a b c
        }

        Hashtable<String, Integer> scores = new Hashtable<>();
        scores.put("ada", 10);
        Enumeration<String> keys = scores.keys();     // like keySet() iterator
        while (keys.hasMoreElements()) {
            System.out.println(keys.nextElement());
        }
    }
}
```

`Enumeration` has **no `remove()`** - it predates the Collections Framework (1.2). APIs that still expose it (e.g. some JAR resource listings, very old servlet headers code) should be adapted:

```java title=Adapt.java
List<String> list = Collections.list(enumeration);   // bulk convert
// or: Collections.enumeration(list) goes the other way (rarely needed)
```

## Enumeration vs Iterator

| | `Enumeration` | `Iterator` |
|---|---|---|
| Since | JDK 1.0 | JDK 1.2 |
| Methods | `hasMoreElements`, `nextElement` | `hasNext`, `next`, **`remove`** |
| Fail-fast | No | Yes (ConcurrentModificationException) |
| Framework | old Vector/Hashtable | **all** Collections |
| Modern use | read only, legacy APIs | the default |

New code: **`Iterator`** (or better, for-each / Streams). Know `Enumeration` only to read old systems.

## Quick quiz

1. Which is faster for a million enum flags: `EnumSet.of(...)`, `HashSet.of(...)`? → EnumSet (bit vector over the ordinal range).
2. Why is `ordinal()` dangerous for persistence? → inserting a constant shifts ordinals; store `name()` or an explicit code.
3. `valueOf("high")` vs `Level.valueOf("HIGH")`? → constants are case-sensitive; `valueOf` takes the exact declared name.

Related: [Collections overview](collections.html) · [Generics](generics.html) · [Iterators & fail-fast in the archive](collections-aniteratorwrapperforanenumeration.html)
