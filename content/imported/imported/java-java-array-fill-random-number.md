---
title: Java array fill random number
nav: Java array fill random num...
description: Imported from the java2s.com archive: Java array fill random number
section: Imported - java2s Archive
order: 1105
source: https://web.archive.org/web/20210102113255/http://www.java2s.com/ref/java/java-array-fill-random-number.html
---
## Description

```java title=Example.java
import java.util.Arrays;
import java.util.Random;

publicclass Main {

  publicstaticvoid main(String args[]) {
    int[] anArray = newint[10];
    Random rand = newRandom();
    /*fromwww.java2s.com*/for (int i = 0; i < 10; i++) {
      anArray[i] = rand.nextInt();
    }

    System.out.println(Arrays.toString(anArray));
  }

}
```

PreviousNext

## Related

- Java array copy to double its size
- Java array copy to merge two arrays
- Java array copy using System.arraycopy()
- Java array fill random number within a range
- Java array fill unique random number
