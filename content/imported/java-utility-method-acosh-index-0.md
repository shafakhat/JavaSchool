---
title: Java Utililty Methods acosh
nav: Java Utililty Methods acosh
description: doubleacosh(double a) Calculates inverse hyperbolic cosine of a double value.
section: Imported - java2s Archive
order: 50010
source: https://www.java2s.com/example/java-utility-method/acosh-index-0.html
---
List of utility methods to do acosh

## Description

The list of methods to do acosh are organized into topic(s).

## Method

doubleacosh(double a) Calculates inverse hyperbolic cosine of a double value.

```java title=Example.java
returnMath.log(Math.sqrt(a * a - 1.0d) + a);
```

doubleacosh(double x) acosh

```java title=Example.java
returnMath.log(x + Math.sqrt(x * x - 1));
```

doubleacosh(double x) Returns the inverse (arc) hyperbolic cosine of a double.

```java title=Example.java
double ans;
if (Double.isNaN(x) || x < 1) {
    ans = Double.NaN;
} elseif (x < 94906265.62) {
    ans = Math.log(x + Math.sqrt(x * x - 1.0));
} else {
    ans = 0.69314718055994530941723212145818 + Math.log(x);
return ans;
```

doubleacosh(double x) Return the inverse (arc) hyperbolic cosine of a double.

```java title=Example.java
double ans;
if (Double.isNaN(x) || (x < 1)) {
    ans = Double.NaN;
elseif (x < 94906265.62) {
    ans = safeLog(x + Math.sqrt(x * x - 1.0D));
} else {
    ans = 0.69314718055994530941723212145818D + safeLog(x);
...
```

doubleacosh(double x) Returns the arc hyperbolic cosine of a value.

```java title=Example.java
returnMath.log(x + Math.sqrt(x * x - 1.0));
```
