---
title: Java Encapsulation
nav: Encapsulation
description: Access modifiers, getters and setters, private fields and why encapsulation keeps code maintainable.
section: Object Oriented
order: 50
---

## Hide the internals, expose an API

**Encapsulation** = bundle data and the methods that touch it inside one unit, and restrict direct access to the internals. You expose a small, safe **API** (methods) instead of the raw fields.

```text title=Without vs with encapsulation
 before:  obj.balance = -500;   // anyone can corrupt state
 after:   obj.withdraw(500);    // method checks the rules first
```

```java title=Encapsulation.java
public class Encapsulation {
    private double balance;          // hidden from the outside world

    public void deposit(double amount) {        // validated gateway in
        if (amount <= 0) throw new IllegalArgumentException("positive amount only");
        balance += amount;
    }

    public boolean withdraw(double amount) {    // validated gateway out
        if (amount > balance) return false;
        balance -= amount;
        return true;
    }

    public double getBalance() {                // controlled read access
        return balance;
    }

    public static void main(String[] args) {
        Encapsulation wallet = new Encapsulation();
        wallet.deposit(1000);
        wallet.withdraw(250);
        System.out.println("balance = " + wallet.getBalance());

        // wallet.balance = -1;     // ERROR: private - the compiler protects invariants
        try {
            wallet.deposit(-10);
        } catch (IllegalArgumentException e) {
            System.out.println("blocked: " + e.getMessage());
        }
    }
}
```

## The four access levels

| Modifier | Class | Package | Subclass (other pkg) | World |
|---|---|---|---|---|
| `public` | &#10004; | &#10004; | &#10004; | &#10004; |
| `protected` | &#10004; | &#10004; | &#10004; | &#10004; |
| *(default)* package-private | &#10004; | &#10004; | &#10004; | &#10004; |
| `private` | &#10004; | &#10004; | &#10004; | &#10004; |

```java title=Access.java
public class Access {
    public String openToAll = "public";       // anyone
    protected String family = "protected";    // package + subclasses
    String siblings = "package-private";      // package only
    private String secret = "private";        // this class only

    public String getSecret() { return secret; }

    public static void main(String[] args) {
        Access a = new Access();
        System.out.println(a.openToAll + " " + a.getSecret());
        // System.out.println(a.secret);      // ERROR from outside the class
    }
}
```

> **Remember:** Top-level classes are only `public` or package-private. Members (fields/methods) can use all four levels. **Default your fields to `private`** and widen only when needed.

## Getters and setters done right

A getter/setter pair is not about ceremony - it gives you **control and observability**:

```java title=Employee.java
public class Employee {
    private String name;
    private int age;
    private double salary;

    public Employee(String name, int age, double salary) {
        this.name = requireName(name);
        setAge(age);
        setSalary(salary);
    }

    public String getName() { return name; }

    public void setName(String name) { this.name = requireName(name); }

    public int getAge() { return age; }

    public void setAge(int age) {
        if (age < 18 || age > 70) throw new IllegalArgumentException("age: " + age);
        this.age = age;
    }

    public double getSalary() { return salary; }

    public void setSalary(double salary) {
        if (salary < 0) throw new IllegalArgumentException("salary must be >= 0");
        this.salary = salary;
    }

    private static String requireName(String n) {
        if (n == null || n.isBlank()) throw new IllegalArgumentException("name required");
        return n.trim();
    }

    @Override
    public String toString() {
        return name + " (" + age + ") earns " + salary;
    }

    public static void main(String[] args) {
        Employee e = new Employee("Tara", 30, 75000);
        System.out.println(e);
        try {
            e.setAge(12);
        } catch ( IllegalArgumentException ex) {
            System.out.println("rejected: " + ex.getMessage());
        }
    }
}
```

Benefits:

- **Invariants** (rules the object must always satisfy) are enforced in one place.
- You can **change the representation** later (e.g. store cents as `long`) without touching callers.
- You can add **logging or lazy computation** inside accessors invisibly.

## When NOT to write a setter

Not every field needs write access. If an attribute is set at construction and never changes, expose only a getter - the object stays immutable-ish and thread-safe for free:

```java title=ImmutablePoint.java
public class ImmutablePoint {
    private final int x;
    private final int y;

    public ImmutablePoint(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public int getX() { return x; }
    public int getY() { return y; }

    public static void main(String[] args) {
        ImmutablePoint p = new ImmutablePoint(3, 4);
        System.out.println("(" + p.getX() + ", " + p.getY() + ")");
    }
}
```

## Encapsulation vs "public fields are fine"

Public fields seem faster - until they aren't:

| Public field | Encapsulated field |
|---|---|
| Any code can set `account.balance = -999` | Only methods that know the rules |
| Callers depend on the exact field | Callers depend on behavior |
| Adding validation later = touching every call site | Adding validation = change one method |
| Hard to add caching/notifications | Getters can cache or fire events |

Framework note: many libraries (Jackson, JPA/Hibernate) actually work *better* with private fields plus getters/setters.

## Encapsulation in layers

Think of encapsulation at every scale:

1. **Method** - hide intermediate variables behind a name.
2. **Class** - private fields + public methods.
3. **Package** - package-private members invisible outside the package ([Packages](packages.html)).
4. **Module** (Java 9+) - `module-info.java` can hide entire packages.

Next: [Abstraction](abstraction.html) - hiding complexity behind interfaces.
