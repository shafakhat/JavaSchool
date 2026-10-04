---
title: Java Utililty Methods Array Cast
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Cast are organized into topic(s).
section: Imported - java2s Archive
order: 50034
source: https://www.java2s.com/example/java-utility-method/array-cast-index-0.html
---
List of utility methods to do Array Cast

## Description

The list of methods to do Array Cast are organized into topic(s).

## Method

double[]arrayCastToDouble(int[] arrayInt) array Cast To Double

```java title=Example.java
double[] arrayDouble = newdouble[arrayInt.length];
for (int i = 0; i < arrayDouble.length; i++)
    arrayDouble[i] = (double) arrayInt[i];
return arrayDouble;
```

int[]arrayCastToInt(double[] a) array Cast To Int

```java title=Example.java
int[] b = newint[a.length];
for (int i = 0; i < b.length; i++)
    b[i] = (int) a[i];
return b;
```

[HOME](https://www.java2s.com/) | Copyright © www.java2s.com 2016
