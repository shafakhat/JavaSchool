---
title: Java Utililty Methods AbstractMap Usage
nav: Java Utililty Methods Abst...
description: The list of methods to do AbstractMap Usage are organized into topic(s).
section: Imported - java2s Archive
order: 50008
source: https://www.java2s.com/example/java-utility-method/abstractmap-usage-index-0.html
---
List of utility methods to do AbstractMap Usage

## Description

The list of methods to do AbstractMap Usage are organized into topic(s).

## Method

Map.Entry>buildClause(String key, String... values) build Clause

```java title=Example.java
List<String> clauseValues = newArrayList<String>();
if (values != null) {
    for (String value : values) {
        clauseValues.add(value);
} else {
    clauseValues.add(null);
returnnewAbstractMap.SimpleEntry<String, List<String>>(key, clauseValues);
```

Map.EntrycountLinesColumns(String text, int initialLinesCnt, int initialColumnsCnt) Count lines and columns (in last line) in text.

```java title=Example.java
int lines = initialLinesCnt;
int columns = initialColumnsCnt;
boolean foundCr = false;
for (char c : text.toCharArray()) {
    if (c == '\n') {
        foundCr = false;
        lines++;
        columns = 0;
...
```

Map.EntrydecodeIconUrl(String path) Decodes an URL path to extract a name and a potential qualifier.

```java title=Example.java
if (path.startsWith("/"))
    path = path.substring(1);
String name = null, qualifier = null;
String[] parts = path.split("/");
switch (parts.length) {
case 2:
    name = parts[0];
    break;
...
```

intgetClassType(Object obj) get Class Type

```java title=Example.java
Class<?> collection = java.util.AbstractCollection.class;
Class<?> map = java.util.AbstractMap.class;
if (collection.isInstance(obj)) {
    return 1;
} elseif (map.isInstance(obj)) {
    return 2;
} else {
    return 0;
...
```

Map>getSymmetricPropertyValueDifference( Properties propertyFileOne, Properties propertyFileTwo) get Symmetric Property Value Difference

```java title=Example.java
Map<String, SimpleEntry<String, String>> differences = newHashMap<String, SimpleEntry<String, String>>();
for (String key : propertyFileOne.stringPropertyNames()) {
    String propertyOneValue = propertyFileOne.getProperty(key);
    String propertyTwoValue = propertyFileTwo.getProperty(key);
    if (propertyOneValue != null && propertyTwoValue != null
            && !propertyOneValue.equals(propertyTwoValue)) {
        differences.put(key, new SimpleEntry(propertyOneValue, propertyTwoValue));
return differences;
```

Map.EntryparseEntityURI(final String uri) parse Entity URI

```java title=Example.java
finalString relPath = uri.substring(uri.lastIndexOf("/"));
finalint branchIndex = relPath.indexOf('(');
finalString es = relPath.substring(0, branchIndex);
finalString eid = relPath.substring(branchIndex + 1, relPath.indexOf(')'));
returnnew SimpleEntry<String, String>(es, eid);
```

Map.EntryparseExportedVariable(String exportedVariable) Parses an exported variable (<variableName> = <defaultValue>).

```java title=Example.java
int index = exportedVariable.indexOf('=');
String varName = exportedVariable, defaultValue = null;
if (index > 0) {
    varName = exportedVariable.substring(0, index).trim();
    defaultValue = exportedVariable.substring(index + 1).trim();
returnnewAbstractMap.SimpleEntry<String, String>(varName, defaultValue);
```

Map.EntryparseSocketAddress(String address) parse Socket Address

```java title=Example.java
String hostName = null;
Integer port = null;
if (null != address) {
    if (-1 != address.indexOf(':')) {
        String[] split = address.split(":");
        hostName = split[0];
        port = Integer.valueOf(split[1]);
    } else {
...
```

Map.EntryparseVariableName(String variableName) Parses a variable name (<facetOrComponentName>.<simpleName>).

```java title=Example.java
String componentOrFacetName = "", simpleName = variableName;
int index = variableName.indexOf('.');
if (index >= 0) {
    componentOrFacetName = variableName.substring(0, index).trim();
    simpleName = variableName.substring(index + 1).trim();
returnnewAbstractMap.SimpleEntry<String, String>(componentOrFacetName, simpleName);
```

EntrysplitByQualifier(String str) split By Qualifier

```java title=Example.java
int i = str.lastIndexOf(':');
String name = i == -1 ? str : str.substring(0, i).trim();
String qualifier = i == -1 ? "" : str.substring(i + 1).trim();
Entry<String, String> result = newAbstractMap.SimpleEntry<String, String>(name, qualifier);
return result;
```

[HOME](https://www.java2s.com/) | Copyright © www.java2s.com 2016
