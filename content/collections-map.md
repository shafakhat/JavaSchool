---
title: Java Map Interface
nav: Map (HashMap, TreeMap, Hashtable)
description: Complete guide to the Java Map hierarchy - HashMap, LinkedHashMap, TreeMap, Hashtable, EnumMap, ConcurrentHashMap, WeakHashMap and friends.
section: Collections
order: 80
---

## The Map family tree

```text title=hierarchy (Map is NOT a Collection - it sits beside it)
Map (key -> value, unique keys)
├── HashMap              - hash table (default)
│   └── LinkedHashMap    - + insertion/access order (linked list)
├── TreeMap              - red-black tree, sorted by key/comparator
│   └─ interfaces: SortedMap -> NavigableMap (range + neighbor lookups)
├── Hashtable            - legacy synchronized (Dictionary-era)
│   └── Properties       - legacy string config file support
├── WeakHashMap          - keys weakly held - auto-evictable cache
├── IdentityHashMap      - == comparison instead of equals
├── EnumMap              - ordinal-indexed, for enum keys (fastest)
├── ConcurrentHashMap    - concurrent hash (Java 8+: CAS + bin locks)
├── ConcurrentSkipListMap- concurrent sorted map
└── (interface) Map.Entry, NavigableMap, ...
```

| Class | Order | get | Null keys/values | Concurrent |
|---|---|---|---|---|
| **HashMap** | none | O(1) avg | 1 null key, many null values | no |
| **LinkedHashMap** | insertion / access | O(1) | same as HashMap | no |
| **TreeMap** | sorted | O(log n) | no nulls (NPE) | no |
| **EnumMap** | enum ordinal | O(1) | no nulls | no |
| **Hashtable** | none | O(1) | no | synchronized |
| **Properties** | none | O(1) | no | synchronized |
| **WeakHashMap** | none | O(1) | no nulls | no |
| **IdentityHashMap** | none | O(1) | yes | no |
| **ConcurrentHashMap** | none | O(1) lock-free read | no nulls | yes |
| **ConcurrentSkipListMap** | sorted | O(log n) | no nulls | yes |

## HashMap - the default

```java title=HashMapDemo.java
import java.util.*;

public class HashMapDemo {
    public static void main(String[] args) {
        Map<String, Integer> ages = new HashMap<>();
        ages.put("ada", 36);
        ages.put("grace", 45);
        ages.put("ada", 37);                    // key unique - replaces value

        System.out.println(ages.get("ada"));            // 37
        System.out.println(ages.getOrDefault("bob", 0));// 0
        System.out.println(ages.containsKey("grace"));  // true
        System.out.println(ages.containsValue(45));     // true - O(n)

        ages.putIfAbsent("bob", 20);            // only if absent
        ages.remove("bob");                     // by key
        ages.remove("ada", 37);                 // conditional remove (key+value)
        ages.merge("grace", 5, Integer::sum);   // 45 + 5 = 50 (atomic in CHM)
        ages.computeIfAbsent("eve", k -> k.length()); // lazy create
        ages.replaceAll((k, v) -> v + 1);

        // iteration - all four styles
        for (Map.Entry<String, Integer> e : ages.entrySet()) {
            System.out.println(e.getKey() + " -> " + e.getValue());
        }
        ages.forEach((k, v) -> System.out.println(k + "=" + v));
        ages.keySet().forEach(System.out::println);      // view!
        ages.values().forEach(System.out::println);

        // bulk
        Map<String, Integer> other = Map.of("zoe", 1);
        ages.putAll(other);
        System.out.println(ages.size());
    }
}
```

Key contract: `hashCode()+equals` of keys decides bucket then identity; keys **must** be immutable-in-practice (changing a key while it's a map key = lost entry); load factor 0.75, resize ×2, treeify at 8/bin (table ≥ 64).

## LinkedHashMap - order & LRU

```java title=LinkedHashMapDemo.java
import java.util.*;

public class LinkedHashMapDemo {
    public static void main(String[] args) {
        // insertion order
        Map<String, Integer> m = new LinkedHashMap<>();
        m.put("b", 2); m.put("a", 1); m.put("c", 3);
        System.out.println(m.keySet());          // [b, a, c]

        // access-order mode + eviction = tiny LRU cache
        Map<String, String> lru = new LinkedHashMap<>(16, 0.75f, true) {
            @Override
            protected boolean removeEldestEntry(Map.Entry<String, String> e) {
                return size() > 3;               // evict oldest-accessed
            }
        };
        lru.put("1", "a"); lru.put("2", "b"); lru.put("3", "c");
        lru.get("1");                            // "1" now most-recent
        lru.put("4", "d");                       // evicts "2"
        System.out.println(lru.keySet());        // [3, 1, 4]  (order by recency)
    }
}
```

Also the base class behind `LinkedHashSet` and used by frameworks for ordered config.

## TreeMap & NavigableMap

```java title=TreeMapDemo.java
import java.util.*;

public class TreeMapDemo {
    public static void main(String[] args) {
        TreeMap<String, Integer> t = new TreeMap<>();
        t.put("pear", 3); t.put("apple", 1); t.put("mango", 2);

        System.out.println(t.firstKey());            // apple
        System.out.println(t.lastEntry());           // mango=2
        System.out.println(t.floorEntry("b"));       // apple=1 (<= "b")
        System.out.println(t.ceilingEntry("bb"));    // mango=3? -> "mango" (>= "bb")
        System.out.println(t.lowerKey("mango"));     // apple
        System.out.println(t.higherKey("apple"));    // mango
        System.out.println(t.headMap("mango"));      // {apple=1, pear=3}
        System.out.println(t.subMap("a", "n"));      // a..m
        NavigableMap<String, Integer> rev = t.descendingMap();
        System.out.println(rev.firstKey());          // pear

        // sorted views stay live with the backing map
        SortedMap<String, Integer> view = t.headMap("m");
        view.put("kiwi", 4);
        System.out.println(t.containsKey("kiwi"));   // true

        // custom keys: must supply a total ordering
        TreeMap<String, Integer> byLen = new TreeMap<>(Comparator.comparingInt(String::length));
        byLen.put("ccc", 1); byLen.put("a", 2);
        System.out.println(byLen.keySet());          // [a, ccc]
    }
}
```

## Hashtable, Properties, WeakHashMap, IdentityHashMap, EnumMap

```java title=Variants.java
import java.util.*;
import java.io.*;

public class Variants {
    public static void main(String[] args) throws Exception {
        // Hashtable - legacy synchronized, no nulls anywhere
        Hashtable<String, Integer> h = new Hashtable<>();
        h.put("k", 1);
        // h.put(null, 1);   // NPE
        System.out.println(h.get("k"));

        // Properties - the classic config file (strings only)
        Properties p = new Properties();
        p.setProperty("db.url", "jdbc:h2:mem:x");
        try (var reader = new StringReader("mode=fast\nsize=9")) {
            p.load(reader);
        }
        p.store(new StringWriter(), "app config");
        System.out.println(p.getProperty("mode"));   // fast

        // WeakHashMap - keys collected when nothing else references them
        WeakHashMap<Object, String> weak = new WeakHashMap<>();
        Object key = new Object();
        weak.put(key, "alive");
        key = null;                                  // entry evictable at next GC
        System.gc();
        System.out.println(weak.size());             // 0 (usually)

        // IdentityHashMap - == not equals (canonicalization, mirror structures)
        IdentityHashMap<String, String> id = new IdentityHashMap<>();
        String a = new String("x"), b = new String("x");
        id.put(a, "first"); id.put(b, "second");
        System.out.println(id.size());               // 2 (equals() would merge)

        // EnumMap - bitset over enum ordinals
        enum Day { MON, TUE, WED }
        // (enums must be top-level/nested - shown inline for brevity of reading)
    }
}
```

`Properties`: prefer `Map<String,String>`/YAML/JSON in new code - it's a `Hashtable<Object,Object>` from 1996 (backed by `String` values only in practice).

## ConcurrentHashMap - the concurrent Map

```java title=CHM.java
import java.util.concurrent.*;

public class CHM {
    public static void main(String[] args) throws Exception {
        ConcurrentHashMap<String, Integer> c = new ConcurrentHashMap<>();
        c.put("hits", 0);

        // atomic compound actions - no external lock needed
        c.compute("hits", (k, v) -> v + 1);
        c.merge("hits", 1, Integer::sum);
        Integer now = c.putIfAbsent("views", 1);

        // replace-if-exact (optimistic locking pattern)
        c.replace("hits", 1, 2);

        // nulls forbidden (ambiguity with "absent" in get)
        // c.put("k", null);   // NPE

        // iteration is weakly consistent - no ConcurrentModificationException
        c.forEach((k, v) -> System.out.println(k + "=" + v));

        // parallel bulk (uses internal segment-level parallelism)
        c.replaceAll((k, v) -> v * 2);
        long sum = c.mappingCount();
        System.out.println("count=" + sum);
    }
}
```

`size()`/`isEmpty()` are estimates under concurrency - use `mappingCount()` and don't build logic on exact mid-flight sizes. `Collections.synchronizedMap` exists but needs manual locking for iteration - CHM is nearly always better.

## Choosing

```text title=decision
one map to rule your code ........................> HashMap
need insertion order / LRU .......................> LinkedHashMap (+removeEldestEntry)
sorted keys / floor-ceiling ranges ................> TreeMap (NavigableMap)
keys are enum constants ..........................> EnumMap
concurrent access .................................> ConcurrentHashMap
concurrent + sorted ................................> ConcurrentSkipListMap
legacy config files / synchronized Vector-era .....> Properties / Hashtable (recognize only)
cache keyed by objects that can die ...............> WeakHashMap
identity-sensitive structures (parser trees) ......> IdentityHashMap
```

Related: [Collections overview](collections.html) · [Set](collections-set.html) · [Queue](collections-queue.html) · [HashMap internals interview Q&A](interview.html) · [Map examples in the archive](collections-data-structure-amemoryefficienthashmap.html)
