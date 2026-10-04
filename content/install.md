---
title: Java Environment Setup
nav: Install / Setup
description: Install a JDK on Windows, macOS or Linux and compile plus run your first Java program.
section: Get Started
order: 30
---

## What you need

To write and run Java programs you need a **JDK** (Java Development Kit). The JDK contains:

- **javac** - the compiler (`.java` -> `.class`)
- **java** - the launcher that runs bytecode on the JVM
- **jar** - tooling to package code
- The standard class libraries

> **Note:** A JRE (Java Runtime Environment) can only *run* Java programs. To *develop*, always install the full JDK.

## Step 1 - Install a JDK

Any of these works:

| Distribution | Best for | Link pattern |
|---|---|---|
| Eclipse Temurin (Adoptium) | Most users, free LTS builds | `adoptium.net` |
| Oracle JDK | Commercial support | `oracle.com/java` |
| OpenJDK | Reference builds | `jdk.java.net` |
| Amazon Corretto | AWS workloads | `corretto.aws` |

Install the latest **LTS** release (17 or 21) - it is the safest choice for learning and production.

**Windows:** download the `.msi`, run it, and tick "Set JAVA_HOME" if offered.
**macOS:** download the `.pkg` installer.
**Linux:** e.g. on Debian/Ubuntu:

```bash title=Terminal
sudo apt update
sudo apt install openjdk-21-jdk
```

## Step 2 - Verify the installation

Open a new terminal and run:

```bash title=Terminal
java -version
javac -version
```

You should see something like:

```text title=Output
openjdk 21.0.5 2025-10-21
javac 21.0.5
```

## Step 3 - Check your PATH

The `java` and `javac` commands must be on your system `PATH`.

- **Windows:** `System Properties > Environment Variables` - ensure `%JAVA_HOME%\bin` is in `Path`.
- **macOS/Linux:** add to `~/.bashrc` or `~/.zshrc`:

```bash title=~/.bashrc
export JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64
export PATH="$JAVA_HOME/bin:$PATH"
```

Then `source ~/.bashrc` and check again.

## Step 4 - Your first program

Create a file named `Hello.java`:

```java title=Hello.java
public class Hello {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
        System.out.println("Java is running!");
    }
}
```

Compile and run it:

```bash title=Terminal
javac Hello.java
java Hello
```

```text title=Output
Hello, World!
Java is running!
```

> **Remember:** `javac Hello.java` creates `Hello.class` (bytecode). `java Hello` runs it - note you pass the *class name*, not the file name, and no `.class` extension.

## Command-line cheat sheet

| Command | What it does |
|---|---|
| `javac File.java` | Compile source to bytecode |
| `java ClassName` | Run a class that has `main` |
| `java -cp dir ClassName` | Run with an extra classpath folder |
| `jar -cf app.jar *.class` | Package classes into a jar |
| `java -jar app.jar` | Run a packaged application |

## Choosing an IDE

You can use any text editor, but an IDE makes Java much easier:

- **IntelliJ IDEA** (Community, free) - most popular for Java
- **Eclipse** - free and extensible
- **VS Code** - lightweight, with the Extension Pack for Java

For this tutorial, an IDE is optional - every example runs with plain `javac`/`java`.

> **Tip:** Enable *format on save* and *auto-import* in your IDE early; they remove 90% of beginner friction.

Next: understand [how Java actually works](how-java-works.html) under the hood.
