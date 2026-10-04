---
title: Java ArrayList
nav: ArrayList
description: ArrayList in depth - add, remove, search, sort, iterate and avoid common mistakes.
section: Collections
order: 20
---

## ArrayList - the default list

`ArrayList` is a resizable array. It implements `List` and is the most-used collection in Java:

- **Fast reads** by index - O(1)
- **Amortized O(1)** appends
- Slower inserts/removals in the middle (elements shift)
- Not synchronized (single-threaded by default)

```java title=Create.java
import java.util.ArrayList;
import java.util.List;

public class Create {
    public static void main(String[] args) {
        ArrayList<String> a = new ArrayList<>();      // empty, capacity grows as needed
        List<String> b = new ArrayList<>(List.of("x", "y"));  // program to the interface
        ArrayList<Integer> c = new ArrayList<>(20);   // initial capacity hint

        a.add("first");
        a.add("second");
        System.out.println(a);        // [first, second]
        System.out.println(a.size()); // 2
        System.out.println(a.isEmpty());
    }
}
```

> **Note:** `new ArrayList<>(20)` only sets *capacity*; `new ArrayList<>(List.of(...))` copies a list. Two different constructors!

## Adding and replacing

```java title=Add.java
import java.util.ArrayList;
import java.util.List;

public class Add {
    public static void main(String[] args) {
        List<String> list = new ArrayList<>(List.of("b", "d"));

        list.add("e");                 // append -> [b, d, e]
        list.add(0, "a");              // insert at index 0 -> [a, b, d, e]
        list.addAll(List.of("f", "g")); // append many
        list.set(2, "c");              // REPLACE index 2 (does not shift)
        System.out.println(list);      // [a, b, c, e, f, g]
    }
}
```

`add(index, x)` **inserts and shifts**; `set(index, x)` **overwrites in place**. Mixing them up is a classic off-by-shift bug.

## Removing elements

```java title=Remove.java
import java.util.ArrayList;
import java.util.List;

public class Remove {
    public static void main(String[] args) {
        List<Integer> nums = new ArrayList<>(List.of(10, 20, 30, 20, 40));

        nums.remove(1);                 // by INDEX -> removes 20 (value at index 1)
        System.out.println(nums);       // [10, 30, 20, 40]

        nums.remove(Integer.valueOf(20)); // by OBJECT -> removes first 20
        System.out.println(nums);       // [10, 30, 40]

        nums.removeIf(n -> n > 35);     // remove all matching (Java 8+)
        System.out.println(nums);       // [10, 30]
    }
}
```

> **Warning:** On `List<Integer>`, `remove(1)` means *index 1*. To remove the value `1`, box it: `remove(Integer.valueOf(1))`. On `List<String>` this trap doesn't exist (only `remove(int)` vs `remove(Object)` overloads).

## Accessing and searching

```java title=Access.java
import java.util.List;

public class Access {
    public static void main(String[] args) {
        List<String> names = new java.util.ArrayList<>(List.of("amy", "bob", "cy", "bob"));

        System.out.println(names.get(0));              // amy
        System.out.println(names.indexOf("bob"));      // 1 (first)
        System.out.println(names.lastIndexOf("bob"));  // 3
        System.out.println(names.contains("cy"));      // true
        System.out.println(names.subList(1, 3));       // [bob, cy] (end exclusive)
        System.out.println(names.toArray().length);    // backing array view
    }
}
```

`get()` on an invalid index throws `IndexOutOfBoundsException` - always loop to `size() - 1`.

## Iterating (the safe ways)

```java title=Iterate.java
import java.util.ArrayList;
import java.util.List;

public class Iterate {
    public static void main(String[] args) {
        List<String> names = new ArrayList<>(List.of("ana", "bo", "chi", "di"));

        // for-each
        for (String n : names) System.out.println(n);

        // remove while iterating - use removeIf (safe, concise)
        names.removeIf(n -> n.length() <= 2);
        System.out.println(names);        // [chi]

        // index loop when you need positions
        for (int i = 0; i < names.size(); i++) {
            System.out.println(i + "=" + names.get(i));
        }
    }
}
```

## Sorting and copying

```java title=SortCopy.java
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class SortCopy {
    public static void main(String[] args) {
        List<Integer> nums = new ArrayList<>(List.of(5, 3, 8, 1));

        Collections.sort(nums);                                  // in place
        System.out.println(nums);                                // [1, 3, 5, 8]

        nums.sort(Collections.reverseOrder());
        System.out.println(nums);                                // [8, 5, 3, 1]

        List<Integer> copy = new ArrayList<>(nums);              // shallow copy
        copy.add(99);
        System.out.println(nums);                                // unchanged
        System.out.println(copy);
    }
}
```

## Common patterns

```java title=Patterns.java
import java.util.ArrayList;
import java.util.List;

public class Patterns {
    public static void main(String[] args) {
        List<String> tasks = new ArrayList<>();

        // guard against nulls and blanks at the boundary
        addTask(tasks, "write code");
        addTask(tasks, "   ");
        addTask(tasks, null);
        System.out.println(tasks);                       // [write code]

        // transform into a new list
        List<Integer> lengths = new ArrayList<>();
        for (String t : tasks) lengths.add(t.length());
        System.out.println(lengths);

        // same with streams (preferred)
        List<Integer> lengths2 = tasks.stream().map(String::length).toList();
        System.out.println(lengths2);
    }

    static void addTask(List<String> list, String task) {
        if (task == null || task.isBlank()) return;
        list.add(task.trim());
    }
}
```

## ArrayList vs LinkedList vs Vector

| | ArrayList | LinkedList | Vector |
|---|---|---|---|
| Get by index | **O(1)** | O(n) | O(1) |
| Add at end | **amortized O(1)** | O(1) | O(1) |
| Add/remove at head | O(n) | **O(1)** | O(n) |
| Memory overhead | low | higher (node links) | low + legacy sync |
| Verdict | **default** | rare (use `ArrayDeque` for ends) | avoid in new code |

Real-world rule: almost always `ArrayList`. Even iteration is usually faster than `LinkedList` because of cache locality.

> **Remember:** An `ArrayList` is *not* thread-safe. Share it across threads only via `Collections.synchronizedList` or `CopyOnWriteArrayList`.

Next: [HashMap](hashmap.html) - fast key-value lookups.
