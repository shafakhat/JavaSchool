---
title: Logical OR Operations
nav: Logical OR Operations
description: The logical OR, ||, omits the evaluation of the right-hand operand when the left-hand operand is true.
section: Imported - java2s Archive
order: 1046
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0060__Operators/LogicalOROperations.htm
---
The logical OR, ||, omits the evaluation of the right-hand operand when the left-hand operand is true.

```java title=Example.java
publicclass MainClass {
  publicstaticvoid main(String[] arg) {
    int value = 8;
    int count = 10;
    int limit = 11;
    if (++value % 2 == 0 | ++count < limit) {
      System.out.println("here");
      System.out.println(value);
      System.out.println(count);
    }
    System.out.println("there");
    System.out.println(value);
    System.out.println(count);
  }
}
java title=Example.java
there
9
11
```
