---
title: Java Regular Expressions
nav: Regular Expressions
description: Pattern, Matcher and the regex syntax you actually need - matching, extracting, replacing and splitting text.
section: Advanced Java
order: 20
---

## Pattern and Matcher

`java.util.regex` has two players:

- **`Pattern`** - the compiled regex (expensive to build → compile once, reuse).
- **`Matcher`** - walks a specific input with that pattern.

```java title=Basics.java
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Basics {
    public static void main(String[] args) {
        Pattern p = Pattern.compile("\\d{3}-\\d{4}");   // compile once
        Matcher m = p.matcher("call 555-1234 now");
        System.out.println(m.find());                    // true - pattern exists somewhere
        System.out.println(m.group());                    // 555-1234
    }
}
```

| Method | Meaning |
|---|---|
| `matches()` | entire string matches |
| `find()` | next substring matches (iterate) |
| `group()` | text of the last match (or group N) |
| `start()` / `end()` | match positions |
| `replaceAll(repl)` | replace every match |
| `split(re)` | split like `String.split` |

> **Note:** In Java source, backslashes must be escaped: the regex `\d` is written `"\\d"`. Or use text blocks for readability.

## The syntax you'll actually use

| Token | Matches |
|---|---|
| `.` | any character |
| `\d` / `\D` | digit / non-digit |
| `\w` / `\W` | word char (letter, digit, _) / not |
| `\s` / `\S` | whitespace / not |
| `a|b` | a or b |
| `^` `$` | start / end of input |
| `[abc]` `[a-z]` `[^0-9]` | character classes |
| `a? a* a+ a{3,5}` | quantifiers (0-1, 0+, 1+, {3,5}) |
| `(…)` | capturing group |
| `(?:…)` | non-capturing group |
| `(?i)` | inline case-insensitive flag |

Greedy vs lazy: `.+` grabs as much as possible; `.+?` stops as soon as it can:

```java title=Greedy.java
import java.util.regex.Pattern;

public class Greedy {
    public static void main(String[] args) {
        String html = "<b>bold</b> and <i>italic</i>";
        Pattern greedy = Pattern.compile("<.+>");
        Pattern lazy = Pattern.compile("<.+?>");
        System.out.println(greedy.matcher(html).find()
            ? greedy.matcher(html).group() : "none");   // <b>bold</b> and <i>italic</i>
        var m = lazy.matcher(html);
        m.find();
        System.out.println(m.group());                  // <b>bold</b>
    }
}
```

Rule of thumb for tags: use the lazy version.

## Extracting with groups

```java title=Extract.java
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Extract {
    public static void main(String[] args) {
        String log = "2026-10-04 12:31:05 ERROR disk full";
        Pattern p = Pattern.compile("(\\d{4}-\\d{2}-\\d{2}) (\\d{2}:\\d{2}:\\d{2}) (\\w+) (.*)");
        Matcher m = p.matcher(log);

        if (m.matches()) {
            System.out.println("date  = " + m.group(1));
            System.out.println("time  = " + m.group(2));
            System.out.println("level = " + m.group(3));
            System.out.println("msg   = " + m.group(4));
        }

        // iterating find() over many matches
        Pattern word = Pattern.compile("\\b[A-Z][a-z]+\\b");
        Matcher wm = word.matcher("Alice met Bob in Berlin");
        while (wm.find()) {
            System.out.println("found: " + wm.group() + " @" + wm.start());
        }
    }
}
```

## Replacing and splitting

```java title=Replace.java
import java.util.Arrays;
import java.util.regex.Pattern;

public class Replace {
    public static void main(String[] args) {
        String text = "Order #A-1001 and #B-2002 are ready";

        System.out.println(text.replaceAll("#\\w-\\d+", "[ID]"));

        // back-references in the replacement
        System.out.println("John Smith".replaceAll("(\\w+) (\\w+)", "$2, $1"));  // Smith, John

        // case-insensitive replace via flags
        System.out.println(Pattern.compile("cat", Pattern.CASE_INSENSITIVE)
                                  .matcher("Cat CAT cAt").replaceAll("dog"));

        String csv = "a, b ,,c";
        System.out.println(Arrays.toString(
            csv.split("\\s*,\\s*")));    // [a, b, , c] - trim while splitting
    }
}
```

## Validation recipes

```java title=Validate.java
import java.util.regex.Pattern;

public class Validate {
    // compiled once as constants - a classic performance win
    static final Pattern EMAIL = Pattern.compile(
        "^[\\w.!#$%&'*+/=?^`{|}~-]+@[\\w-]+(?:\\.[\\w-]+)+$");
    static final Pattern STRONG_PW = Pattern.compile(
        "^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d).{8,}$");
    static final Pattern IPV4 = Pattern.compile(
        "^((25[0-5]|2[0-4]\\d|[01]?\\d\\d?)\\.){3}(25[0-5]|2[0-4]\\d|[01]?\\d\\d?)$");

    public static void main(String[] args) {
        System.out.println(EMAIL.matcher("ada@example.com").matches());   // true
        System.out.println(EMAIL.matcher("no-at-sign").matches());        // false
        System.out.println(STRONG_PW.matcher("SunFlower7").matches());    // true
        System.out.println(IPV4.matcher("192.168.0.1").matches());        // true
        System.out.println(IPV4.matcher("999.1.1.1").matches());          // false
    }
}
```

## Performance tips

1. **Compile once** - store `Pattern` in a `static final` field; compiling is the expensive part.
2. **Anchor when possible** - `matches()` or `^…$` lets the engine short-circuit.
3. **Avoid nested quantifiers** like `(a+)+` - the classic catastrophic-backtracking trap.
4. Prefer `find()` with a narrow pattern over `matches()` on giant strings you only partially need.
5. For simple cases (no groups/backrefs), `String.indexOf`/`replace` beats regex.

Related: [Strings](string-methods.html) · [Java Interview Questions](interview.html)
