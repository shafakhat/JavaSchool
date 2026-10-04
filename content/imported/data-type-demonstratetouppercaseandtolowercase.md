---
title: Demonstrate toUpperCase() and toLowerCase().
nav: Demonstrate toUpperCase() ...
description: Imported from the java2s.com archive: Demonstrate toUpperCase() and toLowerCase().
section: Imported - java2s Archive
order: 1081
source: https://web.archive.org/web/2014/http://www.java2s.com/Tutorial/Java/0040__Data-Type/DemonstratetoUpperCaseandtoLowerCase.htm
---
```java title=Example.java
class ChangeCase {
  public static void main(String args[])
  {
    String s = "This is a test.";
    System.out.println("Original: " + s);
    String upper = s.toUpperCase();
    String lower = s.toLowerCase();
    System.out.println("Uppercase: " + upper);
    System.out.println("Lowercase: " + lower);
  }
}
```
