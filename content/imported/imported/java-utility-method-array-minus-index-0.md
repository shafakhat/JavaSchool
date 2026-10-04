---
title: Java Utililty Methods Array Minus
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Minus are organized into topic(s).
section: Imported - java2s Archive
order: 50084
source: https://www.java2s.com/example/java-utility-method/array-minus-index-0.html
---
List of utility methods to do Array Minus

## Description

The list of methods to do Array Minus are organized into topic(s).

## Method

String[]minus(String[] left, String[] right) minus

```java title=Example.java
return minus(left, right, true);
```

double[]minusC(double[] v, double[] u) minus C

```java title=Example.java
double[] vc = Arrays.copyOf(v, v.length);
for (int i = 0; i < v.length; i++) {
    vc[i] -= u[i];
return vc;
```
