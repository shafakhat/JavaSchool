---
title: Relational and logical operators
nav: Relational and logical ope...
description: System.out.println("(i < 10) && (j < 10) is " + ((i < 10) && (j < 10)));
section: Imported - java2s Archive
order: 1047
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0060__Operators/Relationalandlogicaloperators.htm
---
```java title=Example.java
import java.util.Random;
publicclass MainClass {
  publicstaticvoid main(String[] args) {
    Random rand = new Random();
    int i = rand.nextInt(100);
    int j = rand.nextInt(100);
    System.out.println("i = " + i);
    System.out.println("j = " + j);
    System.out.println("i > j is " + (i > j));
    System.out.println("i < j is " + (i < j));
    System.out.println("i >= j is " + (i >= j));
    System.out.println("i <= j is " + (i <= j));
    System.out.println("i == j is " + (i == j));
    System.out.println("i != j is " + (i != j));
    System.out.println("(i < 10) && (j < 10) is " + ((i < 10) && (j < 10)));
    System.out.println("(i < 10) || (j < 10) is " + ((i < 10) || (j < 10)));
  }
}
```

```java title=Example.java
i = 92
j = 22
i > j is true
i < j is false
i >= j is true
i <= j is false
i == j is false
i != j is true
(i < 10) && (j < 10) is false
(i < 10) || (j < 10) is false
```
