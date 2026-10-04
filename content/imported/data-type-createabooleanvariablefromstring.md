---
title: Create a boolean variable from string
nav: Create a boolean variable ...
description: Imported from the java2s.com archive: Create a boolean variable from string
section: Imported - java2s Archive
order: 1003
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Createabooleanvariablefromstring.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] args) {
    // Parsing string "true" will result boolean true
 boolean boolA = Boolean.parseBoolean("true");
    System.out.println("boolA = " + boolA);
    // Parsing string "TRUE" also resutl boolean true
 boolean boolB = Boolean.parseBoolean("TRUE");
    System.out.println("boolB = " + boolB);
  }
}
```
