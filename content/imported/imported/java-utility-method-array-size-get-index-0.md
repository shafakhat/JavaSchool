---
title: Java Utililty Methods Array Size Get
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Size Get are organized into topic(s).
section: Imported - java2s Archive
order: 50105
source: https://www.java2s.com/example/java-utility-method/array-size-get-index-0.html
---
List of utility methods to do Array Size Get

## Description

The list of methods to do Array Size Get are organized into topic(s).

## Method

intarraySize(final int expected, final float f) array Size

```java title=Example.java
finallong s = Math.max(2L, nextPowerOfTwo((long) Math.ceil((double) ((float) expected / f))));
if (s > 1073741824L) {
    thrownewIllegalArgumentException(
            "Too large (" + expected + " expected elements with load factor " + f + ")");
} else {
    return (int) s;
```

intarraySize(final int expected, final float f) Returns the least power of two smaller than or equal to 230 and larger than or equal to

```java title=Example.java
Math.ceil( expected / f )
```

.

```java title=Example.java
finallong s = nextPowerOfTwo((long) Math.ceil(expected / f));
if (s > (1 << 30))
    thrownewIllegalArgumentException(
            "Too large (" + expected + " expected elements with load factor " + f + ")");
return (int) s;
```

longarraySizeOf(int[] array) array Size Of

```java title=Example.java
if (array == null)
    return 0;
return calArraySize(array.length, SIZE_OF_INT);
```

[HOME](https://www.java2s.com/) | Copyright © www.java2s.com 2016
