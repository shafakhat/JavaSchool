---
title: Java Introduction
nav: Introduction
description: What is Java, a quick history, core features, and where Java is used today.
section: Get Started
order: 20
---

## What is Java?

Java is a **general-purpose, object-oriented programming language** created by James Gosling at Sun Microsystems and released in 1995. Its defining promise is:

> Write once, run anywhere (WORA).

You compile Java source code into an intermediate form called **bytecode**, which runs on any device that has a Java Virtual Machine (JVM). The same `.class` file can run on Windows, Linux or macOS without recompiling.

## A very short history

| Year | Milestone |
|------|-----------|
| 1991 | Project "Green" starts at Sun Microsystems (set-top boxes) |
| 1995 | Java 1.0 released; applets arrive in browsers |
| 2004 | Java 5: generics, annotations, enhanced for loop |
| 2006 | Sun opens source (GPL) and open-sources the JVM |
| 2010 | Oracle acquires Sun |
| 2014 | Java 8: lambdas and streams - the modern era begins |
| 2018+ | Six-month release cadence (9, 11, 17, 21, 25...) |

Today Java is maintained by Oracle with OpenJDK as the open-source reference implementation, and it is one of the most widely used languages in the world.

## Core features

- **Simple syntax** - C-like syntax with automatic memory management (garbage collection).
- **Object-oriented** - everything revolves around classes and objects (with a few primitives as exceptions).
- **Platform independent** - bytecode runs on any JVM.
- **Statically typed** - types are checked at compile time, which catches many bugs early.
- **Robust** - strong exception handling, bounds checking, and no manual pointer arithmetic.
- **Secure** - bytecode verification, sandboxing, no dangerous pointer operations.
- **Multithreaded** - built-in support for concurrent programming.
- **Rich standard library** - collections, I/O, networking, regex, JSON, dates, and much more.

## Where is Java used?

<div class="cards">
  <div class="card"><div class="card-icon">&#128187;</div><h3>Enterprise apps</h3><p>Banking, insurance and large back-end systems on Spring Boot and Jakarta EE.</p></div>
  <div class="card"><div class="card-icon">&#128241;</div><h3>Android</h3><p>Android apps are (historically) built on the Java language and JVM libraries.</p></div>
  <div class="card"><div class="card-icon">&#9729;</div><h3>Big data</h3><p>Hadoop, Spark and Kafka are Java/JVM based.</p></div>
  <div class="card"><div class="card-icon">&#127760;</div><h3>Web &amp; APIs</h3><p>REST services, microservices and high-throughput back ends.</p></div>
</div>

## Java vs other languages

| | Java | Python | C++ |
|---|---|---|---|
| Typing | Static | Dynamic | Static |
| Memory | Garbage collected | Garbage collected | Manual (mostly) |
| Speed | Fast (JIT) | Slower | Fastest |
| Primary use | Enterprise, Android, back end | Scripting, data, AI | Games, embedded, systems |

## Hello, Java!

Every Java program starts with a class and a `main` method. Here is the classic first program:

```java title=Hello.java
public class Hello {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

Running it prints:

```text title=Output
Hello, World!
```

Don't worry about the syntax yet - the next pages explain every keyword. By the end of this tutorial you will be able to read and write programs like this one with confidence.

> **Tip:** Java source files are named after the public class they contain, so `Hello.java` must contain `public class Hello`.

## What you will learn

1. **Basics** - syntax, variables, operators, strings, conditions, loops, arrays, methods
2. **OOP** - classes, constructors, inheritance, polymorphism, interfaces, packages
3. **Core APIs** - exceptions, files, threads, generics
4. **Modern Java** - lambdas and streams
5. **Collections** - List, Set, Map and when to use each
6. **Databases** - JDBC in practice

Ready? Let's [set up your environment](install.html).
