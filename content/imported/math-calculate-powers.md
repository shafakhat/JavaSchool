---
title: Java Algorithms How to - Calculate powers
nav: Java Algorithms How to - C...
description: Imported from the java2s.com archive: Java Algorithms How to - Calculate powers
section: Imported - java2s Archive
order: 1009
source: https://web.archive.org/web/20160729085535/http://www.java2s.com:80/Tutorials/Java/Algorithms_How_to/Math/Calculate_powers.htm
---
```java title=Example.java
Back to Math  ↑
```

## Question

We would like to know how to calculate powers.

## Answer

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String args[]) {
    int num = 2;int pow = 3;
    System.out.print(power(num, pow));
  }
  publicstaticint power(int a, int b) {
    int power = 1;
    for (int c = 0; c < b; c++)
      power *= a;
    return power;
  }
}
```

The code above generates the following result.

```java title=Example.java
Back to Math  ↑
```
