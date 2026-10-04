---
title: Java Algorithms How to - Generate 100 random 3 digit numbers
nav: Java Algorithms How to - G...
description: We would like to know how to generate 100 random 3 digit numbers.
section: Imported - java2s Archive
order: 1027
source: https://web.archive.org/web/20160730061625/http://www.java2s.com:80/Tutorials/Java/Algorithms_How_to/Random/Generate_100_random_3_digit_numbers.htm
---
## Question

We would like to know how to generate 100 random 3 digit numbers.

## Answer

```java title=Example.java
import java.util.Random;
publicclass Main {
  publicstaticvoid main(String[] args) {
    Random rand = new Random();
    for (int i = 1; i <= 100; i++) {
      int randomNum = rand.nextInt((999 - 100) + 1) + 100;
      System.out.println(randomNum);
    }
  }
}
```

The code above generates the following result.
