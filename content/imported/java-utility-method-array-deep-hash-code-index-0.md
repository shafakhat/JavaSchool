---
title: Java Utililty Methods Array Deep Hash Code
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Deep Hash Code are organized into topic(s).
section: Imported - java2s Archive
order: 50050
source: https://www.java2s.com/example/java-utility-method/array-deep-hash-code-index-0.html
---
List of utility methods to do Array Deep Hash Code

## Description

The list of methods to do Array Deep Hash Code are organized into topic(s).

## Method

intdeepHashCode(byte[] array) Computes a hashcode based on the contents of a one-dimensional byte array rather than its identity.

```java title=Example.java
int result = 1;
for (int i = 0; i < array.length; i++) {
    result = 31 * result + array[i];
return result;
```

intdeepHashCode(final Iterable stream) deep Hash Code

```java title=Example.java
int hash = 0;
for (final T next : stream)
    hash = 31 * hash + (next == null ? 0 : next.hashCode());
return hash;
```

intdeepHashCode(Object a[]) Returns a hash code based on the "deep contents" of the specified array.

```java title=Example.java
if (a == null)
    return 0;
int result = 1;
for (Object element : a) {
    int elementHash = 0;
    if (element instanceofObject[])
        elementHash = deepHashCode((Object[]) element);
    elseif (element instanceofbyte[])
...
```

intdeepHashCode(Object a[]) Copied from

```java title=Example.java
Arrays.deepHashCode
```

.

```java title=Example.java
if (a == null) {
    return 0;
int result = 1;
for (Object element : a) {
    int elementHash = 0;
    if (element instanceofObject[]) {
        elementHash = deepHashCode((Object[]) element);
...
```
