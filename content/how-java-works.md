---
title: How Java Works
nav: How Java Works
description: JVM, JRE and JDK explained, plus the compile-run cycle from source code to bytecode.
section: Get Started
order: 40
---

## Source -> Bytecode -> Machine code

Java uses a two-stage process. You write source code, the compiler turns it into **bytecode**, and the **JVM** translates that bytecode into machine instructions for the host operating system.

```text title=The Java pipeline
Hello.java --[ javac ]--> Hello.class --[ JVM ]--> machine code --> runs
 (source)              (bytecode)      (JIT)
```

```java title=Hello.java
public class Hello {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

```bash title=Terminal
javac Hello.java     # stage 1: compile to bytecode
java Hello           # stage 2: JVM executes the bytecode
```

Because all operating systems understand the same bytecode, the *same* `Hello.class` runs everywhere a JVM exists. That is the "Write Once, Run Anywhere" promise.

## JDK vs JRE vs JVM

| Component | What it is | Contains |
|---|---|---|
| **JVM** | The virtual machine that runs bytecode | Interpreter + JIT compiler + garbage collector |
| **JRE** | A complete runtime | JVM + core class libraries |
| **JDK** | A complete development kit | JRE + `javac`, `jar`, debuggers, tools |

```text title=Relationship
JDK = JRE + development tools (javac, jar, jdb...)
JRE = JVM + core libraries (java.lang, java.util, java.io...)
JVM = executes bytecode on this machine
```

As a developer you always install the **JDK**.

## What happens when you run `java Hello`

1. The **launcher** finds `Hello.class` on the classpath.
2. The **class loader** reads and verifies the bytecode.
3. The **interpreter** starts executing `main`.
4. The **JIT compiler** (just-in-time) profiles hot methods and compiles them to fast native machine code.
5. The **garbage collector** reclaims memory from objects that are no longer reachable.

```text title=Runtime anatomy
                 +---------------------------+
   Hello.class ->| Class loader  -> Verifier |
                 +---------------------------+
                          |
                 +---------------------------+
                 | JVM: interpreter + JIT    |--> native code
                 +---------------------------+
                          |
                 +---------------------------+
                 | Heap | Stacks | GC        |
                 +---------------------------+
```

## A quick look at memory

When a program runs, the JVM divides memory into regions:

- **Heap** - where every object lives. Managed by the garbage collector.
- **Stack** - one per thread; holds method frames and local variables.
- **Metaspace** - class metadata (loaded class definitions).

```java title=HeapVsStack.java
public class HeapVsStack {
    public static void main(String[] args) {
        int x = 42;              // x lives on the stack (primitive)
        int[] nums = {1, 2, 3};  // the array object lives on the heap;
                                 // 'nums' (a reference) lives on the stack
        greet("Ada");            // the String may be interned on the heap
    }

    static void greet(String name) {   // 'name' is a stack reference
        System.out.println("Hi " + name);
    }
}
```

> **Note:** You never free memory manually in Java. When an object can no longer be reached, the garbage collector reclaims it.

## Platform independence in practice

```text title=Same bytecode, many platforms
        +---------------------+
        |   Hello.class       |   <- compiled once
        +---------------------+
       /          |           \
      v           v            v
  JVM/Windows  JVM/Linux    JVM/macOS
      |           |            |
   .exe bits   .exe bits    .exe bits   <- machine code per OS
```

That is why installers ship a JAR file rather than separate binaries for each OS - the end user's JVM does the last mile.

## Compiled vs interpreted - why Java is fast

Early Java was purely interpreted and gained a reputation for being slow. Modern JVMs are hybrid:

- Bytecode starts executing immediately through the interpreter.
- Hot loops and methods are detected and compiled by the **JIT** to native code.
- The JIT uses runtime profile information that ahead-of-time compilers don't have (e.g. knowing which branch is usually taken).

```text title=Speed model
first runs ...... interpreted (fast startup, slow execution)
       |
watching ....... JVM counts how often methods/loops run
       |
hot code ....... JIT compiles to optimized machine code
       |
steady state ... near native speed
```

> **Tip:** In interviews, "Java is slow" is usually answered with: *interpreted startup + JIT compilation + garbage collection = near-native steady-state performance.*

Next: [Java Syntax](syntax.html) - the rules that shape every program.
