---
title: Java array fill random number within a range
nav: Java array fill random num...
description: Imported from the java2s.com archive: Java array fill random number within a range
section: Imported - java2s Archive
order: 1104
source: https://web.archive.org/web/20210102113255/http://www.java2s.com/ref/java/java-array-fill-random-number-within-a-range.html
---
## Description

```java title=Example.java
import java.util.Arrays;
import java.util.Random;
publicclass Main {
  publicstaticvoid main(String[] args) {
    int[] array = newint[10];
    Random rand = newRandom();
    for (int i = 0; i < array.length; i++) {
      array[i] = rand.nextInt(10);
    }
    System.out.println(Arrays.toString(array));
  }
}
```

PreviousNext

## Related

- Java array copy to merge two arrays
- Java array copy using System.arraycopy()
- Java array fill random number
- Java array fill unique random number
- Java array find the largest and smallest number using for loop
