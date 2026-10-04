---
title: Java array clone
nav: Java array clone
description: String[] array2 = { "CSS", "HTML", "Java", "Javascript", "SQL", "C++", "C" };
section: Imported - java2s Archive
order: 1099
source: https://web.archive.org/web/20210102113254/http://www.java2s.com/ref/java/java-array-clone.html
---
## Description

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String args[]) {
    int[] array1 = { 1, 2, 3, 4, 5 };

    String[] array2 = { "CSS", "HTML", "Java", "Javascript", "SQL", "C++", "C" };

    System.out.println("Original size: " + array1.length);
    System.out.println("New size: " + cloneArray(array1).length);

    System.out.println("Original size: " + array2.length);
    System.out.println("New size: " + cloneArray(array2).length);
  }//www.java2s.comstaticint[] cloneArray(int[] original) {
    return (int[]) original.clone();
  }

  static <T> T[] cloneArray(T original[]) {
    return (T[]) original.clone();
  }
}
```

PreviousNext

## Related

- Java Array append a char to char array
- Java Array append String to String array
- Java array append new element
- Java array convert to List
- Java array copy to double its size
