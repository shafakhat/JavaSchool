---
title: Java Utililty Methods Array One Dimension to Two Dimension
nav: Java Utililty Methods Arra...
description: List of utility methods to do Array One Dimension to Two Dimension
section: Imported - java2s Archive
order: 50089
source: https://www.java2s.com/example/java-utility-method/array-one-dimension-to-two-dimension-index-0.html
---
List of utility methods to do Array One Dimension to Two Dimension

## Description

The list of methods to do Array One Dimension to Two Dimension are organized into topic(s).

## Method

double[][]array1DTo2D(double[] In, int H) Returns 2d array (column major) of a 1d array.

```java title=Example.java
int W = In.length / H;
double Out[][] = newdouble[H][W];
for (int j = 0; j < H; j++)
    for (int i = 0; i < W; i++)
        Out[i][j] = In[j * W + i];
return Out;
```

Objectarray1DTo2D(final Object data, final int bitpix, final int width, final int height) Converts a Fits data 1D to 2D.

```java title=Example.java
Object obj;
switch (bitpix) {
case 8:
    byte[] dataB = (byte[]) data;
    byte[][] resultB = newbyte[height][width];
    for (int i = 0; i < height; i++) {
        for (int j = 0; j < width; j++) {
            resultB[i][j] = dataB[i * width + j];
...
```

float[][]array1dTo2d(float[] in, int firstDim) returns a float[firstDim][in.length/firstDim] where in.length%firstDim==0

```java title=Example.java
int secondDim = in.length / firstDim;
if (firstDim * secondDim != in.length)
    thrownewError(in.length + " not divisible by " + firstDim);
float[][] out = newfloat[firstDim][secondDim];
for (int i = 0; i < firstDim; i++) {
    System.arraycopy(in, i * secondDim, out[i], 0, secondDim);
return out;
...
```

double[][]array1Dto2D(int m, int n, double[] b) array Dto D

```java title=Example.java
int i, j;
double a[][];
a = newdouble[m][n];
for (i = 0; i < m; i++)
    for (j = 0; j < n; j++)
        a[i][j] = b[i * n + j];
return a;
```

int[][]array1DTo2D(int[] array1D) array D To D

```java title=Example.java
int m = (int) Math.sqrt(array1D.length);
int[][] array2D = newint[m][m];
for (int x = 0; x < array1D.length; x++) {
    int fila = (x / m);
    int columna = x % m;
    array2D[fila][columna] = array1D[x];
return array2D;
...
```

int[][]array1Dto2D(int[] d1, int imageWidth, int imageHeight) array Dto D

```java title=Example.java
int[][] d2 = newint[imageHeight][imageWidth];
for (int h = 0; h < imageHeight; h++) {
    System.arraycopy(d1, h * imageWidth, d2[h], 0, imageWidth);
return d2;
```

float[][]array2multidim(float[] arr, int width, int height) converts a 1D image array to and array of rows

```java title=Example.java
float[][] temp = newfloat[height][width];
int temp2 = 0;
for (int i = 0; i < height; i++) {
    System.arraycopy(arr, temp2, temp[i], 0, width);
    temp2 += width;
return temp;
```

String[]ArrayOutOfMultiDimArray(String _sMultiDimArray[][], int _index) Array Out Of Multi Dim Array

```java title=Example.java
String[] sRetArray = null;
if (_sMultiDimArray != null) {
    sRetArray = newString[_sMultiDimArray.length];
    for (int i = 0; i < _sMultiDimArray.length; i++) {
        sRetArray[i] = _sMultiDimArray[i][_index];
return sRetArray;
...
```
