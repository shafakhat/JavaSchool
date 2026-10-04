---
title: Java Generics
nav: Generics
description: Write type-safe reusable classes and methods with type parameters, bounded types and wildcards.
section: Core Java
order: 60
---

## Why generics?

Before generics, collections stored `Object` and you cast blindly - typos only exploded at runtime:

```text title=Generics vs raw types
raw (pre-1.5):  list.add("text");  int n = (Integer) list.get(0);  // ClassCastException at RUNTIME
generics:       List<String> l;    String s = l.get(0);            // won't even compile if wrong
```

Generics move bugs from **runtime to compile time**.

## Generic classes

```java title=Box.java
public class Box<T> {               // T = type parameter (a placeholder)
    private T value;

    public void set(T value) { this.value = value; }
    public T get() { return value; }

    public static void main(String[] args) {
        Box<String> text = new Box<>();
        text.set("hello");
        System.out.println(text.get().length());   // String methods available - no cast!

        Box<Integer> num = new Box<>();
        num.set(42);
        System.out.println(num.get() + 1);         // 43
        // num.set("nope");                        // ERROR at compile time
    }
}
```

`<T>` is just a placeholder name - convention uses single letters:

| Letter | Meaning |
|---|---|
| `T` | Type |
| `E` | Element (collections) |
| `K` / `V` | Key / Value (maps) |
| `R` | Return |

## Multiple type parameters

```java title=Pair.java
public class Pair<K, V> {
    private final K key;
    private final V value;

    public Pair(K key, V value) {
        this.key = key;
        this.value = value;
    }

    public K getKey() { return key; }
    public V getValue() { return value; }

    @Override
    public String toString() {
        return key + "=" + value;
    }

    public static void main(String[] args) {
        Pair<String, Integer> p = new Pair<>("age", 30);
        Pair<Integer, Boolean> q = new Pair<>(7, true);
        System.out.println(p + " | " + q);
        int age = p.getValue() + 1;      // typed as Integer - unboxes fine
        System.out.println(age);
    }
}
```

## Generic methods

The type parameter goes **before** the return type:

```java title=GenericMethod.java
import java.util.List;

public class GenericMethod {
    static <T> T first(List<T> list) {           // generic method
        if (list.isEmpty()) throw new java.util.NoSuchElementException("empty");
        return list.get(0);
    }

    static <K, V> String describe(java.util.Map<K, V> map) {
        return map.size() + " entries";
    }

    public static void main(String[] args) {
        System.out.println(first(List.of(10, 20, 30)));      // 10 (T = Integer)
        System.out.println(first(List.of("a", "b")));        // a  (T = String)
        System.out.println(describe(java.util.Map.of("k", 1)));
    }
}
```

The compiler **infers** `T` from the argument - you rarely write `<T>` at the call site.

## Bounded type parameters

Constrain `T` so you can *use* its members:

```java title=Bounded.java
public class Bounded {
    // T must be a Number - so we can call .doubleValue()
    static double sum(java.util.List<? extends Number> nums) {
        double s = 0;
        for (Number n : nums) s += n.doubleValue();
        return s;
    }

    static <T extends Comparable<T>> T maxOf(T a, T b) {
        return a.compareTo(b) >= 0 ? a : b;
    }

    public static void main(String[] args) {
        System.out.println(sum(java.util.List.of(1, 2.5, 3L)));   // 6.5
        System.out.println(maxOf("apple", "banana"));             // banana
        System.out.println(maxOf(10, 20));                        // 20
        // System.out.println(maxOf("x", 5));                     // ERROR: types differ
    }
}
```

You can stack bounds: `<T extends Number & Comparable<T>>` - classes first, interfaces after.

## Wildcards

| Wildcard | Means | Use when |
|---|---|---|
| `?` | any type | rare on its own |
| `? extends T` | T or a subtype | you only **read** (producer) |
| `? super T` | T or a supertype | you only **write** (consumer) |

```java title=Wildcards.java
import java.util.List;

public class Wildcards {
    static void printAll(List<?> list) {                 // read-only view of any list
        for (Object o : list) System.out.println(o);
    }

    static void addAll(List<? super Integer> list) {     // can add Integers
        list.add(1);
        list.add(2);
    }

    static int sum(List<? extends Number> list) {        // can read Numbers
        int s = 0;
        for (Number n : list) s += n.intValue();
        return s;
    }

    public static void main(String[] args) {
        printAll(List.of("a", "b"));
        printAll(List.of(1, 2));

        java.util.ArrayList<Integer> ints = new java.util.ArrayList<>();
        addAll(ints);
        System.out.println(ints);

        System.out.println(sum(List.of(1, 2, 3)));
        System.out.println(sum(List.of(1.5, 2.5)));
    }
}
```

The PECS rule from Effective Java: **Producer Extends, Consumer Super**.

## Generic collections in the wild

```java title=WildCollections.java
import java.util.*;

public class WildCollections {
    public static void main(String[] args) {
        List<String> names = new ArrayList<>(List.of("zoe", "amy"));

        Collections.sort(names);                   // sorts List<String>
        System.out.println(names);

        Map<String, List<String>> index = new HashMap<>();
        index.computeIfAbsent("fruit", k -> new ArrayList<>()).add("apple");
        index.computeIfAbsent("fruit", k -> new ArrayList<>()).add("pear");
        System.out.println(index);

        Optional<String> first = names.stream().findFirst();
        first.ifPresent(System.out::println);
    }
}
```

## Type erasure - the historic compromise

Generics are implemented by **erasure**: the compiler checks types, then mostly throws the `<T>` away in bytecode (for backward compatibility with Java 1.4).

Consequences:

```java title=Erasure.java
import java.util.ArrayList;
import java.util.List;

public class Erasure {
    public static void main(String[] args) {
        // 1) no generics at runtime - you cannot ask for T.class
        // Class<T> c = T.class;                    // ERROR

        List<String> a = new ArrayList<>();
        List<Integer> b = new ArrayList<>();
        System.out.println(a.getClass() == b.getClass());   // true - both are ArrayList

        // 2) cannot create arrays of a type parameter
        // T[] arr = new T[10];                     // ERROR

        // 3) instanceof with generics is unchecked
        if (a instanceof List<?> any) {           // wildcard is fine
            System.out.println("a list of something: " + any.size());
        }
    }
}
```

Workarounds: pass `Class<T>` as a parameter, use arrays of the bound type, or prefer `instanceof List<?>`.

> **Remember:** Generics give you compile-time safety with no runtime cost (by erasure) - but also no `T.class`, no `new T[]`, and no generic arrays.

Next: [Collections](collections.html) - the data structures that use generics everywhere.
