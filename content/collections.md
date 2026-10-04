---
title: Java Collections Framework
nav: Collections
description: The Collections framework overview - List, Set, Map, Queue - and when to choose each implementation.
section: Collections
order: 10
---

## What is the Collections framework?

A standard set of interfaces and classes for holding groups of objects:

```text title=The family tree
 Collection (interface)
 ├── List      - ordered, duplicates allowed, by index
 ├── Set       - unique elements
 ├── Queue     - FIFO / priority ordering
 └── Deque     - double-ended queue

 Map (separate hierarchy) - key -> value pairs
```

Everything lives in `java.util`.

## Choosing the right implementation

**Lists**

| Class | Backed by | Get by index | Insert/remove | Use when |
|---|---|---|---|---|
| `ArrayList` | array | O(1) | O(n) (shift) | read-heavy, default choice |
| `LinkedList` | nodes | O(n) | O(1) at head/tail | heavy insert/remove at ends |
| `Vector` | array + locks | O(1) | O(n) | legacy - don't start new code with it |

**Sets**

| Class | Guarantees | Use when |
|---|---|---|
| `HashSet` | unique, unordered, O(1) | membership tests (default) |
| `LinkedHashSet` | unique, insertion order | unique + stable order |
| `TreeSet` | unique, sorted, O(log n) | range queries / sorted output |

**Maps**

| Class | Guarantees | Use when |
|---|---|---|
| `HashMap` | fast, unordered | lookup by key (default) |
| `LinkedHashMap` | insertion order | map + stable iteration |
| `TreeMap` | sorted by key | ordered keys / navigable ranges |
| `ConcurrentHashMap` | thread-safe, no locking reads | multi-threaded access |

## Core operations (same shape everywhere)

```java title=Basics.java
import java.util.*;

public class Basics {
    public static void main(String[] args) {
        // List
        List<String> list = new ArrayList<>();
        list.add("java");
        list.add("python");
        list.add("go");
        list.add(1, "rust");                 // insert at index
        System.out.println(list);            // [java, rust, python, go]
        System.out.println(list.get(0));     // java
        list.remove("go");                   // by object
        list.remove(0);                      // by index (careful: 0 is int!)
        System.out.println(list.contains("rust") + " size=" + list.size());

        // Set
        Set<Integer> set = new HashSet<>(List.of(3, 1, 3, 2));
        System.out.println(set);             // [1, 2, 3] - duplicates dropped
        set.add(4);
        System.out.println(set.contains(3) + " " + set.isEmpty());

        // Map
        Map<String, Integer> ages = new HashMap<>();
        ages.put("Ada", 36);
        ages.put("Lin", 28);
        ages.put("Ada", 37);                 // keys unique - updates in place
        System.out.println(ages);
        System.out.println(ages.get("Lin"));       // 28
        System.out.println(ages.getOrDefault("Bo", -1));  // -1
        ages.remove("Lin");
        System.out.println(ages.keySet() + " " + ages.values());
    }
}
```

> **Warning:** `list.remove(0)` on a `List<Integer>` removes *index* 0; `list.remove(Integer.valueOf(0))` removes the *object*. Mixing `int`/`Integer` here is a famous bug source.

## Iterating

```java title=Iteration.java
import java.util.*;

public class Iteration {
    public static void main(String[] args) {
        List<String> names = new ArrayList<>(List.of("A", "B", "C"));

        // 1. for-each (preferred for reading)
        for (String n : names) System.out.print(n + " ");

        // 2. classic index loop (when you need the index)
        for (int i = 0; i < names.size(); i++) System.out.print(names.get(i) + " ");

        // 3. lambda + stream (preferred for transforming)
        names.stream().map(String::toUpperCase).forEach(s -> System.out.print(s + " "));
        System.out.println();

        // 4. iterator - the only safe way to REMOVE while iterating
        Iterator<String> it = names.iterator();
        while (it.hasNext()) {
            if (it.next().equals("B")) it.remove();
        }
        System.out.println(names);           // [A, C]

        // Map iteration
        Map<String, Integer> m = Map.of("x", 1, "y", 2);
        m.forEach((k, v) -> System.out.println(k + " -> " + v));
        for (Map.Entry<String, Integer> e : m.entrySet()) {
            System.out.println(e.getKey() + " = " + e.getValue());
        }
    }
}
```

> **Warning:** Never `list.remove(x)` inside a for-each loop over the same list - you get `ConcurrentModificationException`. Use the `Iterator` or a stream `filter`.

## Sorting and searching

```java title=Sorting.java
import java.util.*;

public class Sorting {
    public static void main(String[] args) {
        List<Integer> nums = new ArrayList<>(List.of(5, 2, 9, 1));

        Collections.sort(nums);                       // in-place
        System.out.println(nums);                     // [1, 2, 5, 9]

        Collections.sort(nums, Collections.reverseOrder());
        System.out.println(nums);                     // [9, 5, 2, 1]

        List<String> names = new ArrayList<>(List.of("zoe", "amy", "bob"));
        names.sort(Comparator.comparingInt(String::length));
        System.out.println(names);                    // [zoe, bob, amy]

        // binarySearch works ONLY on sorted lists
        Collections.sort(names);
        System.out.println(Collections.binarySearch(names, "bob"));

        // the stream style (returns a new list)
        List<String> sorted = names.stream().sorted().toList();
        System.out.println(sorted);
    }
}
```

## Immutable views

```java title=Immutable.java
import java.util.*;

public class Immutable {
    public static void main(String[] args) {
        List<String> fixed = List.of("a", "b");          // fixed-size, cannot add/remove
        Map<String, Integer> frozen = Map.of("k", 1);    // truly immutable

        try {
            fixed.add("c");                       // List.of(...) rejects every modification
        } catch (UnsupportedOperationException e) {
            System.out.println("blocked: unsupported operation");
        }

        // unmodifiable COPY of something you built yourself
        List<String> built = new ArrayList<>(List.of("x", "y"));
        List<String> view = Collections.unmodifiableList(built);
        System.out.println(view);
    }
}
```

`List.of(...)` throws on any attempt to modify - great for constants and defensive returns. (Java 10+: `List.copyOf(list)`.)

## Collections utility cheat sheet

| Task | Call |
|---|---|
| Sort | `Collections.sort(list)` / `list.sort(cmp)` |
| Reverse | `Collections.reverse(list)` |
| Shuffle | `Collections.shuffle(list)` |
| Max/min | `Collections.max(coll)` |
| Frequency | `Collections.frequency(coll, obj)` |
| Fill/swap | `Collections.fill(list, v)`, `swap(list, i, j)` |
| Empty views | `Collections.emptyList()` |

## Performance intuition

```text title=Big-O quick reference (average case)
 ArrayList.get(i)          O(1)      HashMap.get(k)       O(1)
 ArrayList.add (end)       amortized O(1)
 ArrayList.add (middle)    O(n)      HashMap.put/remove   O(1)
 LinkedList.get(i)         O(n)      TreeSet ops          O(log n)
 HashSet.contains          O(1)      iteration of ArrayList O(n), fast in practice
```

Pick by **access pattern**, not vibes:

- Lots of reads by position → `ArrayList`
- Lots of lookups by key → `HashMap`
- Need sorted keys / ranges → `TreeMap` / `TreeSet`
- Unique elements only → `HashSet`

Deep dives: [ArrayList](arraylist.html), [HashMap](hashmap.html).

> **Remember:** Program to the **interface** (`List`, `Map`, `Set`) and instantiate the implementation (`new ArrayList<>()`) - switching later becomes a one-line change.
