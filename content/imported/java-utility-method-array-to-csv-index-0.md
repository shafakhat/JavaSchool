---
title: Java Utililty Methods Array to CSV
nav: Java Utililty Methods Arra...
description: The list of methods to do Array to CSV are organized into topic(s).
section: Imported - java2s Archive
order: 50118
source: https://www.java2s.com/example/java-utility-method/array-to-csv-index-0.html
---
List of utility methods to do Array to CSV

## Description

The list of methods to do Array to CSV are organized into topic(s).

## Method

StringArrayToCsv(Object[] line) Array To Csv

```java title=Example.java
StringBuilder csvLine = newStringBuilder();
for (Object obj : line) {
    csvLine.append(obj.toString()).append(",");
csvLine.setCharAt(csvLine.length() - 1, '\n');
return csvLine.toString();
```

StringArrayToCSV(String[] array) Array To CSV

```java title=Example.java
StringBuilder sb = newStringBuilder();
for (int i = 0; i < array.length; i++) {
    String string = array[i];
    if (i == 0)
        sb.append(string);
    else
        sb.append("," + string);
return sb.toString();
```

StringarrayToCsvString(String[] array, char delimiter) Utility method to convert a String array to CSV/TSV row string.

```java title=Example.java
StringBuilder arrayString = newStringBuilder();
for (String arrayElement : array) {
    arrayString.append(arrayElement);
    arrayString.append(delimiter);
return arrayString.toString();
```

StringtoCSV(double[] as) to CSV

```java title=Example.java
StringBuilder b = newStringBuilder();
for (int i = 0; i < as.length - 1; i++) {
    b.append(as[i]);
    b.append(",");
b.append(as[as.length - 1]);
return b.toString();
```

StringtoCSV(int[][] values) to CSV

```java title=Example.java
String vs[][] = newString[values.length][];
for (int i = 0; i < values.length; i++) {
    vs[i] = newString[values[i].length];
    for (int j = 0; j < values[i].length; j++) {
        vs[i][j] = "" + values[i][j];
return toCSV(vs);
...
```

StringtoCSV(Object[] objs) to CSV

```java title=Example.java
return toCSV(objs, false);
```

StringtoCSVString(String[] strArray) to CSV String

```java title=Example.java
if (strArray == null)
    return null;
StringBuilder sb = newStringBuilder();
for (Iterator<String> itr = Arrays.asList(strArray).iterator(); itr.hasNext();) {
    String s = itr.next();
    sb.append(s);
    if (itr.hasNext())
        sb.append(",");
...
```
