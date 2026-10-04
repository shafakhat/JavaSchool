---
title: Java List Interface
nav: List (ArrayList, LinkedList, Vector)
description: Complete guide to the Java List hierarchy - ArrayList, LinkedList, Vector, Stack, CopyOnWriteArrayList with methods, complexity and use cases.
section: Collections
order: 50
---

## The List family tree

```text title=java.util List hierarchy
Collection
└── List (ordered, indexed, allows duplicates)
    ├── ArrayList        - resizable array (default choice)
    ├── LinkedList       - doubly linked list (+ Deque)
    ├── Vector           - legacy synchronized array (Hashtable-era)
    │   └── Stack        - legacy LIFO (prefer Deque)
    └── (concurrent) CopyOnWriteArrayList - snapshot iterator, RW-heavy
Interfaces above: SequencedCollection (Java 21) -> List
Common implementations also implement: RandomAccess (ArrayList, Vector)
```

| Class | Backing | get(i) | add middle | remove middle | Thread-safe |
|---|---|---|---|---|---|
| **ArrayList** | array | O(1) | O(n) | O(n) | No |
| **LinkedList** | nodes | O(n) | O(1)* | O(1)* | No |
| **Vector** | array | O(1) | O(n) | O(n) | synchronized |
| **Stack** | array (Vector) | O(n) pop top | — | — | synchronized |
| **CopyOnWriteArrayList** | array copy-on-write | O(1) | O(n) | O(n) | yes (lock-free reads) |

\* with the iterator/handle already positioned; blind index operations are still O(n).

## ArrayList - the default

```java title=ArrayListDemo.java
import java.util.*;

public class ArrayListDemo {
    public static void main(String[] args) {
        ArrayList<String> list = new ArrayList<>();          // capacity 10
        list.add("java");
        list.add("python");
        list.add(1, "kotlin");                                // insert at index
        list.addAll(List.of("go", "rust"));
        list.set(0, "java2");                                 // replace
        String got = list.get(0);                             // O(1)
        list.remove("python");                                // by object -> O(n) search
        list.removeIf(s -> s.length() > 4);                   // bulk filter
        boolean has = list.contains("go");                    // O(n)
        list.sort(Comparator.naturalOrder());

        System.out.println(list);                             // [java2, kotlin, go, rust]
        System.out.println("index of go = " + list.indexOf("go"));

        // iteration - three safe styles
        for (String s : list) System.out.println(s);          // iterator (fail-fast)
        list.forEach(System.out::println);
        ListIterator<String> li = list.listIterator();        // bidirectional + set/remove
        while (li.hasNext()) { li.next(); if (li.nextIndex() == 2) { li.set("X"); } }

        // views (backed by the list!)
        List<String> sub = list.subList(1, 3);                // window into the array
        sub.clear();                                          // removes from the ORIGINAL

        // conversion
        String[] arr = list.toArray(new String[0]);
        List<Integer> boxed = List.of(1, 2, 3);               // immutable, fixed
        ArrayList<Integer> copy = new ArrayList<>(boxed);     // mutable copy
    }
}
```

Internals: grows by ~1.5x (`old + old>>1`) with `System.arraycopy` when full; `ensureCapacity(n)` pre-sizes to avoid copies; `trimToSize()` releases slack. Fail-fast iterator via `modCount` → ConcurrentModificationException on structural change.

## LinkedList - list AND deque

```java title=LinkedListDemo.java
import java.util.*;

public class LinkedListDemo {
    public static void main(String[] args) {
        LinkedList<String> l = new LinkedList<>(List.of("b", "d"));

        // as a List
        l.addFirst("a"); l.addLast("e");                 // O(1) ends
        l.add(2, "c");                                   // O(n) to walk there
        String head = l.peekFirst();                     // null if empty (no throw)
        String tail = l.pollLast();                      // remove+return, null if empty

        // as a Deque (double-ended queue) - also used as a stack
        l.push("z");                                     // stack push (addFirst)
        String top = l.pop();                            // stack pop (removeFirst)

        // queue behavior: offer/poll/peek on a LinkedList are O(1)
        l.offer("q"); l.poll(); l.peek();

        System.out.println(l);
        // RandomAccess? NO - binary search on LinkedList would be a mistake
        System.out.println(l instanceof RandomAccess);   // false
    }
}
```

Pick ArrayList unless you have a measured reason: frequent add/remove **at the ends** (use it as Deque instead - ArrayDeque is faster), or LinkedList-specific iterator insert/remove in the middle of huge lists.

## Vector & Stack (legacy - know to recognize)

```java title=Legacy.java
import java.util.*;

public class Legacy {
    public static void main(String[] args) {
        Vector<String> v = new Vector<>(List.of("x", "y"));  // synchronized methods
        v.addElement("z");                                    // old API name
        Enumeration<String> e = v.elements();                 // pre-Iterator traversal

        Stack<Integer> st = new Stack<>();                    // extends Vector
        st.push(1); st.push(2);
        int top = st.pop();                                   // LIFO
        int peeked = st.peek();
        int idx = st.search(1);                               // distance from top (1-based)
        System.out.println(top + " " + peeked + " " + idx);
        // modern replacement: Deque<Integer> d = new ArrayDeque<>(); d.push/pop/peek
    }
}
```

Why not new code: unsized growth hurts, synchronized-everything wastes uncontended locks, `Enumeration` API, `Stack.search()` oddities. Use `ArrayDeque` (stack/queue) or `ArrayList` (list).

## CopyOnWriteArrayList - the concurrent List

```java title=COWList.java
import java.util.concurrent.CopyOnWriteArrayList;

public class COWList {
    public static void main(String[] args) {
        CopyOnWriteArrayList<String> cow =
            new CopyOnWriteArrayList<>(List.of("a", "b"));

        cow.add("c");                 // full copy of the array per write
        // iteration never throws CME - it walks the snapshot taken at creation
        for (String s : cow) {
            cow.add("late");          // allowed: iterator unaffected
        }
        System.out.println(cow);      // [a, b, c, late]
    }
}
```

Characteristics: writes O(n) copy + CAS of the backing reference; reads O(1) lock-free. Ideal: listener lists, config sets - **read-mostly, tiny write rate**. Terrible for big frequently-mutated lists.

## Choosing in practice

```text title=decision
need index get / iterate a lot ..............> ArrayList
need stack/queue ends .......................> ArrayDeque
need queue with priority ....................> PriorityQueue
frequent add/remove at ends, few gets .......> ArrayDeque (or LinkedList as deque)
legacy code / synchronized Vector ...........> understand it; replace when touching
snapshot iteration, read-mostly shared ......> CopyOnWriteArrayList
huge list with random access ................> ArrayList + ensureCapacity (never LinkedList)
```

Related: [Collections overview](collections.html) · [Set implementations](collections-set.html) · [Queue & Deque](collections-queue.html) · [Map](collections-map.html) · [ArrayList/LinkedList examples in the archive](collections-appendthegivenobjecttothegivenarray.html)
