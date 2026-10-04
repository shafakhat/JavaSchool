---
title: Java Array append a char to char array
nav: Java Array append a char t...
description: char[] c = newchar[] { 'd', 'e', 'm', 'o', '2', 's', '.', 'c', 'o', 'm' };
section: Imported - java2s Archive
order: 1096
source: https://web.archive.org/web/20210102113253/http://www.java2s.com/ref/java/java-array-append-a-char-to-char-array.html
---
## Description

```java title=Example.java
//package com.demo2s;publicclass Main {
    publicstaticvoid main(String[] argv) throwsException {
        char[] c = newchar[] { 'd', 'e', 'm', 'o', '2', 's', '.', 'c', 'o', 'm' };
        char toAdd = 'a';
        System.out.println(java.util.Arrays.toString(addChar(c, toAdd)));
    }/*fromwww.java2s.com*//**
     * Adds a char to an array of chars and returns the new array.
     *
     * @param c The chars to where the new char should be appended
     * @param toAdd the char to be added
     * @return a new array with the passed char appended.
     */publicstaticchar[] addChar(char[] c, char toAdd) {
        char[] c1 = newchar[c.length + 1];

        System.arraycopy(c, 0, c1, 0, c.length);
        c1[c.length] = toAdd;
        return c1;

    }
}
```

PreviousNext

## Related

- Java Array multidimensional Arrays reference element
- Java Array search unsorted array for a value using for each loop
- Java array check if an array of primitive chars is empty or null.
- Java Array append String to String array
- Java array append new element
