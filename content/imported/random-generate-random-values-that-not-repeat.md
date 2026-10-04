---
title: Java Algorithms How to - Generate random values that not repeat
nav: Java Algorithms How to - G...
description: We would like to know how to generate random values that not repeat.
section: Imported - java2s Archive
order: 1006
source: https://web.archive.org/web/20160730060913/http://www.java2s.com:80/Tutorials/Java/Algorithms_How_to/Random/Generate_random_values_that_not_repeat.htm
---
```java title=Example.java
Back to Random  ↑
```

## Question

We would like to know how to generate random values that not repeat.

## Answer

```java title=Example.java
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Random;
import java.util.Set;
publicclass Main {
  publicstaticvoid main(String[] args) {
    Random random = new Random();
    Set<Integer> set = new HashSet<Integer>();
    while (set.size() < 5) {
      set.add(random.nextInt());
    }
    List<Integer> result = new ArrayList<Integer>(set);
    System.out.println(result);
  }
}
```

The code above generates the following result.

```java title=Example.java
Back to Random  ↑
```
