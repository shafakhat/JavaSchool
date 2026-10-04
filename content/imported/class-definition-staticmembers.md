---
title: Static Members
nav: Static Members
description: the method main(the entry point to a class) is static because it must be called before any object is created.
section: Imported - java2s Archive
order: 1049
source: https://web.archive.org/web/20070711190542/http://www.java2s.com:80/Tutorial/Java/0100__Class-Definition/StaticMembers.htm
---
- Static members are not tied to class instances.
- Static members can be called without having an instance.

The out field in java.lang.System is static.

```java title=Example.java
public class MainClass {
  public static void main() {
    System.out.println("123");
  }
}
```

the method main(the entry point to a class) is static because it must be called before any object is created.
