---
title: Java Algorithms How to - Generate a random number from an array
nav: Java Algorithms How to - G...
description: We would like to know how to generate a random number from an array.
section: Imported - java2s Archive
order: 1000
source: https://web.archive.org/web/20160730060908/http://www.java2s.com:80/Tutorials/Java/Algorithms_How_to/Random/Generate_a_random_number_from_an_array.htm
---
```java title=Example.java
Back to Random  ↑
```

## Question

We would like to know how to generate a random number from an array.

## Answer

```java title=Example.java
import java.util.Random;
publicclass Main {
  publicstaticvoid main(String... args) {
    int[] data = newint[] { 1, 2, 2, 2, 3, 3, 4, 5, 5, 5, 5, 5, 5 };
    System.out.print(data[new Random().nextInt(data.length)]);
  }
}
```

The code above generates the following result.

```java title=Example.java
Back to Random  ↑
```
