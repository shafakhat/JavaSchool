---
title: Java array fill unique random number
nav: Java array fill unique ran...
description: //check if the check array index has been set//if set regenerate while (check[rnd]) {
section: Imported - java2s Archive
order: 1106
source: https://web.archive.org/web/20210102113255/http://www.java2s.com/ref/java/java-array-fill-unique-random-number.html
---
## Description

```java title=Example.java
import java.util.Arrays;
import java.util.Random;

publicclass Main {
  publicstaticint[] uniqueRandom(int length) {
    Random rand = newRandom();
    int[] nums = newint[length];
    //fromwww.java2s.comboolean[] check = newboolean[length];

    for (int k = 0; k < length; k++) {
      int rnd = rand.nextInt(length);
      //check if the check array index has been set//if set regenerate while (check[rnd]) {
        rnd = rand.nextInt(length);
      }
      nums[k] = rnd;
      check[rnd] = true;
    }
    return nums;
  }
  publicstaticvoid main(String args[]) {
    int length = 10;
    int[] a = uniqueRandom(length);
    System.out.println(Arrays.toString(a));

  }
}
```

PreviousNext

## Related

- Java array copy using System.arraycopy()
- Java array fill random number
- Java array fill random number within a range
- Java array find the largest and smallest number using for loop
- Java array find the max and min value via Collections.min/max
