---
title: Java Algorithms How to - Generate a random -1 or 1
nav: Java Algorithms How to - G...
description: Imported from the java2s.com archive: Java Algorithms How to - Generate a random -1 or 1
section: Imported - java2s Archive
order: 1028
source: https://web.archive.org/web/20160730061307/http://www.java2s.com:80/Tutorials/Java/Algorithms_How_to/Random/Generate_a_random_1_or_1.htm
---
```java title=Example.java
Back to Random  ↑
```

## Question

We would like to know how to generate a random -1 or 1.

## Answer

```java title=Example.java
//fromwww.java2s.comimport java.util.Random;

publicclass Main {
  publicstaticvoid main(String[] args) {
    for (int i = 0; i < 100; i++) {
      System.out.println(randomOneOrMinusOne());
    }
  }
  staticint randomOneOrMinusOne() {
    Random rand = new Random();
    if (rand.nextBoolean())
      return 1;
    elsereturn -1;
  }
}
```

The code above generates the following result.

```java title=Example.java
Back to Random  ↑
```
