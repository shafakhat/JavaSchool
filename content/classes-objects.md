---
title: Java Classes and Objects
nav: Classes & Objects
description: Define classes, create objects, work with fields, methods, references and the this keyword.
section: Object Oriented
order: 10
---

## Class vs object

A **class** is the blueprint; an **object** is an instance built from it.

```text title=Blueprint vs house
 class Car  -------->  car1 (red, 100 km)
                       car2 (blue, 40 km)
```

```java title=Car.java
public class Car {
    // fields (state)
    String color;
    int speed;

    // behavior
    void accelerate(int by) {
        speed += by;
    }

    void brake(int by) {
        speed = Math.max(0, speed - by);
    }

    void describe() {
        System.out.println(color + " car at " + speed + " km/h");
    }

    public static void main(String[] args) {
        Car a = new Car();      // create object 1
        a.color = "red";
        a.accelerate(60);

        Car b = new Car();      // create object 2
        b.color = "blue";
        b.accelerate(40);

        a.describe();           // red car at 60 km/h
        b.describe();           // blue car at 40 km/h
    }
}
```

- **Fields** hold the object's state (`color`, `speed`).
- **Methods** define what the object can do (`accelerate`, `describe`).
- `new Car()` allocates a fresh object on the **heap** and returns a reference to it.

## References - two names for one object

```java title=Reference.java
public class Reference {
    static class Car {          // (the Car class from the example above)
        String color;
    }

    public static void main(String[] args) {
        Car original = new Car();
        original.color = "green";

        Car alias = original;        // both names point to the SAME object
        alias.color = "black";

        System.out.println(original.color);  // black - changed via alias
    }
}
```

Assigning an object variable copies the **reference**, not the object. For a true copy you need the `clone()` method or a copy constructor.

## Fields, defaults and initialization

```java title=Fields.java
public class Fields {
    String name;          // default null
    int count;            // default 0
    boolean flag;         // default false
    double ratio;         // default 0.0

    int explicit = 10;    // always initialized

    public static void main(String[] args) {
        Fields f = new Fields();
        System.out.println(f.name + " " + f.count + " " + f.flag + " " + f.ratio + " " + f.explicit);
        // null 0 false 0.0 10
    }
}
```

Instance fields default to `0`/`false`/`null`. **Local variables have no default** - the compiler forces you to initialize them.

## The `this` keyword

`this` refers to the **current object**. Its two main uses:

```java title=ThisKeyword.java
public class ThisKeyword {
    String name;
    int age;

    // 1) disambiguate parameter vs field
    ThisKeyword(String name, int age) {
        this.name = name;    // left side: field; right side: parameter
        this.age = age;
    }

    // 2) pass the current object along
    void printSelf() {
        System.out.println(this);
    }

    public static void main(String[] args) {
        ThisKeyword p = new ThisKeyword("Noor", 20);
        p.printSelf();                       // prints object hash code like ThisKeyword@1b6d3586
        System.out.println(p.name + ", " + p.age);
    }
}
```

## Static members

`static` members belong to the **class**, shared by all objects:

```java title=StaticMembers.java
public class StaticMembers {
    static int instances = 0;         // one copy for the whole class
    String id;

    StaticMembers() {
        instances++;
        id = "obj-" + instances;
    }

    static void showCount() {         // callable as StaticMembers.showCount()
        System.out.println("created so far: " + instances);
    }

    public static void main(String[] args) {
        new StaticMembers();
        new StaticMembers();
        StaticMembers third = new StaticMembers();
        StaticMembers.showCount();    // created so far: 3
        System.out.println(third.id); // obj-3
    }
}
```

## A realistic small class

```java title=BankAccount.java
public class BankAccount {
    private final String owner;    // see Encapsulation for 'private'
    private double balance;

    public BankAccount(String owner, double opening) {
        this.owner = owner;
        this.balance = opening;
    }

    public void deposit(double amount) {
        if (amount <= 0) throw new IllegalArgumentException("deposit must be positive");
        balance += amount;
    }

    public boolean withdraw(double amount) {
        if (amount > balance) return false;   // overdraft not allowed
        balance -= amount;
        return true;
    }

    public double getBalance() {
        return balance;
    }

    public static void main(String[] args) {
        BankAccount acct = new BankAccount("Kavya", 500);
        acct.deposit(1500);
        boolean ok = acct.withdraw(300);
        System.out.println(acct.owner + " withdrew? " + ok + ", balance=" + acct.getBalance());
        // compile error below if you uncomment: acct.balance = 1_000_000;
    }
}
```

This pattern - data + methods that guard the data - is the essence of object-oriented design.

## Objects on the heap (mental model)

```text title=What new really does
 BankAccount acct = new BankAccount("Kavya", 500);
 ^              ^     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 |              |     allocates on heap, runs constructor
 |              +------ variable on the stack (holds a reference)
 +--------------------- type
```

The stack holds the reference (cheap); the heap holds the object (managed by the garbage collector).

> **Remember:** `null` is a reference that points to nothing. Calling a method on `null` throws `NullPointerException` - a runtime error, not a compile error.

Next: [Constructors](constructors.html) - the special methods that build objects.
