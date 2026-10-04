---
title: Java Utililty Methods Array Deep Copy
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Deep Copy are organized into topic(s).
section: Imported - java2s Archive
order: 50048
source: https://www.java2s.com/example/java-utility-method/array-deep-copy-index-0.html
---
List of utility methods to do Array Deep Copy

## Description

The list of methods to do Array Deep Copy are organized into topic(s).

## Method

int[][]deep_copy(int M[][]) Deep Copy - Make a deep copy of M[][].

```java title=Example.java
int[][] C = newint[M.length][];
for (int i = 0; i < C.length; i++) {
    C[i] = Arrays.copyOf(M[i], M[i].length);
return C;
```

double[][]deepArrayCopy(double[][] original) deep Array Copy

```java title=Example.java
double[][] copy = original.clone();
for (int i = 0; i < copy.length; i++) {
    copy[i] = copy[i].clone();
return copy;
```

double[][]deepArrayCopy(double[][] original) deep Array Copy

```java title=Example.java
double[][] copy = newdouble[original.length][original[0].length];
for (int i = 0; i < copy.length; i++) {
    copy[i] = Arrays.copyOf(original[i], original[i].length);
return copy;
```

double[][]deepArrayCopy(double[][] original) deep Array Copy

```java title=Example.java
double[][] copy = newdouble[original.length][original[0].length];
for (int i = 0; i < copy.length; i++) {
    copy[i] = Arrays.copyOf(original[i], original[i].length);
return copy;
```

double[][]deepClone(double[][] ary) deep Clone

```java title=Example.java
double[][] res = ary.clone();
for (int i = 0; i < res.length; ++i)
    res[i] = ary[i].clone();
return res;
```

int[][]deepClone(int[][] source) deep Clone

```java title=Example.java
int[][] result = newint[source.length][];
for (int i = 0; i < source.length; i++)
    result[i] = source[i].clone();
return result;
```

byte[]deepCopy(byte[] org) deep Copy

```java title=Example.java
if (org == null)
    return null;
byte[] result = newbyte[org.length];
System.arraycopy(org, 0, result, 0, org.length);
return result;
```

double[][]deepCopy(double[][] in) deep Copy

```java title=Example.java
double[][] out = newdouble[in.length][in[0].length];
for (int i = 0; i < in.length; i++)
    for (int j = 0; j < in[0].length; j++) {
        out[i][j] = in[i][j];
return out;
```

StringdeepCopy(final String s) Does an deep copy of the input string and returns so

```java title=Example.java
input != (return value)
```

```java title=Example.java
returnnewString(s);
```

int[]deepCopy(int[] array) deep Copy

```java title=Example.java
int[] copy = newint[array.length];
for (int i = 0; i < array.length; i++) {
    copy[i] = array[i];
return copy;
```
