---
title: Java Algorithms How to - Generate random float number within -1 and 1
nav: Java Algorithms How to - G...
description: We would like to know how to generate random float number within -1 and 1.
section: Imported - java2s Archive
order: 1002
source: https://web.archive.org/web/20160730055229/http://www.java2s.com:80/Tutorials/Java/Algorithms_How_to/Random/Generate_random_float_number_within_1_and_1.htm
---
```java title=Example.java
Back to Random  ↑
```

## Question

We would like to know how to generate random float number within -1 and 1.

## Answer

```java title=Example.java
import java.util.Random;
/*fromwww.java2s.com*/publicclass Main {
  publicstaticvoid main(String[] args) {
    Random random = new Random();
    for (int i = 0; i < 1000000000; i++) {
      float f = random.nextFloat() * 2 - 1;
      if (Float.isNaN(f)) {
        System.out.println("NaN!");
      }
    }
  }
}
```

```java title=Example.java
Back to Random  ↑
```
