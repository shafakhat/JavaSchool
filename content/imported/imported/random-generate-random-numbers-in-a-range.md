---
title: Java Algorithms How to - Generate Random numbers in a range
nav: Java Algorithms How to - G...
description: We would like to know how to generate Random numbers in a range.
section: Imported - java2s Archive
order: 1004
source: https://web.archive.org/web/20160730060903/http://www.java2s.com:80/Tutorials/Java/Algorithms_How_to/Random/Generate_Random_numbers_in_a_range.htm
---
```java title=Example.java
Back to Random  ↑
```

## Question

We would like to know how to generate Random numbers in a range.

## Answer

```java title=Example.java
import java.util.Random;
/*www.java2s.com*/publicclass Main {
  publicstaticvoid main(String[] args) {
    int randomNumberBetween1To100 = getRandom(0, 100);
    System.out.println("Random number between 1 to 100 is: "
        + randomNumberBetween1To100);
  }

  publicstaticint getRandom(int minNumber, int maxNumber) {
    Random rand = new Random();
    int randomNum = rand.nextInt(maxNumber - minNumber);
    return randomNum;
  }
}
```

The code above generates the following result.

```java title=Example.java
Back to Random  ↑
```
