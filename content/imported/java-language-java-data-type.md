---
title: Java Tutorial - Java Data Type
nav: Java Tutorial - Java Data ...
description: Java defines eight primitive types of data: byte, short, int, long, char, float, double, and boolean.
section: Imported - java2s Archive
order: 50420
source: https://www.java2s.com/Tutorials/Java/Java_Language/2005__Java_Data_Type.html
---
```java title=Example.java
```

Java defines eight primitive types of data: byte, short, int, long, char, float, double, and boolean.

| Primitive Type | Reserved Word | Size | Min Value | Max Value |
|---|---|---|---|---|
| Boolean | boolean | N/A | N/A | N/A |
| Character | char | 16-bit | Unicode 0 | Unicode 2 16 - 1 |
| Byte integer | byte | 8-bit | -128 | +127 |
| Short integer | short | 16-bit | -2 15 | +2 15 - 1 |
| Integer | int | 32-bit | -2 31 | +2 31 - 1 |
| Long integer | long | 64-bit | -2 63 | +2 63 - 1 |
| Floating-point | float | 32-bit | 1.4e-045 | 3.4e+038 |
| Double precision floating-point | double | 64-bit | 4.9e-324 | 1.8e+308 |

byte, short, int, and long are for whole-valued signed numbers. float and double are fractional precision numbers.

char represents symbols in a character set, like letters and numbers. boolean represents true/false values.

## Java Integers

Java defines four integer types: byte, short, int, and long.

Integer types are signed and can have positive and negative values.

The width and ranges of these integer types vary widely:

Name  Width  Range
---  ---  ---
long  64  -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807
int  32  -2,147,483,648 to 2,147,483,647
short  16  -32,768 to 32,767
byte  8  -128 to 127

## Floating Point Types

There are two kinds of floating-point types: float and double. float type represents single-precision numbers. double type stores double-precision numbers.

Floating-Point Types width and ranges are shown here:

Name  Width in Bits  Approximate Range
---  ---  ---
double  64  4.9e-324 to 1.8e+308
float  32  1.4e-045 to 3.4e+038

- « Previous
