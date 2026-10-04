---
title: Java Strings
nav: Strings
description: Create, concatenate, search, split, format and compare strings - plus immutability and the string pool.
section: Java Basics
order: 50
---

## Strings are objects

A `String` is a sequence of characters - but in Java it is an **object**, and it is **immutable**: once created, its value can never change. Every "modification" returns a *new* String.

```java title=HelloString.java
public class HelloString {
    public static void main(String[] args) {
        String greeting = "Hello";
        String who = "Java";

        // concatenation creates a NEW string
        String message = greeting + ", " + who + "!";
        System.out.println(message);   // Hello, Java!
        System.out.println(greeting);  // Hello - unchanged
    }
}
```

## Creating strings

```java title=Create.java
public class Create {
    public static void main(String[] args) {
        String a = "Hi";                 // string literal (pool)
        String b = new String("Hi");     // new object on the heap
        char[] chars = {'H', 'i'};
        String c = new String(chars);    // from a char array

        System.out.println(a.equals(b)); // true  - same content
        System.out.println(a == b);      // false - different objects
    }
}
```

### The string pool

The JVM keeps a pool of unique literals. `a = "Hi"` points into the pool; `new String("Hi")` makes a fresh copy. That's why:

```java title=Pool.java
public class Pool {
    public static void main(String[] args) {
        String x = "java";
        String y = "java";
        String z = new String("java");

        System.out.println(x == y);   // true  - both in the pool
        System.out.println(x == z);   // false - z is a separate object
        System.out.println(x.equals(z)); // true
    }
}
```

> **Remember:** Always compare string **content** with `equals()` (or `equalsIgnoreCase()`), never with `==`.

## Essential methods

```java title=Methods.java
public class Methods {
    public static void main(String[] args) {
        String s = "  Learn Java the right way  ";

        System.out.println(s.trim());              // remove leading/trailing spaces
        System.out.println(s.length());            // 27
        System.out.println(s.toUpperCase());       // LEARN JAVA...
        System.out.println(s.toLowerCase());       // learn java...
        System.out.println(s.contains("Java"));    // true
        System.out.println(s.indexOf("Java"));     // 7 (position)
        System.out.println(s.startsWith("  Learn"));// true
        System.out.println(s.endsWith("way  "));   // true
        System.out.println(s.charAt(2));           // 'L'
        System.out.println(s.replace('a', '4'));   // L4earn j4v4...
        System.out.println(s.isEmpty());           // false
    }
}
```

### Extracting parts

```java title=Slicing.java
public class Slicing {
    public static void main(String[] args) {
        String file = "report-2026-final.pdf";

        System.out.println(file.substring(7));          // 2026-final.pdf
        System.out.println(file.substring(7, 11));      // 2026  (start, end-exclusive)

        int dot = file.lastIndexOf('.');
        System.out.println(file.substring(dot + 1));    // pdf

        System.out.println("abc".charAt(0));            // a
    }
}
```

### Splitting and joining

```java title=SplitJoin.java
public class SplitJoin {
    public static void main(String[] args) {
        String csv = "apple,banana,cherry";
        String[] parts = csv.split(",");
        for (String p : parts) {
            System.out.println("fruit: " + p);
        }

        String joined = String.join(" | ", parts);
        System.out.println(joined);   // apple | banana | cherry

        String multi = "one two\tthree";
        System.out.println(java.util.Arrays.toString(multi.split("\\s+")));
    }
}
```

## Building text efficiently

Because strings are immutable, concatenating in a loop creates garbage. Use `StringBuilder`:

```java title=Build.java
public class Build {
    public static void main(String[] args) {
        // bad: creates a new string every iteration
        String slow = "";
        for (int i = 0; i < 5; i++) {
            slow += i + " ";
        }

        // good: one mutable buffer
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 5; i++) {
            sb.append(i).append(' ');
        }
        sb.append("| done");

        System.out.println(slow.trim());
        System.out.println(sb.toString().trim());
        System.out.println(new StringBuilder("race").reverse()); // ecar
    }
}
```

> **Tip:** In loops, always prefer `StringBuilder`. For a handful of `+` in normal code, the compiler optimizes it for you.

## Formatting with `String.format`

```java title=Format.java
public class Format {
    public static void main(String[] args) {
        String name = "Anil";
        double price = 49.5;
        int qty = 3;

        String line = String.format("%-10s | %8.2f | x%d", name, price, qty);
        System.out.println(line);

        System.out.printf("Total: %.2f%n", price * qty);
        System.out.printf("%,d%n", 1000000);        // 1,000,000
        System.out.printf("%05d%n", 42);            // 00042
        System.out.printf("%h-%h%n", "AB", "cd");   // locale-aware case
    }
}
```

Common format specifiers: `%s` string, `%d` integer, `%f` decimal, `%b` boolean, `%c` char, `%n` newline. Add flags between `%` and the letter (`-` left align, `,` grouping, `0` padding, `.2` precision).

## Comparing strings

```java title=Compare.java
public class Compare {
    public static void main(String[] args) {
        String a = "java", b = "Java";

        System.out.println(a.equals(b));            // false
        System.out.println(a.equalsIgnoreCase(b));  // true

        System.out.println("apple".compareTo("banana")); // negative - apple < banana
        System.out.println("apple".compareToIgnoreCase("APPLE")); // 0

        String t = "  pad  ";
        System.out.println(t.strip().isEmpty());    // true (strip() = Java 11+)
    }
}
```

To sort strings ignoring case, use `String.CASE_INSENSITIVE_ORDER`.

## Strings and numbers

```java title=Conversions.java
public class Conversions {
    public static void main(String[] args) {
        int n = Integer.parseInt("42");
        double d = Double.parseDouble("3.14");
        long l = Long.parseLong("1234567890123");

        String fromInt = String.valueOf(n);      // "42"
        String fromConcat = "" + d;              // "3.14" (simple but lazy)

        System.out.println(n + d + " " + fromInt + " " + fromConcat);
    }
}
```

For parsing with failure handling, prefer the safe variants that return `Optional`/default instead of throwing:

```java title=SafeParse.java
public class SafeParse {
    public static void main(String[] args) {
        String input = "12a";
        try {
            int v = Integer.parseInt(input);
            System.out.println(v);
        } catch (NumberFormatException e) {
            System.out.println("Not a number: " + input);
        }
    }
}
```

## Immutability - why it matters

- Strings can be **shared safely** between threads with no locking.
- They work as reliable **map keys** - their hash code never changes.
- The downside: repeated modifications should use `StringBuilder` instead.

Full method list: [String reference](string-methods.html).

Next: [Conditions](conditionals.html) - making decisions in code.
