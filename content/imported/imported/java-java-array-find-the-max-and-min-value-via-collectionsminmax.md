---
title: Java array find the max and min value via Collections.min/max
nav: Java array find the max an...
description: Java array find the max and min value via Collections.min/max
section: Imported - java2s Archive
order: 1109
source: https://web.archive.org/web/20210102113255/http://www.java2s.com/ref/java/java-array-find-the-max-and-min-value-via-collectionsminmax.html
---
## Description

```java title=Example.java
import java.util.Arrays;
import java.util.Collections;

publicclass Main {
  publicstaticvoid main(String[] args) {
    Integer[] numbers = { 1238, 3212, 1236, 7321, 3450, 1345, 3454, 9, 5435, 1233 };

    System.out.println(Arrays.toString(numbers));
    //fromwww.java2s.comint min = (int) Collections.min(Arrays.asList(numbers));
    int max = (int) Collections.max(Arrays.asList(numbers));

    System.out.println("Min number: " + min);
    System.out.println("Max number: " + max);
  }
}
```

PreviousNext

## Related

- Java array fill random number within a range
- Java array fill unique random number
- Java array find the largest and smallest number using for loop
- Java array find the max and min value via sorting
- Java array get random element
