---
title: Java Utililty Methods Array to Hex String
nav: Java Utililty Methods Arra...
description: The list of methods to do Array to Hex String are organized into topic(s).
section: Imported - java2s Archive
order: 50120
source: https://www.java2s.com/example/java-utility-method/array-to-hex-string-index-0.html
---
List of utility methods to do Array to Hex String

## Description

The list of methods to do Array to Hex String are organized into topic(s).

## Method

StringarrayToHexString(byte[] array) Helper method to convert a byte[] array (such as a MsgId) to a hex string

```java title=Example.java
return arrayToHexString(array, 0, array.length);
```

Stringarraytohexstring(byte[] bytes) arraytohexstring

```java title=Example.java
StringBuilder string = newStringBuilder();
for (byte b : bytes) {
    String hexString = Integer.toHexString(0x00FF & b);
    string.append(hexString.length() == 1 ? "0" + hexString : hexString);
return string.toString();
```

StringarrayToHexString(final byte[] byteArray) Convert a byte array into hex sequence like [#01 #02 #03]

```java title=Example.java
finalStringBuilder result = newStringBuilder();
result.append('[');
boolean space = false;
for (finalbyte b : byteArray) {
    if (space) {
        result.append(' ');
    } else {
        space = true;
...
```
