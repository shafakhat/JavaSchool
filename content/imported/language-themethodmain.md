---
title: The Method main
nav: The Method main
description: All arguments must be passed as strings. For instance, to pass two arguments, "1" and "mode" when running the Test class, you type this:
section: Imported - java2s Archive
order: 1013
source: https://web.archive.org/web/20070513042831/http://www.java2s.com:80/Tutorial/Java/0020__Language/TheMethodmain.htm
---
- A special method called main provides the entry point to an application.
- An application can have many classes and only one of the classes needs to have the method main.
- This method allows the class containing it to be invoked.

The signature of the method main is as follows.

```java title=Example.java
public class MainClass {
  public static void main(String[] args) {
  }
}
```

- In addition, you can pass arguments to main when using 'java' to run a class.
- To pass arguments, type them after the class name. Two arguments are separated by a space.

```java title=Example.java
java className arg1 arg2 arg3 ...
```

All arguments must be passed as strings. For instance, to pass two arguments, "1" and "mode" when running the Test class, you type this:

```java title=Example.java

java Test 1 mode
```
