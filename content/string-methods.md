---
title: Java String Methods Reference
nav: String Methods
description: Complete reference of common String methods with examples - searching, transforming, splitting and formatting.
section: Reference
order: 20
---

## At a glance

All methods return a **new** String unless noted - the original never changes (strings are immutable).

### Checking

| Method | Returns | Example (`s = "JavaRules"`) |
|---|---|---|
| `isEmpty()` | no characters? | `false` |
| `isBlank()` | only whitespace? (Java 11+) | `false` |
| `length()` | character count | `9` |
| `equals(o)` | exact match | `"JavaRules".equals(s)` -> `true` |
| `equalsIgnoreCase(o)` | match ignoring case | `true` for `"javarules"` |
| `startsWith(p)` / `endsWith(p)` | prefix / suffix | `startsWith("Java")` -> `true` |
| `contains(c)` | substring present? | `contains("Rules")` -> `true` |
| `indexOf(c)` / `lastIndexOf(c)` | position or `-1` | `indexOf("Rules")` -> `4` |
| `compareTo(o)` | sort order (0 = equal) | `s.compareTo("A")` > 0 |
| `matches(regex)` | full regex match | `"123".matches("\\d+")` -> `true` |

```java title=Check.java
public class Check {
    public static void main(String[] args) {
        String s = "JavaRules";
        System.out.println(s.isEmpty());                 // false
        System.out.println(s.isBlank());                 // false
        System.out.println(s.length());                  // 9
        System.out.println(s.equals("JavaRules"));       // true
        System.out.println(s.equalsIgnoreCase("javarules")); // true
        System.out.println(s.startsWith("Java"));        // true
        System.out.println(s.endsWith("Rules"));         // true
        System.out.println(s.contains("vaRu"));          // true
        System.out.println(s.indexOf("Rules"));          // 4
        System.out.println(s.indexOf("zz"));             // -1
    }
}
```

### Transforming

| Method | Effect |
|---|---|
| `toUpperCase()` / `toLowerCase()` | case change (locale-aware overloads exist) |
| `trim()` | remove ASCII whitespace from both ends |
| `strip()` / `stripLeading()` / `stripTrailing()` | remove all whitespace (Java 11+, better for Unicode) |
| `replace(a, b)` | replace every literal `a` with `b` |
| `replaceAll(regex, repl)` | regex replace |
| `replaceFirst(regex, repl)` | replace first regex match |
| `concat(s2)` | same as `+` |
| `repeat(n)` | concatenate n times (Java 11+) |
| `indent(n)` | adjust indentation (Java 12+) |
| `stripTrailing()` | remove trailing whitespace (Java 11+) |

For reversing, there is no `String.reverse()` - use `new StringBuilder(s).reverse().toString()`.

```java title=Transform.java
public class Transform {
    public static void main(String[] args) {
        String s = "  hello world  ";
        System.out.println("[" + s.trim() + "]");           // [hello world]
        System.out.println("[" + s.strip() + "]");          // [hello world]
        System.out.println("JAVA".toLowerCase());           // java
        System.out.println("a-b-c".replace('-', '+'));      // a+b+c
        System.out.println("a1b2c".replaceAll("\\d", "#")); // a#b#c
        System.out.println("ab".repeat(3));                 // ababab
        System.out.println(new StringBuilder("mirror").reverse()); // rorrim
    }
}
```

### Extracting and splitting

| Method | Returns |
|---|---|
| `charAt(i)` | char at index |
| `substring(begin)` | from index to end |
| `substring(begin, end)` | `[begin, end)` |
| `chars()` | IntStream of code points (Java 8+) |
| `split(regex)` | `String[]` |
| `split(regex, limit)` | controlled split count |
| `lines()` | Stream of lines (Java 11+) |
| `toCharArray()` | `char[]` copy |

```java title=Extract.java
import java.util.Arrays;

public class Extract {
    public static void main(String[] args) {
        String s = "learn-java-the-fun-way";
        System.out.println(s.charAt(0));                 // l
        System.out.println(s.substring(6));              // java-the-fun-way
        System.out.println(s.substring(6, 10));          // java
        System.out.println(Arrays.toString(s.split("-")));  // [learn, java, ...]
        System.out.println(s.split("-", 2)[1]);          // java-the-fun-way (limit)

        "a\nb\nc".lines().forEach(l -> System.out.println(">" + l));
        System.out.println("abc".toCharArray().length);  // 3
    }
}
```

### Converting and formatting

| Method | Returns |
|---|---|
| `String.valueOf(x)` | string form of any primitive/object |
| `formatted(args)` / `String.format(fmt, args)` | formatted string |
| `intern()` | pooled canonical version |
| `getBytes(charset)` | byte array |
| `Numeric` classes `parseInt/parseLong/parseDouble` | parse from string |

```java title=Format.java
public class Format {
    public static void main(String[] args) {
        System.out.println(String.valueOf(42) + " " + String.valueOf(3.14));
        System.out.printf("%,d%n", 1234567);            // 1,234,567
        System.out.printf("%-8s|%8.2f|%n", "tea", 45.5); // aligned columns
        System.out.println("Item x%d".formatted(3));    // Item x3
        System.out.println(Integer.parseInt("42") + 1); // 43
    }
}
```

### Text blocks (Java 15+)

```java title=TextBlock.java
public class TextBlock {
    public static void main(String[] args) {
        String json = """
                {
                    "name": "Ada",
                    "age": 36
                }
                """;
        System.out.println(json);
        System.out.println(json.strip().startsWith("{"));  // true
    }
}
```

Triple quotes preserve line breaks and indentation cleanly - far nicer than `\n` chains.

## Common recipes

```java title=Recipes.java
import java.util.Arrays;
import java.util.stream.Collectors;

public class Recipes {
    public static void main(String[] args) {
        String csv = " apple , banana ,, cherry ";

        // split + trim + drop blanks
        var items = Arrays.stream(csv.split(","))
            .map(String::trim)
            .filter(s -> !s.isEmpty())
            .toList();
        System.out.println(items);                        // [apple, banana, cherry]

        // capitalize first letter
        String word = "java";
        String capped = Character.toUpperCase(word.charAt(0)) + word.substring(1);
        System.out.println(capped);                       // Java

        // check blank input safely
        String input = "   ";
        System.out.println(input == null || input.isBlank() ? "(empty)" : input);

        // hide middle of an identifier
        String account = "1234567890";
        String masked = account.substring(0, 3) + "*".repeat(account.length() - 6)
                       + account.substring(account.length() - 3);
        System.out.println(masked);                       // 123******90

        // count occurrences
        String hay = "the cat and the hat";
        long count = hay.chars().filter(c -> c == 't').count();
        System.out.println("t count = " + count);

        // join a list
        System.out.println(items.stream().map(String::toUpperCase)
            .collect(Collectors.joining(" | ")));
    }
}
```

## Performance notes

- Concatenating in a loop? Use `StringBuilder` (or `String.join` / streams at the end).
- `indexOf`/`contains` are fast; `matches(regex)` compiles the pattern each call - precompile with `Pattern.compile` if reused.
- `"a" + "b"` of constants is folded at compile time; everything else creates objects.

See also: [Strings tutorial](strings.html) · [Keywords](keywords.html) · [Useful classes](java-api.html)
