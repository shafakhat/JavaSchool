---
title: Java Utililty Methods Array Region Match
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Region Match are organized into topic(s).
section: Imported - java2s Archive
order: 50094
source: https://www.java2s.com/example/java-utility-method/array-region-match-index-0.html
---
List of utility methods to do Array Region Match

## Description

The list of methods to do Array Region Match are organized into topic(s).

## Method

booleanarrayRegionMatches(char[] source, int sourceStart, char[] target, int targetStart, int len) Convenience utility to compare two char[]s.

```java title=Example.java
int sourceEnd = sourceStart + len;
int delta = targetStart - sourceStart;
for (int i = sourceStart; i < sourceEnd; i++) {
    if (source[i] != target[i + delta])
        return false;
return true;
```

booleanarrayRegionMatches(Object[] source, int sourceStart, Object[] target, int targetStart, int len) Convenience utility to compare two Object[]s Ought to be in System.

```java title=Example.java
int sourceEnd = sourceStart + len;
int delta = targetStart - sourceStart;
for (int i = sourceStart; i < sourceEnd; i++) {
    if (!arrayEquals(source[i], target[i + delta]))
        return false;
return true;
```

booleanarrayRegionMatches(Object[] source, int sourceStart, Object[] target, int targetStart, int len) Convenience utility to compare two Object[]s Ought to be in System.

```java title=Example.java
int sourceEnd = sourceStart + len;
int delta = targetStart - sourceStart;
for (int i = sourceStart; i < sourceEnd; i++) {
    if (!arrayEquals(source[i], target[i + delta]))
        return false;
return true;
```

booleanarrayRegionsEqual(boolean[] a, int aoff, int alen, boolean[] b, int boff, int blen) array Regions Equal

```java title=Example.java
if (alen != blen)
    return false;
else {
    for (int i = 0; i < alen; ++i)
        if (a[aoff + i] != b[boff + i])
            return false;
    return true;
```
