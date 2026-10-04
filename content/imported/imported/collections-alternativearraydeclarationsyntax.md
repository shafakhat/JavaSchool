---
title: Alternative Array Declaration Syntax
nav: Alternative Array Declarat...
description: This alternative declaration form offers convenience when declaring several arrays at the same time:
section: Imported - java2s Archive
order: 1034
source: https://web.archive.org/web/20070520064943/http://www.java2s.com:80/Tutorial/Java/0140__Collections/AlternativeArrayDeclarationSyntax.htm
---
For example, the following two declarations are equivalent:

```java title=Example.java
int al[] = new int[3];
int[] a2 = new int[3];
```

The following declarations are also equivalent:

char twod1[][] = new char[3][4];
char[][] twod2 = new char[3][4];

This alternative declaration form offers convenience when declaring several arrays at the same time:

```java title=Example.java
int[] nums, nums2, nums3; // create three arrays
```
