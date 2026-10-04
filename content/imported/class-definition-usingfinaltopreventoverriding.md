---
title: Using final to Prevent Overriding
nav: Using final to Prevent Ove...
description: Imported from the java2s.com archive: Using final to Prevent Overriding
section: Imported - java2s Archive
order: 1136
source: https://web.archive.org/web/20140829082700/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/UsingfinaltoPreventOverriding.htm
---
```java title=Example.java
class A {
  final void meth() {
    System.out.println("This is a final method.");
  }
}
class B extends A {
  void meth() { // ERROR! Can't override.
    System.out.println("Illegal!");
  }
}
```
