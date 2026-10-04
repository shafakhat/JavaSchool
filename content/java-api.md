---
title: Useful Java Classes
nav: Useful Java Classes
description: Everyday standard-library classes - Math, Scanner, Arrays, Date/Time, Random, UUID and more.
section: Reference
order: 30
---

## Math

```java title=MathDemo.java
public class MathDemo {
    public static void main(String[] args) {
        System.out.println(Math.abs(-7));        // 7
        System.out.println(Math.max(3, 9));      // 9
        System.out.println(Math.min(3, 9));      // 3
        System.out.println(Math.pow(2, 10));     // 1024.0
        System.out.println(Math.sqrt(81));       // 9.0
        System.out.println(Math.ceil(2.1));      // 3.0
        System.out.println(Math.floor(2.9));     // 2.0
        System.out.println(Math.round(2.6));     // 3 (returns long)
        System.out.println(Math.PI);
        System.out.println(Math.random());       // 0.0 <= x < 1.0
    }
}
```

For money or exact decimals, avoid `double` - use `BigDecimal`:

```java title=BigDecimalDemo.java
import java.math.BigDecimal;
import java.math.RoundingMode;

public class BigDecimalDemo {
    public static void main(String[] args) {
        BigDecimal a = new BigDecimal("0.10");
        BigDecimal b = new BigDecimal("0.20");
        System.out.println(a.add(b));                                   // 0.30
        System.out.println(a.add(b).setScale(2, RoundingMode.HALF_UP)); // 0.30
        System.out.println(BigDecimal.valueOf(3).multiply(BigDecimal.valueOf(1.5))); // 4.5
    }
}
```

## Random

```java title=RandomDemo.java
import java.util.Random;

public class RandomDemo {
    public static void main(String[] args) {
        Random r = new Random(42);                 // fixed seed = reproducible

        System.out.println(r.nextInt());           // any int
        System.out.println(r.nextInt(6) + 1);      // dice: 1..6
        System.out.println(r.nextDouble());        // 0.0 .. <1.0
        System.out.println(r.nextBoolean());

        // modern one-liners (Java 17+ Math.random alternatives)
        System.out.println(java.util.Random.from(java.util.random.RandomGenerator.getDefault()).nextInt(100));
        System.out.println(ThreadLocalRandom().nextInt(10, 20));
    }

    static java.util.concurrent.ThreadLocalRandom ThreadLocalRandom() {
        return java.util.concurrent.ThreadLocalRandom.current();
    }
}
```

(The `ThreadLocalRandom` helper just keeps the example on one line - in real code call `ThreadLocalRandom.current().nextInt(10, 20)` directly.)

## Scanner (input)

```java title=ScannerDemo.java
import java.util.Scanner;

public class ScannerDemo {
    public static void main(String[] args) {
        Scanner sc = new Scanner("Ada Lovelace 36 4.9");   // usually: new Scanner(System.in)

        String first = sc.next();      // token (whitespace-delimited)
        String last = sc.next();
        int age = sc.nextInt();
        double score = sc.nextDouble();

        System.out.println(first + " " + last + ", age " + age + ", score " + score);
        sc.close();
    }
}
```

| Method | Reads |
|---|---|
| `next()` / `nextLine()` | token / whole line |
| `nextInt()` / `nextDouble()` / `nextBoolean()` | typed values |
| `hasNext()` / `hasNextInt()` | is more input available? |
| `useDelimiter(regex)` | custom token separator |

Reading user input: `new Scanner(System.in)` - check `hasNextInt()` first to avoid `InputMismatchException`.

## Arrays utilities

```java title=ArraysDemo.java
import java.util.Arrays;

public class ArraysDemo {
    public static void main(String[] args) {
        int[] a = {5, 2, 9, 1};

        Arrays.sort(a);
        System.out.println(Arrays.toString(a));          // [1, 2, 5, 9]
        System.out.println(Arrays.binarySearch(a, 5));   // 2

        int[] copy = Arrays.copyOf(a, 6);                // pad with 0
        System.out.println(Arrays.toString(copy));

        int[] part = Arrays.copyOfRange(a, 1, 3);        // [start, end)
        System.out.println(Arrays.toString(part));

        Arrays.fill(copy, 7);
        System.out.println(Arrays.toString(copy));
        System.out.println(Arrays.equals(a, new int[]{1, 2, 5, 9}));

        String[][] grid = {{"a", "b"}, {"c", "d"}};
        System.out.println(Arrays.deepToString(grid));   // nested arrays
    }
}
```

## Date and Time (`java.time`, Java 8+)

```java title=DateTime.java
import java.time.*;
import java.time.format.DateTimeFormatter;

public class DateTime {
    public static void main(String[] args) {
        LocalDate today = LocalDate.now();
        LocalDate birthday = LocalDate.of(1995, 8, 15);
        LocalTime now = LocalTime.now();
        LocalDateTime dt = LocalDateTime.of(today, now);
        Instant instant = Instant.now();                        // machine timestamp (UTC)
        ZoneId zone = ZoneId.of("Asia/Kolkata");
        ZonedDateTime zdt = instant.atZone(zone);

        System.out.println(today);
        System.out.println("age-ish: " + Period.between(birthday, today).getYears() + " years");
        System.out.println(dt.format(DateTimeFormatter.ofPattern("dd MMM yyyy, HH:mm")));

        LocalDate plus10 = today.plusDays(10);
        System.out.println("in 10 days: " + plus10);
        System.out.println("day of week: " + today.getDayOfWeek());

        Duration d = Duration.between(LocalTime.of(9, 0), LocalTime.of(10, 30));
        System.out.println("minutes = " + d.toMinutes());       // 90
        System.out.println(zdt);
    }
}
```

Immutable, thread-safe, and no `Date`/`Calendar` quirks. For anything date-related in new code, use `java.time`.

## UUID

```java title=UuidDemo.java
import java.util.UUID;

public class UuidDemo {
    public static void main(String[] args) {
        UUID id = UUID.randomUUID();
        System.out.println(id);                    // e.g. 3f1d...-...-...-...-...
        System.out.println(id.toString().replace("-", ""));
    }
}
```

## StringBuilder quick reference

```java title=SbDemo.java
public class SbDemo {
    public static void main(String[] args) {
        StringBuilder sb = new StringBuilder("start");
        sb.append("!").append(" more").append(42);
        sb.insert(0, ">> ");
        sb.replace(0, 2, "**");
        sb.deleteCharAt(sb.length() - 1);
        sb.reverse();
        System.out.println(sb);
        System.out.println("len=" + sb.length() + " charAt(0)=" + sb.charAt(0));
    }
}
```

## Wrap-up

| Task | Reach for |
|---|---|
| Math | `Math`, `BigDecimal` |
| Random | `Random`, `ThreadLocalRandom` |
| Input | `Scanner` |
| Arrays | `Arrays` |
| Dates | `java.time` (`LocalDate`, `ZonedDateTime`) |
| IDs | `UUID` |
| Text building | `StringBuilder` |

Test yourself on all of this with the [Java Quiz](quiz.html).
