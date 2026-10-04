---
title: Java Utililty Methods Array Shuffle
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Shuffle are organized into topic(s).
section: Imported - java2s Archive
order: 50104
source: https://www.java2s.com/example/java-utility-method/array-shuffle-index-0.html
---
List of utility methods to do Array Shuffle

## Description

The list of methods to do Array Shuffle are organized into topic(s).

## Method

T[]randomize(final T[] array) Reassigns all of the existing values in the given array to different (pseudo-random) slots.

```java title=Example.java
if (array == null) {
    throw (newNullPointerException("passed array is of null value"));
T[] copy = Arrays.copyOf(array, array.length);
List<Integer> track = newArrayList<Integer>();
for (int i = 0; i < array.length; i++) {
    int rand = -1;
    do {
...
```

voidshuffle() shuffle

```java title=Example.java
int i;
int j;
int tmp;
int rmd;
Random rnd = newRandom();
for (i = 0, j = 0; i < no; i++, j++) {
    seq[j] = 0;
for (i = 0; i < py; i++, j++) {
    seq[j] = 1;
for (i = 0; i < os; i++, j++) {
    seq[j] = 2;
for (i = 0; i < dl; i++, j++) {
    seq[j] = 3;
for (i = 0; i < sl; i++, j++) {
    seq[j] = 4;
for (i = 0, j = total - 1; j > 0; i++, j--) {
    rmd = rnd.nextInt() % (j + 1);
    if (rmd < 0) {
        rmd = rmd * -1;
    tmp = seq[rmd + i];
    seq[rmd + i] = seq[i];
    seq[i] = tmp;
```

voidshuffle(byte[] array) Randomly shuffle elements within an array.

```java title=Example.java
shuffle(newRandom(), array);
```

voidshuffle(byte[] values, Random rnd) Shuffles the elements in the given array into a random sequence.

```java title=Example.java
shuffle(values, 0, values.length, rnd);
```

Listshuffle(Collection items, Random random) shuffle

```java title=Example.java
List<T> result = newArrayList<T>(items);
Collections.shuffle(result, random);
return result;
```

Listshuffle(Collection objects) Creates a new shuffled list containing the objects in the given collection.

```java title=Example.java
return shuffle(objects, Collections.<T>emptyList());
```

voidshuffle(double[] arr, Random rnd) Randomly permute the given double array.

```java title=Example.java
for (int i = arr.length - 1; i > 0; i--) {
    int j = rnd.nextInt(i + 1);
    double tmp = arr[i];
    arr[i] = arr[j];
    arr[j] = tmp;
```

voidShuffle(double[] array) Shuffle an array.

```java title=Example.java
Shuffle(array, 0);
```

voidshuffle(double[] array, Random r) Implements Fisher-Yates shuffle.

```java title=Example.java
for (int i = array.length - 1; i > 0; i--) {
    int index = r.nextInt(i + 1);
    double a = array[index];
    array[index] = array[i];
    array[i] = a;
```

double[][]shuffle(double[][] kernel, long seed) Shuffle a kernel matrix with seed to initialize the Random object

```java title=Example.java
Double[][] kernelDouble = convert2DoubleObjects(kernel);
for (int i = 0; i < kernel.length; i++) {
    Collections.shuffle(Arrays.asList(kernelDouble[i]), newRandom(seed));
Collections.shuffle(Arrays.asList(kernelDouble), newRandom(seed));
return convert2DoublePrimitives(kernelDouble);
```

[HOME](https://www.java2s.com/) | Copyright © www.java2s.com 2016
