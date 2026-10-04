---
title: Java Utililty Methods Array Convert to
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Convert to are organized into topic(s).
section: Imported - java2s Archive
order: 50043
source: https://www.java2s.com/example/java-utility-method/array-convert-to-index-0.html
---
List of utility methods to do Array Convert to

## Description

The list of methods to do Array Convert to are organized into topic(s).

## Method

Float[]array_float_to_array_Float(float[] a) arrafloatarra Float

```java title=Example.java
Float[] result = newFloat[a.length];
for (int i = 0; i < a.length; i++) {
    result[i] = a[i];
return result;
```

shortarrayFillNonAtomic(byte bArray[], short bOff, short bLen, byte bValue) Fills the byte array (non-atomically) beginning at the specified position, for the specified length with the specified byte value.

```java title=Example.java
byte tester = bArray[bOff];
if (bLen < 0) {
    thrownewArrayIndexOutOfBoundsException();
while (bLen-- > 0) {
    bArray[bOff++] = bValue;
return (short) (bOff + bLen);
...
```

voidarrayMoveWithin(Object[] array, int moveFrom, int moveTo, int numToMove) Moves a number of entries in an array to another point in the array, shifting those inbetween as required.

```java title=Example.java
if (numToMove <= 0) {
    return;
if (moveFrom == moveTo) {
    return;
if (moveFrom < 0 || moveFrom >= array.length) {
    thrownewIllegalArgumentException("The moveFrom must be a valid array index");
...
```

StringarrayOfDoubleToString(double[] array) Provides a string representation for a given double array.

```java title=Example.java
StringBuilder sb = newStringBuilder();
sb.append("[");
boolean firstIteration = true;
for (int i = 0; i < array.length; ++i) {
    if (firstIteration) {
        firstIteration = false;
    } else {
        sb.append(",");
...
```

StringarrayOfIntToString(int[] array) array Of Int To String

```java title=Example.java
String s = "";
for (int i = 0; i < array.length; i++) {
    s += array[i];
    s += (i < array.length - 1 ? "," : "");
return"[" + s + "]";
```

IllegalArgumentExceptionarrayOfValuesToLookForIsEmpty() array Of Values To Look For Is Empty

```java title=Example.java
returnnewIllegalArgumentException("The array of values to look for should not be empty");
```

StringarrayToCamelCase(String[] nameArray, int start, int end) array To Camel Case

```java title=Example.java
StringBuilder sb = newStringBuilder();
boolean isFirst = true;
for (int i = start; i < end; i++) {
    if (nameArray[i].length() > 0) {
        if (isFirst) {
            sb.append(nameArray[i].toLowerCase());
            isFirst = false;
        } else {
...
```

StringarrayToCSL(String[] vals) Converts an array of Strings to a comma-sperated-list.

```java title=Example.java
if (vals == null) {
    return null;
String csl = null;
boolean first = true;
for (int i = 0; i < vals.length; i++) {
    if (vals[i] != null) {
        if (first) {
...
```

doublearrayToDouble(final byte[] array, final int start) Convert the contents of the specified array to a

```java title=Example.java
double
```

, starting at an offset of

```java title=Example.java
start
```

.

```java title=Example.java
int i;
int count;
long accum;
finalint length;
finalbyte[] temp;
count = 0;
length = 8;
temp = newbyte[length];
...
```

StringarrayToHTMLString(Object[] objectArray, int indent) Converts an array to an HTML string.

```java title=Example.java
String value = "";
String indentString = "";
for (int i = 0; i < indent; i++)
    indentString = indentString + spaceChar;
for (int i = 0; i < objectArray.length; i++) {
    Object obj = objectArray[i];
    if (obj.getClass().isArray()) {
        value = value + arrayToHTMLString((Object[]) obj, indent + INDENT);
...
```

[HOME](https://www.java2s.com/) | Copyright © www.java2s.com 2016
