---
title: Java Array display arrays
nav: Java Array display arrays
description: To print an array, print each element in the array using a loop like the following:
section: Imported - java2s Archive
order: 1103
source: https://web.archive.org/web/20210102113249/http://www.java2s.com/ref/java/java-array-display-arrays.html
---
## Introduction

To print an array, print each element in the array using a loop like the following:

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
    int[] array = newint[5];
    for (int i = 0; i < array.length; i++) {
      array[i] = (int)(Math.random() * 100);
    } for (int i = 0; i < array.length; i++) {
      System.out.print(array[i] + " ");
    }
  }
}
```

PreviousNext

## Related

- Java Array length property
- Java Array as frequency counters
- Java Array count occurrences of letter in char array
- Java Array find array element above average
- Java Array find the largest element
