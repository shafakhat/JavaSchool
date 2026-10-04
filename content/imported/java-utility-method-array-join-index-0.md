---
title: Java Utililty Methods Array Join
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Join are organized into topic(s).
section: Imported - java2s Archive
order: 50077
source: https://www.java2s.com/example/java-utility-method/array-join-index-0.html
---
List of utility methods to do Array Join

## Description

The list of methods to do Array Join are organized into topic(s).

## Method

int[]arrayJoin(int[] a, int[] b) array Join

```java title=Example.java
int[] result = newint[a.length + b.length];
System.arraycopy(a, 0, result, 0, a.length);
System.arraycopy(b, 0, result, a.length, b.length);
return result;
```

StringarrayJoin(String[] arr, String joinStr) array Join

```java title=Example.java
if (arr == null || arr.length == 0)
    return null;
if (joinStr == null)
    joinStr = "";
StringBuffer buf = newStringBuffer();
for (String str : arr)
    buf.append(str).append(joinStr);
return buf.substring(0, buf.length() - joinStr.length());
...
```

StringarrayJoin(String[] array, char with) array Join

```java title=Example.java
if (array == null || array.length == 0) {
    return"";
int len = array.length;
StringBuilder sb = newStringBuilder(16 + len * 8);
sb.append(array[0]);
for (int i = 1; i < len; i++) {
    sb.append(with);
...
```

StringarrayJoinToString(Object[] array, CharSequence delim) array Join To String

```java title=Example.java
StringBuffer sb = newStringBuffer();
boolean first = true;
for (Object o : array) {
    if (first)
        first = false;
    else
        sb.append(delim);
    sb.append(o.toString());
...
```

byte[]join(byte[]... bs) Join.

```java title=Example.java
int len = 0;
for (byte[] b : bs) {
    len += b.length;
byte[] out = newbyte[len];
int offset = 0;
for (byte[] b : bs) {
    System.arraycopy(b, 0, out, offset, b.length);
...
```

Stringjoin(char sep, Object[] array) join

```java title=Example.java
return join(sep, Arrays.asList(array));
```

Stringjoin(CharSequence separator, String[] strings) Concatenates strings, using a separator.

```java title=Example.java
StringBuilder sb = newStringBuilder();
boolean first = true;
for (String s : strings) {
    if (first) {
        first = false;
    } else {
        sb.append(separator);
    sb.append(s);
return sb.toString();
```

Stringjoin(CharSequence[] strings, CharSequence separator) Joins the strings in 'strings' with 'separator' between each.

```java title=Example.java
StringBuilder result = newStringBuilder();
for (CharSequence string : strings) {
    if (result.length() > 0) {
        result.append(separator);
    result.append(string);
return result.toString();
...
```

Stringjoin(final Object[] array) join

```java title=Example.java
return join(array, ", ");
```

Stringjoin(final Object[] array, final char separator) join

```java title=Example.java
if (array == null) {
    return null;
return join(array, separator, 0, array.length);
```
