---
title: Number Parsing
nav: Number Parsing
description: Parsing is to do with the conversion of a string into a number or a date.
section: Imported - java2s Archive
order: 1119
source: https://web.archive.org/web/20140829092204/http://www.java2s.com/Tutorial/Java/0040__Data-Type/NumberParsing.htm
---
Parsing is to do with the conversion of a string into a number or a date.
The purpose of number parsing is to convert a string into a numeric primitive type. Byte, Short, Integer, Long, Float, and Double classes, provide static methods to parse strings. For example, the Integer class has the parseInteger method with the following signature.

```java title=Example.java
public static int parseInt (String s) throws NumberFormatException
```

The Byte class provides the parseByte method, The Long class the parseLong method, The Short class the parseShort method, The Float class the parseFloat method, and The Double class the parseDouble method.
If the String does not contain a valid integer representation, a NumberFormatException will be thrown. For example, the following snippet uses parseInt to parse the string "123" to 123.

```java title=Example.java
public class MainClass{
  public static void main(String[] args){
      int x = Integer.parseInt ("123");
  }
}
```
