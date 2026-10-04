---
title: Multiple selections
nav: Multiple selections
description: If there are multiple selections, you can also use if with a series of else statements.
section: Imported - java2s Archive
order: 1166
source: https://web.archive.org/web/20140829084742/http://www.java2s.com/Tutorial/Java/0080__Statement-Control/Multipleselections.htm
---
If there are multiple selections, you can also use if with a series of else statements.

```java title=Example.java
if (booleanExpression1) {
    // statements
} else if (booleanExpression2) {
    // statements
}
...
else {
    // statements
}
```

For example:

```java title=Example.java
public class MainClass {
  public static void main(String[] args) {
    int a = 0;
    if (a == 1) {
      System.out.println("one");
    } else if (a == 2) {
      System.out.println("two");
    } else if (a == 3) {
      System.out.println("three");
    } else {
      System.out.println("invalid");
    }
  }
}
```
