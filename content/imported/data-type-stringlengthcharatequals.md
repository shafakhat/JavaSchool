---
title: String length, charAt, equals
nav: String length, charAt, equ...
description: Imported from the java2s.com archive: String length, charAt, equals
section: Imported - java2s Archive
order: 1036
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/StringlengthcharAtequals.htm
---
```java title=Example.java
class StringDemo2 {
  publicstaticvoid main(String args[]) {
    String strOb1 = "First String";
    String strOb2 = "Second String";
    String strOb3 = strOb1;
    System.out.println("Length of strOb1: " +
                       strOb1.length());
    System.out.println("Char at index 3 in strOb1: " +
                       strOb1.charAt(3));
    if(strOb1.equals(strOb2))
      System.out.println("strOb1 == strOb2");
    else
      System.out.println("strOb1 != strOb2");
    if(strOb1.equals(strOb3))
      System.out.println("strOb1 == strOb3");
    else
      System.out.println("strOb1 != strOb3");
  }
}
```
