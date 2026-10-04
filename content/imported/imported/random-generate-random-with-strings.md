---
title: Java Algorithms How to - Generate random with strings
nav: Java Algorithms How to - G...
description: System.out.println("Random String selected: " + arr[select]);
section: Imported - java2s Archive
order: 1007
source: https://web.archive.org/web/20160730061920/http://www.java2s.com:80/Tutorials/Java/Algorithms_How_to/Random/Generate_random_with_strings.htm
---
```java title=Example.java
Back to Random  ↑
```

## Question

We would like to know how to generate random with strings.

## Answer

```java title=Example.java
import java.util.Random;
//fromwww.java2s.compublicclass Main {

  publicstaticvoid main(String[] args) {

    String[] arr = { "A", "B", "C", "D" };
    Random random = new Random();

    int select = random.nextInt(arr.length);

    System.out.println("Random String selected: " + arr[select]);
  }
}
```

The code above generates the following result.

```java title=Example.java
Back to Random  ↑
```
