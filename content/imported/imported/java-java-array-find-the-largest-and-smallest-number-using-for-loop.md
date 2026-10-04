---
title: Java array find the largest and smallest number using for loop
nav: Java array find the larges...
description: Java array find the largest and smallest number using for loop
section: Imported - java2s Archive
order: 1108
source: https://web.archive.org/web/20210102113255/http://www.java2s.com/ref/java/java-array-find-the-largest-and-smallest-number-using-for-loop.html
---
## Description

```java title=Example.java
import java.util.Arrays;
import java.util.Random;

publicclass Main {

  publicstaticvoid main(String[] args) {
    int[] a = newint[10];
    /*www.java2s.com*/int min = Integer.MAX_VALUE;
    int max = Integer.MIN_VALUE;

    for (int i = 0; i < a.length; i++) {
      a[i] = newRandom().nextInt(100);
    }
    System.out.println(Arrays.toString(a));

    for (int i = 0; i < a.length; i++) {
      if (a[i] < min)
        min = a[i];
      if (a[i] > max)
        max = a[i];
    }
    System.out.println("Min is: " + min + " " + "Max is: " + max);
  }
}
```

PreviousNext

## Related

- Java array fill random number
- Java array fill random number within a range
- Java array fill unique random number
- Java array find the max and min value via Collections.min/max
- Java array find the max and min value via sorting
