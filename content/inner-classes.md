---
title: Java Inner Classes
nav: Inner Classes
description: Inner (member), local and anonymous classes plus a first look at lambda replacements.
section: Object Oriented
order: 90
---

## Four kinds of nested classes

| Kind | Declared | Has reference to outer? | Typical use |
|---|---|---|---|
| **Static nested** | `static class` inside a class | no | helper grouped with its parent |
| **Inner (member)** | inside a class, no `static` | yes | tightly coupled helper objects |
| **Local** | inside a method | yes (effectively final) | one-off helper |
| **Anonymous** | `new X() { ... }` | yes | callbacks, quick implementations |

## Inner classes

An inner class instance is **tied to an outer instance** - it can read the outer's fields directly:

```java title=Inner.java
public class Inner {
    private String brand = "Omega";

    class Watch {
        private String model = "Solar-X";

        void show() {
            // outer field + inner field together
            System.out.println(brand + " / " + model);
        }
    }

    Watch makeWatch() {
        return new Watch();      // created with an implicit reference to this
    }

    public static void main(String[] args) {
        Inner outer = new Inner();
        Inner.Watch w = outer.new Watch();   // note the outer-dot syntax
        w.show();

        outer.makeWatch().show();
    }
}
```

```text title=Output
Omega / Solar-X
Omega / Solar-X
```

The compiler secretly stores a reference `this$0` in the inner class - that's why inner classes can reach the outer object's state.

## Local classes

Defined inside a method; visible only there:

```java title=Local.java
public class Local {
    interface Greeting {
        void hi(String who);
    }

    static Greeting makeGreeting(String punctuation) {
        class Polite implements Greeting {       // local class
            @Override
            public void hi(String who) {
                System.out.println("Hello, " + who + punctuation);
            }
        }
        return new Polite();
    }

    public static void main(String[] args) {
        makeGreeting("!").hi("Ada");
        makeGreeting("?").hi("Ada");
    }
}
```

Local classes can capture **effectively final** local variables of the enclosing method.

## Anonymous classes

Define-and-instantiate in one expression - ideal for one-off implementations:

```java title=Anonymous.java
public class Anonymous {
    interface Executor {
        void run(int n);
    }

    static void execute(int n, Executor e) {
        e.run(n);
    }

    public static void main(String[] args) {
        execute(5, new Executor() {                 // class defined on the spot
            @Override
            public void run(int n) {
                System.out.println("running with " + n);
            }
        });

        // variations of the same idea:
        Runnable r = new Runnable() {
            @Override
            public void run() { System.out.println("anonymous runnable"); }
        };
        r.run();

        String[] names = {"bee", "cat"};
        java.util.Arrays.sort(names, new java.util.Comparator<String>() {
            @Override
            public int compare(String a, String b) {
                return b.length() - a.length();      // sort by length desc
            }
        });
        System.out.println(java.util.Arrays.toString(names));
    }
}
```

```text title=Output
running with 5
anonymous runnable
[cat, bee]
```

## Lambdas replace anonymous classes (Java 8+)

When the anonymous class implements a **functional interface** (one abstract method), a lambda does the same job with far less noise:

```java title=LambdaVsAnon.java
public class LambdaVsAnon {
    interface Op { int apply(int a, int b); }

    static int compute(int a, int b, Op op) { return op.apply(a, b); }

    public static void main(String[] args) {
        // anonymous class (pre-Java-8 style)
        int r1 = compute(3, 4, new Op() {
            @Override
            public int apply(int a, int b) { return a + b; }
        });

        // lambda (Java 8+)
        int r2 = compute(3, 4, (a, b) -> a * b);

        System.out.println(r1 + " " + r2);   // 7 12
    }
}
```

| | Anonymous class | Lambda |
|---|---|---|
| `this` | refers to *itself* | refers to enclosing instance |
| Can have fields/state | yes | no (stateless) |
| Verbosity | high | minimal |
| Requirement | any abstract type | functional interface only |

## Serialization caveat

Inner and anonymous classes hold a hidden reference to the outer object - be careful when serializing them, or when the outer object is huge:

```java title=Capture.java
public class Capture {
    String prefix = "id=";

    Runnable makeTask(int n) {
        // captures the outer Capture object AND n
        return () -> System.out.println(prefix + n);
    }

    public static void main(String[] args) {
        Capture c = new Capture();
        Runnable task = c.makeTask(42);
        task.run();      // id=42
    }
}
```

> **Tip:** If the nested class doesn't need the outer instance, make it `static` - it's cheaper and avoids accidentally retaining the outer object (a classic memory-leak source).

Next: [Exceptions](exceptions.html) - surviving things that go wrong.
