---
title: Java Algorithms How to - Get random boolean
nav: Java Algorithms How to - G...
description: Imported from the java2s.com archive: Java Algorithms How to - Get random boolean
section: Imported - java2s Archive
order: 1010
source: https://web.archive.org/web/20160730061924/http://www.java2s.com:80/Tutorials/Java/Algorithms_How_to/Random/Get_random_boolean.htm
---
```java title=Example.java
Back to Random  ↑
```

## Question

We would like to know how to get random boolean.

## Answer

```java title=Example.java
import java.util.Random;
publicclass Main {
  publicstaticfinalvoid main(String... args) {
    Random randomGenerator = new Random();
    for (int idx = 1; idx <= 10; ++idx) {
      boolean randomBool = randomGenerator.nextBoolean();
      System.out.println("Generated : " + randomBool);
    }
  }
}
```

```java title=Example.java
Back to Random  ↑
```
