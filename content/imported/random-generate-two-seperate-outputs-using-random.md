---
title: Java Algorithms How to - Generate two seperate outputs using Random
nav: Java Algorithms How to - G...
description: We would like to know how to generate two seperate outputs using Random.
section: Imported - java2s Archive
order: 1008
source: https://web.archive.org/web/20160730060630/http://www.java2s.com:80/Tutorials/Java/Algorithms_How_to/Random/Generate_two_seperate_outputs_using_Random.htm
---
## Question

We would like to know how to generate two seperate outputs using Random.

## Answer

```java title=Example.java
import java.util.Random;
publicclass Main {
  privatestaticfinal Random rand = new Random();
  publicstaticvoid main(String[] args) {
    int i = 1;
    while (i <= 100) {
      System.out.printf("%-5d", rand.nextInt(4) + 4);
      if (i % 10 == 0) {
        System.out.println();
      }
      i++;
    }
    System.out.println();
    i = 1;// modified here
while (i <= 100) {
      System.out.printf("%-5d", rand.nextInt(10 * (80) + 10));
      if (i % 10 == 0) {
        System.out.println();
      }
      i++;
    }
  }
}
```

The code above generates the following result.
