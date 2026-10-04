---
title: Java Utililty Methods Array Permute
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Permute are organized into topic(s).
section: Imported - java2s Archive
order: 50091
source: https://www.java2s.com/example/java-utility-method/array-permute-index-0.html
---
List of utility methods to do Array Permute

## Description

The list of methods to do Array Permute are organized into topic(s).

## Method

int[]permutation(final int start, final int end) Creates a permutation of all integers in the interval [start, end]

```java title=Example.java
if (start > end)
    returnnewint[0];
finalint length = end - start + 1;
finalint[] r = newint[length];
for (int i = 0; i < length; i++)
    r[i] = start + i;
for (int i = length - 1; i > 0; i--) {
    finalint j = random.nextInt(i + 1);
...
```

int[]permutation(int n) Generates a random permutation of the numbers {0, ..., n-1}

```java title=Example.java
return permutation(n, getRandomGenerator());
```

Object[]permute(int k, Object[] os) permute

```java title=Example.java
for (int j = 2; j <= os.length; j++) {
    k = k / (j - 1);
    Object tmp = os[j - 1];
    os[j - 1] = os[(k % j)];
    os[(k % j)] = tmp;
return os;
```

voidpermute(int[] elements, int i, int j) permute

```java title=Example.java
int temp;
temp = elements[i];
elements[i] = elements[j];
elements[j] = temp;
```

int[]permute(int[] in, int[] idx) permute

```java title=Example.java
int[] out = newint[in.length];
for (int i = 0; i < in.length; i++)
    out[i] = in[idx[i]];
return out;
```

Object[]permute(int[] p, Object[] data, boolean clone) Rearrange the specified data according to the specified permutation.

```java title=Example.java
Object[] permuted = null;
if (clone) {
    permuted = (Object[]) data.clone();
    for (int i = 0; i < data.length; i++)
        permuted[p[i]] = data[i];
} else {
    int i = 0;
    while (i < p.length) {
...
```

voidpermute(String str, int startIndex, int endIndex) Algo {A,B,C} first take index 0 and swap with all A swap with A {A,B,C} ---> now take second char and make first char fixed {A,B,C} and {A,C,B} A swap with B {B,A,C} ---> now take second char and make first char fixed {B,A,C} and {B,C,A} A swap with C {C,B,A} ---> now take second char and make first char fixed {C,B,A} and {C,A,B} now take second char on each

```java title=Example.java
if (startIndex == endIndex) {
    System.out.println(str);
} else {
    for (int i = startIndex; i <= endIndex; i++) {
        str = swap(str, startIndex, i);
        permute(str, startIndex + 1, endIndex);
        str = swap(str, startIndex, i);
```

voidpermute(T[] array) Randomly permute the values in array .

```java title=Example.java
Collections.shuffle(Arrays.asList(array));
```

T[]permute(T[] values) "Randomly" permute an array in place.

```java title=Example.java
for (int i = 0; i < values.length; i++) {
    swap(values, i, generator.nextInt(values.length));
return values;
```

int[]permuteArray(int[] array, Integer[] permutation) permute Array

```java title=Example.java
int[] output = newint[array.length];
for (int i = 0; i < output.length; i++) {
    output[i] = array[permutation[i]];
return output;
```

[HOME](https://www.java2s.com/) | Copyright © www.java2s.com 2016
