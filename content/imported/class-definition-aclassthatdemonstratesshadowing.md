---
title: A Class that Demonstrates Shadowing
nav: A Class that Demonstrates ...
description: Imported from the java2s.com archive: A Class that Demonstrates Shadowing
section: Imported - java2s Archive
order: 1197
source: https://web.archive.org/web/20140829081255/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/AClassthatDemonstratesShadowing.htm
---
```java title=Example.java
public class MainClass {
  static int x;
  public static void main(String[] args) {
    x = 5;
    System.out.println("x = " + x);
    int x;
    x = 10;
    System.out.println("x = " + x);
    System.out.println("ShadowApp.x = " + ShadowApp.x);
  }
}
```

| 5.4.1. | Scope class demonstrates field and local variable scopes |
|---|---|
| 5.4.2. | Dynamically changing the behavior of an object via composition (the 'State' design pattern) |
| 5.4.3. | Scope for Class and Local Variables |
| 5.4.4. | A Class that Demonstrates Shadowing |
