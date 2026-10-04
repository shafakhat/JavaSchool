---
title: Java Utililty Methods Array Start With
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Start With are organized into topic(s).
section: Imported - java2s Archive
order: 50109
source: https://www.java2s.com/example/java-utility-method/array-start-with-index-0.html
---
List of utility methods to do Array Start With

## Description

The list of methods to do Array Start With are organized into topic(s).

## Method

booleanarrayStartsWith(byte[] a, byte[] b) array Starts With

```java title=Example.java
return rangeEquals(a, 0, b, 0, b.length);
```

booleanarrayStartsWith(byte[] array, byte[] target) Checks if array starts with target.

```java title=Example.java
if (array == null) {
    return false;
if (target == null) {
    return true;
if (target.length > array.length) {
    return false;
...
```

booleanarrayStartsWith(final byte[] array, final byte[] str) Check that a byte array starts with some byte values.

```java title=Example.java
boolean result = false;
if (array.length >= str.length) {
    result = true;
    int index = str.length;
    while (--index >= 0) {
        if (array[index] != str[index]) {
            result = false;
            break;
...
```

booleanarrayStartsWith(V[] pattern, V[] data) array Starts With

```java title=Example.java
for (int i = 0; i < pattern.length; i++) {
    if (data[i] != pattern[i]) {
        return false;
return true;
```

booleanstartWith(byte[] data, int start, byte[] find) start With

```java title=Example.java
if (data.length - start < find.length) {
    return false;
for (int i = 0; i < find.length; i++) {
    if (data[start + i] != find[i]) {
        return false;
return true;
```

booleanstartWith(byte[] startWith, byte[] bytes) start With

```java title=Example.java
if (bytes == null || startWith == null || bytes.length < startWith.length) {
    return false;
for (int i = 0; i < startWith.length; i++) {
    if (bytes[i] != startWith[i]) {
        return false;
return true;
```

intstartWith(char[] value, char c) start With

```java title=Example.java
for (int i = 0; i < value.length; i++) {
    if (Character.isSpaceChar(value[i]) || Character.isWhitespace(value[i]))
        continue;
    elseif (c == value[i])
        return i;
    elsereturn -1;
return -1;
```

booleanstartWith(final byte[] aBuffer, final byte[] aPrefix) start With

```java title=Example.java
if (aBuffer == null || aPrefix == null || aBuffer.length < aPrefix.length) {
    return false;
int wMax = aPrefix.length;
int wI = 0;
while (wI < wMax) {
    if (aBuffer[wI] != aPrefix[wI]) {
        return false;
...
```

booleanstartWith(String t, String[] prefix) start With

```java title=Example.java
for (String p : prefix) {
    if (t.startsWith(p)) {
        return true;
return false;
```
