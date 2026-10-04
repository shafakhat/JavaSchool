---
title: Java Utililty Methods Args Parse
nav: Java Utililty Methods Args...
description: The list of methods to do Args Parse are organized into topic(s).
section: Imported - java2s Archive
order: 1012
source: https://web.archive.org/web/2016/https://www.java2s.com/example/java-utility-method/args-parse-index-0.html
---
List of utility methods to do Args Parse

## Description

The list of methods to do Args Parse are organized into topic(s).

## Method

ListgetPossibleCompletionsForGivenArgs(String[] args, String[] possibilitiesOfCompletion) get Possible Completions For Given Args

```java title=Example.java
final String argumentToFindCompletionFor = args[args.length - 1];
final List<String> listOfPossibleCompletions = new ArrayList<String>();
for (int i = 0; i < possibilitiesOfCompletion.length; i++) {
    final String[] foundString = possibilitiesOfCompletion;
    try {
        if (foundString[i] != null && foundString[i].regionMatches(true, 0, argumentToFindCompletionFor, 0,
                argumentToFindCompletionFor.length())) {
            listOfPossibleCompletions.add(foundString[i]);
...
```

ListgetPossibleCompletionsForGivenArgs(String[] args, String[] possibilitiesOfCompletion) get Possible Completions For Given Args

```java title=Example.java
String argumentToFindCompletionFor = args[args.length - 1];
List<String> listOfPossibleCompletions = new ArrayList<String>();
for (int i = 0; i < possibilitiesOfCompletion.length; ++i) {
    String foundString = possibilitiesOfCompletion[i];
    if (foundString.regionMatches(true, 0, argumentToFindCompletionFor, 0,
            argumentToFindCompletionFor.length())) {
        listOfPossibleCompletions.add(foundString);
return listOfPossibleCompletions;
```

Mapparse(String[] args) parse

```java title=Example.java
Map<String, String> options = new HashMap<>();
for (int i = 0; i < args.length; i++) {
    if (args[i].charAt(0) == '-' || args[i].charAt(0) == '/')
        args[i] = args[i].substring(1);
        if (i + 1 >= args.length || args[i + 1].charAt(0) == '-' || args[i + 1].charAt(0) == '/')
            options.put(args[i], "null");
...
```

Mapparse(String[] args) parse

```java title=Example.java
HashMap<String, String> ret = new HashMap<>();
for (int i = 0; i < args.length; i += 2) {
    String key = args[i].substring(1);
    ret.put(key.substring(1), args[i + 1]);
return ret;
```

HashMapparseAndFillFittingValues(String[] prefixes, String[] values) parse And Fill Fitting Values

```java title=Example.java
HashMap<String, String> result = new HashMap();
for (String value : values) {
    for (String prefix : prefixes) {
        String realValue = getValueIfExists(prefix, value);
        if (realValue != null) {
            result.put(prefix, realValue);
return result;
```

MapparseArg(String[] args) parse Arg

```java title=Example.java
Map<String, String> map = new HashMap<String, String>();
if (args == null || args.length == 0)
    return map;
String lastKey = null;
for (int i = 0; i < args.length; i++) {
    if (args[i] == null || args[i].equals(""))
        continue;
    if (args[i].startsWith("-")) {
...
```

MapparseArgs(String argvStart, String[] args) parse Args

```java title=Example.java
Map<String, String> rs = new HashMap<String, String>();
for (int i = 0; i < args.length; i++) {
    String arg = args[i];
    String v = ((i < args.length - 1) && !args[i + 1].startsWith(argvStart)) ? args[++i] : null;
    arg = arg.substring(argvStart.length());
    rs.put(arg, v);
return rs;
...
```

MapparseArgs(String[] args) parse Args

```java title=Example.java
Map<String, String> parsedArgs = new HashMap<String, String>();
for (String arg : args) {
    if (arg.startsWith("--port=")) {
        parsedArgs.put("port", arg.substring("--port=".length()));
    } else if (arg.equals("START") || arg.equals("STOP")) {
        parsedArgs.put("action", arg);
    } else {
        throw new RuntimeException("Only accepts START, STOP, and --port=<port #> as arguments");
...
```

HashMapparseArgs(String[] args) parse Args

```java title=Example.java
HashMap results = new HashMap();
for (int i = 0; i <= args.length - 1; i++) {
    String value = "";
    if (args[i].indexOf("-") == 0) {
        if (args[i].length() == 2) {
            try {
                value = args[i + 1];
            } catch (Exception e) {
...
```

MapparseArgs(String[] args) Parse command-line options of the form --key=value into a map of .

```java title=Example.java
Map<String, String> m = new HashMap<String, String>();
if (args != null) {
    for (String s : args) {
        if (s.indexOf("=") < 0) {
            m.put(s.replace("--", ""), Boolean.TRUE.toString());
        } else {
            String key = s.substring(0, s.indexOf("=")).replace("--", "");
            String val = s.substring(s.indexOf("=") + 1);
...
```
