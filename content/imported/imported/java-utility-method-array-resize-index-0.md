---
title: Java Utililty Methods Array Resize
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Resize are organized into topic(s).
section: Imported - java2s Archive
order: 50097
source: https://www.java2s.com/example/java-utility-method/array-resize-index-0.html
---
List of utility methods to do Array Resize

## Description

The list of methods to do Array Resize are organized into topic(s).

## Method

double[]arrayResize(double[] source, int targetSize) array resize to target size using linear interpolation

```java title=Example.java
if (source.length == targetSize) {
    return source;
int sourceSize = source.length;
double fraction = (double) source.length / (double) targetSize;
double[] newSignal = newdouble[targetSize];
for (int i = 0; i < targetSize; i++) {
    double posIdx = fraction * i;
...
```

String[]prepend(String firstElement, String[] remaining) prepend

```java title=Example.java
if (remaining == null) {
    returnnewString[] { firstElement };
ArrayList<String> res = newArrayList<>();
res.add(firstElement);
res.addAll(Arrays.asList(remaining));
return res.toArray(newString[remaining.length + 1]);
```

T[]prepend(T element, T[] array) Adds the element to the beginning of the array and returns the new array.

```java title=Example.java
array = Arrays.copyOf(array, array.length + 1);
System.arraycopy(array, 0, array, 1, array.length - 1);
array[0] = element;
return array;
```

String[]prependArg(String args[], String newArg) prepend Arg

```java title=Example.java
ArrayList<String> newArgs = newArrayList<String>();
newArgs.add(newArg);
for (String arg : args)
    newArgs.add(arg);
return newArgs.toArray(newString[newArgs.size()]);
```

byte[]prependZeros(int n, byte[] message) prepend Zeros

```java title=Example.java
byte[] result = newbyte[n + message.length];
Arrays.fill(result, (byte) 0);
System.arraycopy(message, 0, result, n, message.length);
return result;
```

double[][]resize2(double[][] array, int newsize1, int newsize2, double padding) Resizes a 2-dimensional array preserving data and padding as needed

```java title=Example.java
if (newsize1 < 0 || newsize2 < 0) {
    thrownewRuntimeException("newsizes must be >=0");
int oldsize1 = array.length;
int oldsize2 = array[0].length;
if (oldsize1 == newsize1 && oldsize2 == newsize2) {
    return array;
double[][] newArray = newdouble[newsize1][];
int count = (oldsize1 < newsize1 ? oldsize1 : newsize1);
System.arraycopy(array, 0, newArray, 0, count);
for (int i = 0; i < count; i++) {
    newArray[i] = resize(array[i], newsize2, padding);
for (int i = count; i < newsize1; i++) {
    newArray[i] = newdouble[newsize2];
if (padding != 0.0) {
    for (int i = count; i < newsize1; i++) {
        Arrays.fill(newArray[i], padding);
return newArray;
```

T[]resizeArray(final T[] array, final int newSize) Copies the contents of the given array into an array of the specified size.

```java title=Example.java
returnArrays.copyOf(array, newSize);
```

T[]resizeNoAutoInit(T[] oldarray, int newsize) Resize an array without autoinitialization.

```java title=Example.java
T[] tmp = Arrays.copyOf(oldarray, newsize);
System.out.printf("Old array of type %s resized without auto-init. New capacity: %d\n",
        tmp.getClass().getComponentType(), newsize);
return tmp;
```
