---
title: Java Algorithms How to - Generate Random Number Between Two Given Values
nav: Java Algorithms How to - G...
description: We would like to know how to generate Random Number Between Two Given Values.
section: Imported - java2s Archive
order: 1003
source: https://web.archive.org/web/20160730061302/http://www.java2s.com:80/Tutorials/Java/Algorithms_How_to/Random/Generate_Random_Number_Between_Two_Given_Values.htm
---
```java title=Example.java
Back to Random  ↑
```

## Question

We would like to know how to generate Random Number Between Two Given Values.

## Answer

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
    int n1 = 1;/*fromwww.java2s.com*/int n2 = 100;
    double Random;

    Random = n2 + (Math.random() * (n1 - n2));
    System.out.println("Your random number is: " + Random);
  }
}
```

The code above generates the following result.

```java title=Example.java
Back to Random  ↑
```
