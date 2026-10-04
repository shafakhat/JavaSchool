---
title: Java Exceptions
nav: Exceptions
description: try/catch/finally, checked vs unchecked exceptions, custom exceptions, throw and try-with-resources.
section: Core Java
order: 10
---

## What is an exception?

An **exception** is an object describing something that went wrong. Instead of silently returning bad data, Java *throws* an exception that interrupts the normal flow until someone catches it.

```text title=Normal vs exceptional flow
 normal:     read file -> parse -> return result
 exceptional: read file -> THROWS IOException -> nearest catch handles it
```

```java title=TryCatch.java
public class TryCatch {
    public static void main(String[] args) {
        int[] nums = {1, 2, 3};

        try {
            System.out.println(nums[5]);        // throws ArrayIndexOutOfBoundsException
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("bad index: " + e.getMessage());
        }

        System.out.println("program continues");
    }
}
```

```text title=Output
bad index: Index 5 out of bounds for length 3
program continues
```

## The exception hierarchy

```text title=java.lang.Throwable
Throwable
├── Error                 <- serious JVM/system problems (OutOfMemoryError...): don't catch
└── Exception
    ├── RuntimeException   <- UNCHECKED (NullPointerException, ArithmeticException...)
    │   ├── NullPointerException
    │   ├── IllegalArgumentException
    │   ├── ClassCastException
    │   └── ...
    └── checked: IOException, SQLException, FileNotFoundException...
```

| | Checked | Unchecked |
|---|---|---|
| Compiler enforces handling | **yes** - catch or declare | no |
| Typical cause | recoverable, external (file, network) | programming bugs |
| `throws` declaration required | yes | optional |
| Examples | `IOException`, `ParseException` | `NullPointerException`, `ArithmeticException` |

```java title=CheckedVsUnchecked.java
import java.io.FileInputStream;
import java.io.FileNotFoundException;

public class CheckedVsUnchecked {
    // method must declare it - the compiler enforces it
    static void openFile(String path) throws FileNotFoundException {
        new FileInputStream(path);
    }

    static void divide(int a, int b) {
        System.out.println(a / b);        // ArithmeticException is unchecked - no throws needed
    }

    public static void main(String[] args) {
        try {
            openFile("missing.txt");
        } catch (FileNotFoundException e) {
            System.out.println("handled: " + e.getMessage());
        }

        try {
            divide(4, 0);
        } catch (ArithmeticException e) {
            System.out.println("handled: " + e);
        }
    }
}
```

## catch, finally, and try-with-resources

```java title=Finally.java
import java.io.FileWriter;
import java.io.IOException;

public class Finally {
    public static void main(String[] args) {
        try {
            System.out.println("work");
            // throw new RuntimeException("boom");
        } catch (RuntimeException e) {
            System.out.println("caught: " + e.getMessage());
        } finally {
            System.out.println("always runs - cleanup goes here");
        }
    }
}
```

`finally` runs whether you return, throw, or fall through - the classic place for cleanup. Since Java 7, **try-with-resources** does it automatically for anything implementing `AutoCloseable`:

```java title=Resources.java
import java.io.FileWriter;
import java.io.IOException;

public class Resources {
    public static void main(String[] args) {
        // the resource is closed automatically, even if an exception occurs
        try (FileWriter w = new FileWriter("out.txt")) {
            w.write("hello from try-with-resources\n");
            w.write("second line\n");
        } catch (IOException e) {
            System.out.println("write failed: " + e.getMessage());
        }

        // multiple resources: closed in reverse order
        try (var in = new java.util.Scanner(new java.io.FileInputStream("out.txt"))) {
            while (in.hasNextLine()) {
                System.out.println("> " + in.nextLine());
            }
        } catch (java.io.IOException e) {
            System.out.println("read failed");
        }
    }
}
```

Never open files with plain `try/finally` in new code - `try (...)` is shorter *and* exception-safe.

## Throwing exceptions

```java title=Throw.java
public class Throw {
    static int parseAge(String text) {
        if (text == null || text.isBlank()) {
            throw new IllegalArgumentException("age text is required");
        }
        int age;
        try {
            age = Integer.parseInt(text.trim());
        } catch (NumberFormatException e) {
            throw new IllegalArgumentException("not a number: " + text, e);  // keep cause!
        }
        if (age < 0 || age > 150) {
            throw new IllegalArgumentException("age out of range: " + age);
        }
        return age;
    }

    public static void main(String[] args) {
        System.out.println(parseAge(" 42 "));

        try {
            parseAge("forty");
        } catch (IllegalArgumentException e) {
            System.out.println("rejected -> " + e.getMessage());
            System.out.println("cause    -> " + e.getCause());
        }
    }
}
```

Guidelines for throwing:

- Choose the **most specific** sensible type (`IllegalArgumentException` for bad arguments).
- Include **context** in the message (`"age out of range: " + age`, not `"bad"`).
- Pass the original exception as the **cause** (`new X("msg", cause)`) so stack traces aren't lost.
- Never swallow exceptions silently (`catch (Exception e) {}` is a code smell).

## Custom exceptions

```java title=InsufficientFundsException.java
class InsufficientFundsException extends Exception {
    private final double shortfall;

    InsufficientFundsException(double shortfall) {
        super("short by " + shortfall);
        this.shortfall = shortfall;
    }

    double getShortfall() { return shortfall; }
}

class Account {
    private double balance;

    Account(double balance) { this.balance = balance; }

    void withdraw(double amount) throws InsufficientFundsException {
        if (amount > balance) {
            throw new InsufficientFundsException(amount - balance);
        }
        balance -= amount;
    }

    double getBalance() { return balance; }

    public static void main(String[] args) {
        Account a = new Account(100);
        try {
            a.withdraw(150);
        } catch (InsufficientFundsException e) {
            System.out.println("declined: " + e.getMessage() + " (shortfall=" + e.getShortfall() + ")");
        }
        System.out.println("balance = " + a.getBalance());
    }
}
```

Checked custom exceptions force callers to deal with the failure; extend `RuntimeException` if it represents a bug rather than an expected condition.

## Stack traces

```text title=Reading a stack trace
Exception in thread "main" java.lang.IllegalStateException: no session
    at com.app.Auth.login(Auth.java:42)     <- where it was thrown
    at com.app.Auth.main(Auth.java:10)      <- who called it
    ...
```

Read **top down**: the first line gives type + message; the frames below show the exact path. The first frame *in your own code* is usually where the fix belongs.

> **Remember:** Exceptions are for **exceptional situations**, not for normal control flow. Using exceptions to replace `if/else` is slow and hard to read.

Next: [File I/O](file-io.html) - reading and writing files safely.
