---
title: Java Algorithms How to - Divide a number into smaller random ints
nav: Java Algorithms How to - D...
description: We would like to know how to divide a number into smaller random ints.
section: Imported - java2s Archive
order: 1025
source: https://web.archive.org/web/20160730062906/http://www.java2s.com:80/Tutorials/Java/Algorithms_How_to/Random/Divide_a_number_into_smaller_random_ints.htm
---
```java title=Example.java
Back to Random  ↑
```

## Question

We would like to know how to divide a number into smaller random ints.

## Answer

```java title=Example.java
import java.util.Arrays;
import java.util.HashSet;
import java.util.Random;
publicclass Main {
   publicstatic Random r = new Random();
   publicstaticint[] divide(int number, int number_of_parts) {
      HashSet<Integer> uniqueInts = new HashSet<Integer>();
      uniqueInts.add(0);
      uniqueInts.add(number);
      int array_size = number_of_parts + 1;
      while (uniqueInts.size() < array_size) {
         uniqueInts.add(1 + r.nextInt(number - 1));
      }
      Integer[] dividers = uniqueInts.toArray(newInteger[array_size]);
      Arrays.sort(dividers);
      int[] results = newint[number_of_parts];
      for(int i = 1, j = 0; i < dividers.length; ++i, ++j) {
         results[j] = dividers[i] - dividers[j];
      }
      return results;
   }
   publicstaticvoid main(String[] args) {
      System.out.println(Arrays.toString(divide(12, 5)));
   }
}
```

The code above generates the following result.

```java title=Example.java
Back to Random  ↑
```
