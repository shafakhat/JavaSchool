---
title: Java Algorithms How to - Toss Coin
nav: Java Algorithms How to - T...
description: Imported from the java2s.com archive: Java Algorithms How to - Toss Coin
section: Imported - java2s Archive
order: 1014
source: https://web.archive.org/web/20160730060640/http://www.java2s.com:80/Tutorials/Java/Algorithms_How_to/Random/Toss_Coin.htm
---
```java title=Example.java
Back to Random  ↑
```

## Question

We would like to know how to toss Coin.

## Answer

```java title=Example.java
import java.util.Random;
class Coin {
  public String toss() {
    Random myRand = new Random();
    int face = myRand.nextInt(2);
    if (face == 0) {
      return"heads";
    } else {
      return"tails";
    }
  }
}
publicclass Main {
  publicstaticvoid main(String[] args) {
    Coin coin = new Coin();
    int headsCount = 0;
    int tailsCount = 0;
    for (int i = 1; i <= 40; i++) {
      if (coin.toss().equals("heads")) {
        headsCount++;
      } else {
        tailsCount++;
      }
    }
    System.out.println("Total number of heads: " + headsCount
        + "\nTotal number of tails: " + tailsCount);
  }
}
```

The code above generates the following result.

```java title=Example.java
Back to Random  ↑
```
