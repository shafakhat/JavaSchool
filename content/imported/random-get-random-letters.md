---
title: Java Algorithms How to - Get random letters
nav: Java Algorithms How to - G...
description: System.out.println("" + pickRandom("ACEGIKMOQSUWY".toCharArray())
section: Imported - java2s Archive
order: 1011
source: https://web.archive.org/web/20160730061312/http://www.java2s.com:80/Tutorials/Java/Algorithms_How_to/Random/Get_random_letters.htm
---
## Question

We would like to know how to get random letters.

## Answer

```java title=Example.java
import java.util.Random;
publicclass Main {
  static Random r = new Random();
  staticchar pickRandom(char... letters) {
    return letters[r.nextInt(letters.length)];
  }
  publicstaticvoid main(String args[]) {
    for (int i = 0; i < 10; i++) {
      System.out.println("" + pickRandom("ACEGIKMOQSUWY".toCharArray())
          + pickRandom("BDFHJLNPRVXZ".toCharArray())
          + pickRandom("ABCDEFGHJKLMOPQRSTVWXYZ".toCharArray()));
    }
  }
}
```

The code above generates the following result.
