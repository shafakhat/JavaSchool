---
title: Java Utililty Methods Array Print
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Print are organized into topic(s).
section: Imported - java2s Archive
order: 50092
source: https://www.java2s.com/example/java-utility-method/array-print-index-0.html
---
List of utility methods to do Array Print

## Description

The list of methods to do Array Print are organized into topic(s).

## Method

StringformatStringForPrettyPrintingRelatedValues(double[] values, int minDigits) format String For Pretty Printing Related Values

```java title=Example.java
double diff = minDiff(values, true);
double roundingFactor = Math.round(Math.log(diff) / Math.log(10) - 0.5);
if (roundingFactor > -minDigits)
    roundingFactor = -minDigits;
double normFactor = Math.pow(10, roundingFactor);
roundingFactor = -roundingFactor;
return"%." + String.format("%.0f", roundingFactor) + "f";
```

voidprettyPrint(double[][] gammas, double[][] thetas, double[][] zprobs) pretty Print

```java title=Example.java
prettyPrint("GAMMAS", gammas);
prettyPrint("THETAS", thetas);
prettyPrint("ZPROBS", zprobs);
```

Stringprint(Object[] array) print

```java title=Example.java
return print(array, ", ");
```

voidprint(Object[] array) print

```java title=Example.java
if (array == null) {
    System.out.println("object is null");
} else {
    System.out.println(Arrays.asList(array));
```

voidprint(String[] files) print

```java title=Example.java
for (int i = 0; i < files.length; i++) {
    System.out.print(files[i] + " ");
System.out.print("\n");
```

voidprint1DIntArray(int[] array) print D Int Array

```java title=Example.java
printArray(getBoxedIntArray(array));
```

StringprintArray(boolean[] array) print Array

```java title=Example.java
StringBuilder sb = newStringBuilder();
for (int i = 0; i < array.length; i++) {
    if (i > 0) {
        sb.append(" ");
    sb.append(array[i] ? "1" : "0");
return sb.reverse().toString();
...
```

voidprintArray(double[] _a)

Prints on console the elements of a double array. **System**.out.println(array2string(_a));

voidprintArray(double[] _a)

Prints on console the elements of an array of doubles

```java title=Example.java
System.out.println(array2string(_a));
```

voidprintArray(double[] a) print array of values in one line

```java title=Example.java
for (int i = 0; i < a.length; i++) {
    System.out.format("%.2f  ", a[i]);
System.out.println();
```
