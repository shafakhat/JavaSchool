---
title: Java Set Interface
nav: Set (HashSet, LinkedHashSet, TreeSet)
description: Complete guide to Java Sets - HashSet, LinkedHashSet, TreeSet, EnumSet, SortedSet, NavigableSet, CopyOnWriteArraySet with all behaviors.
section: Collections
order: 60
---

## The Set family tree

```text title=java.util Set hierarchy
Collection
└── Set (unique elements, no order guarantee)
    ├── HashSet            - hash table (O(1), unordered)
    │   └── LinkedHashSet  - hash + insertion/access order links
    ├── TreeSet            - red-black tree (sorted, O(log n))
    │   └── (interfaces) SortedSet -> NavigableSet (range ops)
    ├── AbstractSet        - shared equals/hashCode implementation
    └── (concurrent) CopyOnWriteArraySet, ConcurrentSkipListSet
EnumSet (abstract) -> RegularEnumSet / JumboEnumSet - bit vectors over enums
```

| Class | Order | get/contains | Nulls | Notes |
|---|---|---|---|---|
| **HashSet** | none | O(1) avg | 1 allowed | backed by HashMap |
| **LinkedHashSet** | insertion (or access*) | O(1) | 1 allowed | *if constructed accessOrder-style via constructor arg on the map side; LinkedHashSet itself = insertion order |
| **TreeSet** | sorted / comparator | O(log n) | **no** | NavigableSet extras |
| **EnumSet** | enum ordinal | O(1) | no | tiny/bitset, only enum constants |
| **CopyOnWriteArraySet** | insertion | O(n) read | yes | snapshot iteration |
| **ConcurrentSkipListSet** | sorted | O(log n) | no | concurrent TreeSet |

## HashSet - the workhorse

```java title=HashSetDemo.java
import java.util.*;

public class HashSetDemo {
    public static void main(String[] args) {
        Set<String> set = new HashSet<>(List.of("java", "go", "java"));

        set.add("rust");
        boolean added = set.add("rust");       // false - duplicate rejected
        set.addAll(Set.of("c", "zigzag"));
        set.retainAll(Set.of("java", "go"));   // intersection with argument
        set.removeAll(Set.of("go"));           // difference

        System.out.println(set.contains("java"));      // O(1) via hashCode+equals
        System.out.println(set.size());
        set.removeIf(s -> s.length() < 2);

        // iteration order is undefined - never rely on it
        for (String s : set) System.out.println(s);

        // set algebra
        Set<String> a = new HashSet<>(List.of("x", "y", "z"));
        Set<String> b = new HashSet<>(List.of("y", "w"));
        Set<String> inter = new HashSet<>(a); inter.retainAll(b);   // {y}
        Set<String> union = new HashSet<>(a); union.addAll(b);      // {x,y,z,w}
        Set<String> diff  = new HashSet<>(a); diff.removeAll(b);    // {x,z}

        // equals between sets ignores order: new HashSet<>(a).equals(b)
    }
}
```

Under the hood: a `HashMap` where the element is the key and a shared `PRESENT` object is the value - same resize (1.5x at 75%), treeification (≥8 in a bin), and contract: **equal objects must hash equally**.

## LinkedHashSet - predictable order

```java title=LinkedHashSetDemo.java
import java.util.*;

public class LinkedHashSetDemo {
    public static void main(String[] args) {
        Set<String> s = new LinkedHashSet<>(List.of("m", "a", "z"));
        System.out.println(s);              // [m, a, z] - insertion order kept
        // re-adding an existing element does NOT change its position
        s.add("m");
        System.out.println(s);              // [m, a, z]
        // iteration is stable across runs - safe for UI lists / tests
        for (String x : s) System.out.print(x + " ");   // m a z
    }
}
```

Cost: two extra pointers per entry vs HashSet. Use whenever output order matters (menus, recent-items, deterministic tests).

## TreeSet & NavigableSet - sorted, with range operations

```java title=TreeSetDemo.java
import java.util.*;

public class TreeSetDemo {
    public static void main(String[] args) {
        TreeSet<Integer> t = new TreeSet<>(List.of(5, 1, 9, 3));

        System.out.println(t.first());               // 1
        System.out.println(t.last());                // 9
        System.out.println(t.floor(4));              // 3  - greatest <= 4
        System.out.println(t.ceiling(4));            // 5  - least  >= 4
        System.out.println(t.lower(5));              // 3  - greatest <  5
        System.out.println(t.higher(5));             // 9  - least  >  5
        System.out.println(t.headSet(5));            // {1, 3}
        System.out.println(t.tailSet(5));            // {5, 9}
        System.out.println(t.subSet(3, 9));          // {3, 5}  (hi exclusive)
        System.out.println(t.pollFirst());           // 1 (removes)

        SortedSet<String> sorted = new TreeSet<>(Set.of("pear", "apple"));
        for (String s : sorted) System.out.print(s + " ");   // apple pear

        // custom ordering
        TreeSet<String> byLen = new TreeSet<>(Comparator.comparingInt(String::length));
        byLen.addAll(List.of("bbb", "a", "cc"));
        System.out.println(byLen);                   // [a, cc, bbb]
    }
}
```

Rules: **no nulls** (first null breaks comparator/compareTo contracts); consistency with `equals` recommended for `compareTo` (`TreeSet.equals` is still AbstractSet's). `NavigableSet` is what you code against for schedulers, leaderboards, "next bigger item" logic.

## EnumSet - the fastest set when keys are enums

```java title=EnumSetDemo.java
import java.util.*;

public class EnumSetDemo {
    enum Skill { JAVA, SQL, K8S, GO }

    public static void main(String[] args) {
        EnumSet<Skill> none = EnumSet.noneOf(Skill.class);        // empty
        EnumSet<Skill> all  = EnumSet.allOf(Skill.class);
        EnumSet<Skill> some = EnumSet.of(Skill.JAVA, Skill.K8S);
        EnumSet<Skill> range = EnumSet.range(Skill.JAVA, Skill.K8S); // JAVA,SQL,K8S

        some.add(Skill.GO);
        some.remove(Skill.SQL);
        System.out.println(some.contains(Skill.JAVA));  // true - bit test O(1)

        // set algebra on enums is cheap and expressive
        EnumSet<Skill> missing = EnumSet.complementOf(some);
        System.out.println("missing: " + missing);      // SQL
        System.out.println(all.containsAll(some));      // true
    }
}
```

RegularEnumSet (≤64 constants → one long) or JumboEnumSet (long[]); serialization-stable, null-hostile, iteration in ordinal order.

## Concurrent sets

```java title=ConcurrentSets.java
import java.util.concurrent.*;

public class ConcurrentSets {
    public static void main(String[] args) {
        // read-mostly: snapshot iteration, O(n) contains
        CopyOnWriteArraySet<String> cow = new CopyOnWriteArraySet<>();
        cow.add("config-a");

        // concurrent sorted set: skip list, O(log n), weakly consistent iteration
        ConcurrentSkipListSet<Integer> skl = new ConcurrentSkipListSet<>();
        skl.add(3); skl.add(1);
        System.out.println(skLhead(skl));

        // usual answer instead: ConcurrentHashMap.newKeySet()
        var keySet = ConcurrentHashMap.<String>newKeySet();
        keySet.add("workers-1");
        keySet.forEach(System.out::println);
    }

    static Object skLhead(ConcurrentSkipListSet<Integer> s) { return s.first(); }
}
```

## Put-everything-together examples

```java title=Recipes.java
import java.util.*;
import java.util.stream.*;

public class Recipes {
    public static void main(String[] args) {
        List<String> words = List.of("the", "cat", "the", "sat");

        // unique preserving encounter order
        Set<String> unique = new LinkedHashSet<>(words);

        // duplicates found
        Set<String> seen = new HashSet<>();
        List<String> dups = words.stream()
            .filter(w -> !seen.add(w))          // add() false => duplicate
            .toList();
        System.out.println("dups: " + dups);    // [the]

        // sets from streams - and back
        Set<Integer> lens = words.stream().map(String::length).collect(Collectors.toSet());
        List<String> sortedUnique = new TreeSet<>(words).stream().toList();

        // dedupe objects by key
        record User(long id, String name) {}
        List<User> users = List.of(new User(1, "a"), new User(1, "b"), new User(2, "c"));
        Map<Long, User> byId = users.stream()
            .collect(Collectors.toMap(User::id, u -> u, (a, b) -> a));
        System.out.println(byId.keySet());      // [1, 2]
    }
}
```

Related: [Collections overview](collections.html) · [List](collections-list.html) · [Queue & Deque](collections-queue.html) · [Map](collections-map.html) · [Set examples in the archive](collections-asortedsetisasetthatmaintainsitsitemsinasortedorder.html)
