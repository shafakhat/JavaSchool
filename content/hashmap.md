---
title: Java HashMap
nav: HashMap
description: HashMap in depth - put, get, merge, iterate, custom keys and how hashing works internally.
section: Collections
order: 30
---

## The map you'll use most

`HashMap` stores **key -> value** pairs with near-constant time lookups:

- `get(key)` / `put(key, value)` - **O(1)** average
- allows one `null` key and multiple `null` values
- **unordered** - iteration order is unspecified (use `LinkedHashMap` if you care)
- not thread-safe (use `ConcurrentHashMap` for concurrency)

```java title=Create.java
import java.util.HashMap;
import java.util.Map;

public class Create {
    public static void main(String[] args) {
        Map<String, Integer> scores = new HashMap<>();
        scores.put("math", 92);
        scores.put("english", 85);
        scores.put("science", 88);

        System.out.println(scores);                    // {math=92, ...}
        System.out.println(scores.get("math"));        // 92
        System.out.println(scores.size());             // 3
        System.out.println(scores.containsKey("art")); // false
        System.out.println(scores.containsValue(85));  // true
    }
}
```

## Reading safely

```java title=Read.java
import java.util.HashMap;
import java.util.Map;

public class Read {
    public static void main(String[] args) {
        Map<String, Integer> stock = new HashMap<>();
        stock.put("pen", 10);

        Integer n = stock.get("pencil");       // null - key missing
        // int x = stock.get("pencil");        // NPE on unboxing!

        int count = stock.getOrDefault("pencil", 0);   // 0 - the safe way
        System.out.println("pencil=" + count);

        stock.putIfAbsent("pen", 99);          // only if absent - keeps 10
        stock.putIfAbsent("marker", 4);
        System.out.println(stock);
    }
}
```

> **Warning:** `map.get()` returns `null` for missing keys. Auto-unboxing that into `int` throws `NullPointerException`. Always prefer `getOrDefault` when absence is normal.

## Updating, merging, computing

```java title=Update.java
import java.util.HashMap;
import java.util.Map;

public class Update {
    public static void main(String[] args) {
        Map<String, Integer> wordCount = new HashMap<>();

        // classic count pattern
        String[] words = "the cat sat on the mat the cat".split(" ");
        for (String w : words) {
            wordCount.put(w, wordCount.getOrDefault(w, 0) + 1);
        }
        System.out.println(wordCount);   // {the=3, cat=2, sat=1, on=1, mat=1}

        // modern one-liner (Java 8+)
        Map<String, Integer> wc2 = new HashMap<>();
        for (String w : words) wc2.merge(w, 1, Integer::sum);
        System.out.println(wc2);

        // compute / computeIfAbsent
        Map<String, java.util.List<String>> byLetter = new HashMap<>();
        for (String w : words) {
            byLetter.computeIfAbsent(w.substring(0, 1), k -> new java.util.ArrayList<>()).add(w);
        }
        System.out.println(byLetter);

        wordCount.put("the", 100);              // plain overwrite
        wordCount.computeIfPresent("cat", (k, v) -> v * 10);
        wordCount.remove("sat");
        System.out.println(wordCount);
    }
}
```

| Method | Behavior |
|---|---|
| `put(k,v)` | store/overwrite, returns previous value |
| `putIfAbsent(k,v)` | store only if key missing |
| `getOrDefault(k,d)` | read with default |
| `merge(k,v,fn)` | combine old + new with a function |
| `compute(k,fn)` | recompute value for key (null removes) |
| `computeIfAbsent(k,fn)` | build value lazily, only when missing |
| `replace(k,v)` | update only if key exists |

## Iterating a map

```java title=Iterate.java
import java.util.HashMap;
import java.util.Map;

public class Iterate {
    public static void main(String[] args) {
        Map<String, Integer> ages = new HashMap<>();
        ages.put("Ada", 36);
        ages.put("Lin", 28);
        ages.put("Sam", 41);

        // 1. entrySet - most common
        for (Map.Entry<String, Integer> e : ages.entrySet()) {
            System.out.println(e.getKey() + " is " + e.getValue());
        }

        // 2. lambda
        ages.forEach((name, age) -> System.out.println(name + "/" + age));

        // 3. keys, values, or both separately
        ages.keySet().stream().sorted().forEach(System.out::println);
        System.out.println(ages.values());
        System.out.println("total = " + ages.values().stream().mapToInt(Integer::intValue).sum());
    }
}
```

Never modify a map's structure (`put`/`remove`) while iterating its `entrySet` - it throws `ConcurrentModificationException`. Transform with streams, or remove via `Iterator.remove` / `removeIf`.

## Using objects as keys

Your key class needs correct `equals` and `hashCode`:

```java title=Key.java
import java.util.HashMap;
import java.util.Map;
import java.util.Objects;

public class Key {
    record Point(int x, int y) {}    // records auto-generate equals/hashCode

    static class City {
        final String name, country;
        City(String name, String country) {
            this.name = name;
            this.country = country;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (!(o instanceof City c)) return false;
            return name.equals(c.name) && country.equals(c.country);
        }

        @Override
        public int hashCode() {
            return Objects.hash(name, country);
        }

        @Override
        public String toString() { return name + "(" + country + ")"; }
    }

    public static void main(String[] args) {
        Map<City, String> timezone = new HashMap<>();
        timezone.put(new City("Hyderabad", "IN"), "Asia/Kolkata");
        timezone.put(new City("Berlin", "DE"), "Europe/Berlin");

        // works even though these are different City OBJECTS:
        System.out.println(timezone.get(new City("Hyderabad", "IN")));  // Asia/Kolkata
        System.out.println(timezone.get(new Point(1, 2)));              // null (no such key)

        Map<Point, String> labels = new HashMap<>();
        labels.put(new Point(3, 4), "origin-ish");
        System.out.println(labels.get(new Point(3, 4)));                // origin-ish - records shine
    }
}
```

The contract: **if `a.equals(b)` then `a.hashCode() == b.hashCode()`** - break it and lookups silently fail.

## How HashMap works (mental model)

```text title=Buckets and chains (pre-Java 8 simplified)
 hash(key) -> bucket index
      |
 [0] -> null
 [1] -> KeyA -> null          (separate chaining)
 [2] -> KeyB -> KeyC -> null
 [3] -> null

 Java 8+: a chain grows into a RED-BLACK TREE when > 8 nodes (O(log n) worst case)
```

- Good hash spreads keys across buckets; collisions create chains.
- Resizing (when load factor > 0.75) re-hashes everything - O(n), rare.
- That's why **stable, well-distributed `hashCode`** matters.

```java title=HashDemo.java
import java.util.HashMap;

public class HashDemo {
    public static void main(String[] args) {
        HashMap<String, Integer> m = new HashMap<>();
        m.put("alpha", 1);
        m.put("beta", 2);
        System.out.println("alpha hash = " + "alpha".hashCode());
        System.out.println("bucket hint = " + ("alpha".hashCode() % 16));
        System.out.println(m);
    }
}
```

## Choosing the variant

| Need | Use |
|---|---|
| General lookup | `HashMap` |
| Insertion/iteration order matters | `LinkedHashMap` |
| Sorted keys / floor / ceiling ops | `TreeMap` |
| Concurrent access | `ConcurrentHashMap` |
| Tiny map, immutable | `Map.of(...)` |
| Count things frequently | `HashMap` + `merge` / `getOrDefault` |

> **Remember:** `HashMap` allows one `null` key (it hashes to bucket 0) - but relying on it is poor style; `TreeMap` forbids `null` keys entirely.

Next: [JDBC](jdbc.html) - connecting Java to a database.
