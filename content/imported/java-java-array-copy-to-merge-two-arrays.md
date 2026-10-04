---
title: Java array copy to merge two arrays
nav: Java array copy to merge t...
description: Imported from the java2s.com archive: Java array copy to merge two arrays
section: Imported - java2s Archive
order: 1101
source: https://web.archive.org/web/20210102113254/http://www.java2s.com/ref/java/java-array-copy-to-merge-two-arrays.html
---
## Description

```java title=Example.java
import java.util.Arrays;
publicclass Main {
  publicstaticvoid main(String[] args) {
    String[] names = newString[] { "HTML", "CSS", "SQL" };
    String[] extended = newString[5];
    extended[0] = "0";
    extended[1] = "1";
    extended[2] = "2";
    extended[3] = "3";
    extended[4] = "4";
    System.arraycopy(names, 0, extended, 0, names.length);
    System.out.println(Arrays.toString(names));
    System.out.println(Arrays.toString(extended));
  }
}
```

PreviousNext

## Related

- Java array clone
- Java array convert to List
- Java array copy to double its size
- Java array copy using System.arraycopy()
- Java array fill random number
