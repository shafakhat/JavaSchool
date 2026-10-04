---
title: Java Reflection
nav: Reflection
description: Inspect classes at runtime with the reflection API - fields, methods, constructors and dynamic invocation.
section: Advanced Java
order: 30
---

## What reflection is

Reflection lets a program **inspect and modify itself at runtime**: discover classes, read fields, invoke methods and create objects - even when the exact type isn't known at compile time.

Powerful, but with costs: slower than direct calls, breaks encapsulation, and refactoring tools can't see string-based names. Use it for frameworks (DI, ORMs, serializers), not everyday code.

## Class objects - three ways

```java title=ClassObjects.java
import java.util.ArrayList;

public class ClassObjects {
    public static void main(String[] args) {
        Class<?> a = ArrayList.class;                 // 1. class literal (no object needed)
        ArrayList<String> list = new ArrayList<>();
        Class<?> b = list.getClass();                 // 2. from an instance
        try {
            Class<?> c = Class.forName("java.util.ArrayList");  // 3. by name (dynamic!)
            System.out.println(a == b && b == c);     // true - all the same Class
        } catch (ClassNotFoundException e) {
            System.out.println(e.getMessage());
        }
    }
}
```

## Inspecting fields and methods

```java title=Inspect.java
import java.lang.reflect.Field;
import java.lang.reflect.Method;

public class Inspect {
    public static void main(String[] args) throws Exception {
        Class<?> cls = Class.forName("java.lang.String");

        System.out.println("== fields ==");
        for (Field f : cls.getDeclaredFields()) {
            System.out.println("  " + f.getType().getSimpleName() + " " + f.getName());
        }

        System.out.println("== a few methods ==");
        int shown = 0;
        for (Method m : cls.getDeclaredMethods()) {
            System.out.println("  " + m.getReturnType().getSimpleName() + " " + m.getName()
                + "(" + m.getParameterCount() + ")");
            if (++shown >= 5) break;
        }

        // ask directly
        Method len = cls.getMethod("length");
        System.out.println("length() exists, returns " + len.getReturnType().getSimpleName());
    }
}
```

## Invoking methods and creating objects dynamically

```java title=Invoke.java
import java.lang.reflect.Constructor;
import java.lang.reflect.Method;

public class Invoke {
    public static void main(String[] args) throws Exception {
        // compile-time unknown type: comes in as a String name
        Class<?> cls = Class.forName("java.lang.StringBuilder");

        // create an instance (no-arg constructor)
        Constructor<?> ctor = cls.getConstructor(String.class);
        Object sb = ctor.newInstance("start-");

        // call methods reflectively
        Method append = cls.getMethod("append", String.class);
        Method toString = cls.getMethod("toString");
        Object after = append.invoke(sb, "done");      // returns the same builder
        System.out.println(toString.invoke(after));    // start-done
    }
}
```

`invoke(target, args...)` throws `InvocationTargetException` wrapping any exception thrown by the called method - unwrap it with `getCause()`.

## Reading a class's structure generically

```java title=Structure.java
import java.lang.reflect.Modifier;

public class Structure {
    static class Account {
        private String owner;
        private double balance;

        public Account(String owner, double balance) {
            this.owner = owner;
            this.balance = balance;
        }

        public void deposit(double amount) { balance += amount; }
    }

    public static void main(String[] args) {
        Class<?> c = Account.class;
        System.out.println("class " + c.getSimpleName()
            + (Modifier.isAbstract(c.getModifiers()) ? " (abstract)" : ""));

        for (var f : c.getDeclaredFields()) {
            String vis = Modifier.isPrivate(f.getModifiers()) ? "private" : "public";
            System.out.println("  field  " + vis + " " + f.getType().getSimpleName() + " " + f.getName());
        }
        for (var m : c.getDeclaredMethods()) {
            System.out.println("  method " + m.getName() + "() -> " + m.getReturnType().getSimpleName());
        }
        for (var ctor : c.getDeclaredConstructors()) {
            System.out.println("  ctor(" + ctor.getParameterCount() + " params)");
        }
    }
}
```

## Reaching private members (and why to think twice)

```java title=BreakIn.java
import java.lang.reflect.Field;

public class BreakIn {
    static class Vault {
        private String secret = "hidden";
    }

    public static void main(String[] args) throws Exception {
        Vault v = new Vault();
        Field f = Vault.class.getDeclaredField("secret");
        f.setAccessible(true);                    // defeat private access (opens module warnings in modern Java)
        System.out.println(f.get(v));             // hidden
        f.set(v, "changed");
        System.out.println(f.get(v));             // changed
    }
}
```

On JDK 17+ reflective access to other modules' internals is strongly restricted (`InaccessibleObjectException`). Within your own code, prefer normal APIs.

## Where reflection is used

| Framework | Uses reflection for |
|---|---|
| Spring / Guice | dependency injection, `@Autowired` wiring |
| JPA/Hibernate | instantiating entities, mapping columns |
| Jackson/Gson | serializing fields, calling setters |
| JUnit | discovering `@Test` methods |
| `equals`/`hashCode` codegen, `records` tooling | introspection |

> **Remember:** reflection trades compile-time safety for runtime flexibility - a typo in `"getBalance"` is a `NoSuchMethodException` at runtime, not a red underline. Keep reflective names in constants and fail fast at startup.

Next: [Design Patterns](design-patterns.html).
