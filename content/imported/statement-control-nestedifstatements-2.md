---
title: Nested if Statements
nav: Nested if Statements
description: Imported from the java2s.com archive: Nested if Statements
section: Imported - java2s Archive
order: 1061
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0080__Statement-Control/NestedifStatements.htm
---
```java title=Example.java
publicclass MainClass {
  publicstaticvoid main(String[] arg) {
    int a = 2;
    if (a == 0) {
      System.out.println("in the block");
      if (a == 2) {
        System.out.println("a is 0");
      } else {
        System.out.println("a is not 2");
      }
    } else {
      System.out.println("a is not 0");
    }
  }
}
```

```java title=Example.java
a is not 0
```
