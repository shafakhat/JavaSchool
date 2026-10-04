---
title: Java Algorithms Search Linear Search
nav: Java Algorithms Search Lin...
description: The linear search compares the key element sequentially with each element in the array.
section: Imported - java2s Archive
order: 1033
source: https://web.archive.org/web/20210102113327/http://www.java2s.com/ref/java/java-algorithms-search-linear-search.html
---
## Introduction

The linear search compares the key element sequentially with each element in the array.

It continues to do so until the key matches an element in the array or the array is exhausted.

- If a match is found, the linear search returns the index of the element in the array that matches the key.
- If no match is found, the search returns -1.

```java title=Example.java
publicclass Main {
  /** The method for finding a key in the list */publicstaticint linearSearch(int[] list, int key) {
    for (int i = 0; i < list.length; i++) {
      if (key == list[i])
        return i;
    }return -1;
  }
  publicstaticvoid main(String[] args) {
    int[] list = { 11, 14, 4, 12, 5, -3, 16, 2 };
    int i = linearSearch(list, 4);
    System.out.println(i);
    int j = linearSearch(list, -4);
    System.out.println(j);
    int k = linearSearch(list, -3);
    System.out.println(k);
  }
}
```

PreviousNext

## Related
