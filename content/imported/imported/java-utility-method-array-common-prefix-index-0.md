---
title: Java Utililty Methods Array Common Prefix
nav: Java Utililty Methods Arra...
description: The list of methods to do Array Common Prefix are organized into topic(s).
section: Imported - java2s Archive
order: 50039
source: https://www.java2s.com/example/java-utility-method/array-common-prefix-index-0.html
---
List of utility methods to do Array Common Prefix

## Description

The list of methods to do Array Common Prefix are organized into topic(s).

## Method

intlongestCommonContiguousSubstring(String s, String t) Computes the longest common contiguous substring of s and t.

```java title=Example.java
if (s.isEmpty() || t.isEmpty()) {
    return 0;
int M = s.length();
int N = t.length();
int[][] d = newint[M + 1][N + 1];
for (int j = 0; j <= N; j++) {
    d[0][j] = 0;
...
```

StringlongestCommonPath(String... paths) Returns the longest common path of a group of path strings.

```java title=Example.java
if (paths.length == 0) {
    return"";
if (paths.length == 1) {
    return paths[0];
String prefix = longestCommonPrefix(paths);
int prefixLength = prefix.length();
...
```

intlongestCommonPrefix(CharSequence str1, CharSequence str2) longest Common Prefix

```java title=Example.java
return longestCommonPrefix(str1, str2, 0);
```

intlongestCommonPrefix(String a, String b) longest Common Prefix

```java title=Example.java
int i = 0;
char[] as = a.toCharArray();
char[] bs = b.toCharArray();
int aLen = as.length;
int bLen = bs.length;
while (i < aLen && i < bLen && as[i] == bs[i])
    ++i;
return i;
...
```

StringlongestCommonPrefix(String one, String two) Returns the longest common prefix for two Strings or "" if no prefix is shared

```java title=Example.java
if (one.equals(two)) {
    return one;
if (one.equals("") || two.equals("")) {
    return"";
String currentPrefix = "";
int size = 0;
...
```

StringlongestCommonPrefix(String s1, String s2) longest Common Prefix

```java title=Example.java
if (s1.length() > s2.length()) {
    String tmp = s1;
    s1 = s2;
    s2 = tmp;
int i = 0;
while (i < s1.length() && Character.toUpperCase(s1.charAt(i)) == Character.toUpperCase(s2.charAt(i))) {
    i++;
...
```

StringlongestCommonPrefix(String str1, String str2) longest Common Prefix

```java title=Example.java
int i = 0;
while (i < str1.length() && i < str2.length() && str1.charAt(i) == str2.charAt(i)) {
    i++;
String str = str1.substring(0, i);
return str;
```

StringlongestCommonPrefix(String... strs) Returns the longest common prefix of a group of strings.

```java title=Example.java
if (strs.length == 0) {
    return"";
if (strs.length == 1) {
    return strs[0];
int end = 0;
charLoop: do {
...
```

StringlongestCommonPrefix(String[] strArray) longest Common Prefix

```java title=Example.java
if (strArray.length == 0)
    return"";
if (strArray.length == 1)
    return strArray[0];
int maxLength = Integer.MAX_VALUE;
for (int i = 0; i < strArray.length; i++) {
    maxLength = Math.min(strArray[i].length(), maxLength);
if (maxLength == 0)
    return"";
for (int i = 0; i < maxLength; i++) {
    for (int j = 0; j < strArray.length - 1; j++) {
        if (strArray[j].charAt(i) != strArray[j + 1].charAt(i)) {
            return strArray[j].substring(0, i);
return strArray[0].substring(0, maxLength);
```

StringlongestCommonPrefix(String[] strs) longest Common Prefix

```java title=Example.java
if (strs.length == 0) {
    return"";
int minLen = findMin(strs);
String str0 = strs[minLen];
for (int k = 0; k < str0.length(); k++) {
    for (int i = 0; i < strs.length; i++) {
        String str = strs[i];
...
```
