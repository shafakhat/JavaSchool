---
title: Java Design Patterns
nav: Design Patterns
description: Singleton, Factory, Builder, Observer and Strategy implemented in clean, modern Java.
section: Advanced Java
order: 40
---

## What (and what not) to do with patterns

Design patterns are **named solutions to recurring design problems** - vocabulary for teams, not decoration. Learn a handful deeply; reach for them when you feel the pain they solve.

| Pattern | Type | One-liner |
|---|---|---|
| Singleton | creational | exactly one instance, globally reachable |
| Factory Method | creational | let subclasses/implementations decide which object you get |
| Builder | creational | step-by-step construction of complex immutable objects |
| Observer | behavioral | many listeners react to one object's changes |
| Strategy | behavioral | swap algorithms behind a stable interface |

## Singleton (thread-safe)

```java title=Singleton.java
public class Singleton {
    // initialization-on-demand holder: lazy + thread-safe without locks
    private static class Holder {
        private static final Singleton INSTANCE = new Singleton();
    }

    private Singleton() {          // private ctor prevents new-ing from outside
    }

    public static Singleton getInstance() {
        return Holder.INSTANCE;
    }

    void hello() {
        System.out.println("single instance: " + System.identityHashCode(this));
    }

    public static void main(String[] args) {
        Singleton a = Singleton.getInstance();
        Singleton b = Singleton.getInstance();
        System.out.println(a == b);      // true
        a.hello();
    }
}
```

> **Tip:** modern Java often prefers passing dependencies (DI) over global singletons - they hide coupling and hurt testability. Use sparingly.

## Factory Method

```java title=Factory.java
interface Notifier {
    void send(String to, String message);
}

class EmailNotifier implements Notifier {
    public void send(String to, String message) {
        System.out.println("email to " + to + ": " + message);
    }
}

class SmsNotifier implements Notifier {
    public void send(String to, String message) {
        System.out.println("sms to " + to + ": " + message);
    }
}

public class Factory {
    // the factory - caller doesn't know/care which implementation it gets
    static Notifier create(String channel) {
        return switch (channel) {
            case "email" -> new EmailNotifier();
            case "sms" -> new SmsNotifier();
            default -> throw new IllegalArgumentException("unknown channel: " + channel);
        };
    }

    public static void main(String[] args) {
        Notifier n = Factory.create("sms");
        n.send("+911234567890", "Your code is 4821");
    }
}
```

Callers depend on `Notifier`; adding `PushNotifier` later changes nothing at the call sites (open/closed principle).

## Builder (immutable object, many parameters)

```java title=Builder.java
public class Builder {
    static final class HttpRequest {
        private final String method;
        private final String url;
        private final int timeoutMs;
        private final boolean followRedirects;

        private HttpRequest(Builder b) {
            this.method = b.method;
            this.url = b.url;
            this.timeoutMs = b.timeoutMs;
            this.followRedirects = b.followRedirects;
        }

        public String toString() {
            return method + " " + url + " timeout=" + timeoutMs
                + " follow=" + followRedirects;
        }

        static class Builder {          // fluent builder
            private String method = "GET";
            private final String url;
            private int timeoutMs = 5000;
            private boolean followRedirects = true;

            Builder(String url) { this.url = url; }

            Builder method(String m) { this.method = m; return this; }
            Builder timeout(int ms) { this.timeoutMs = ms; return this; }
            Builder followRedirects(boolean f) { this.followRedirects = f; return this; }

            HttpRequest build() {
                if (!Set.of("GET", "POST", "PUT", "DELETE").contains(method)) {
                    throw new IllegalArgumentException("bad method " + method);
                }
                return new HttpRequest(this);
            }
        }

        static Builder to(String url) { return new Builder(url); }
    }

    public static void main(String[] args) {
        HttpRequest req = HttpRequest.to("https://api.example.com/users")
                                      .method("POST")
                                      .timeout(1500)
                                      .build();
        System.out.println(req);
    }
}
```

Much better than 5-arg constructors or a mutable JavaBean - and the object stays immutable.

## Observer

```java title=Observer.java
import java.util.ArrayList;
import java.util.List;
import java.util.function.Consumer;

public class Observer {
    static final class PriceFeed {
        private final List<Consumer<Double>> listeners = new ArrayList<>();

        void subscribe(Consumer<Double> listener) { listeners.add(listener); }

        void publish(double price) {
            for (Consumer<Double> l : listeners) {
                l.accept(price);          // notify every subscriber
            }
        }
    }

    public static void main(String[] args) {
        PriceFeed feed = new PriceFeed();
        feed.subscribe(p -> System.out.printf("alert: price moved to %.2f%n", p));
        feed.subscribe(p -> { if (p > 100) System.out.println("threshold hit"); });

        feed.publish(99.5);
        feed.publish(101.25);
    }
}
```

The JDK's own `PropertyChangeSupport`, Swing listeners and `Observable`/`Flow` follow this shape; reactive streams (RxJava, Project Reactor) are Observer grown up.

## Strategy

```java title=Strategy.java
import java.util.List;
import java.util.function.BinaryOperator;

public class Strategy {
    // the algorithm is data - chosen at runtime
    static int reduce(List<Integer> nums, BinaryOperator<Integer> strategy) {
        int acc = nums.get(0);
        for (int i = 1; i < nums.size(); i++) {
            strategy.apply(acc, nums.get(i));
            acc = strategy.apply(acc, nums.get(i));
        }
        return acc;
    }

    public static void main(String[] args) {
        List<Integer> nums = List.of(3, 1, 4, 1, 5);

        BinaryOperator<Integer> sum = Integer::sum;
        BinaryOperator<Integer> max = Math::max;

        System.out.println("max = " + reduce(nums, max));   // 5
        System.out.println("sum-ish = " + reduce(nums, sum));
    }
}
```

Real-world examples: `Comparator` passed to `sort`, `Charset` passed to encoding, pricing rules, payment providers behind one `PaymentService` interface.

## Anti-patterns to avoid

- **God class** - one class doing everything; split by responsibility.
- **Premature abstraction** - don't build a factory hierarchy for one implementation; refactor *into* patterns when a second variant appears.
- **Singleton everywhere** - global mutable state is hidden coupling.
- **Copy-paste "patterns"** - if you can't name the problem it solves, skip it.

Related: [Abstraction & interfaces](abstraction.html) · [Design-Pattern code examples imported from java2s](design-pattern-*.html in the sidebar)
