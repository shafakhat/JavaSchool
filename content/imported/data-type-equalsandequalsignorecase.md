---
title: equals() and equalsIgnoreCase().
nav: equals() and equalsIgnoreC...
description: System.out.println(s1 + " equals " + s2 + " -> " + s1.equals(s2));
section: Imported - java2s Archive
order: 1132
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/equalsandequalsIgnoreCase.htm
---
```java title=Example.java
class equalsDemo {
  public static void main(String args[]) {
    String s1 = "Hello";
    String s2 = "Hello";
    String s3 = "Good-bye";
    String s4 = "HELLO";
    System.out.println(s1 + " equals " + s2 + " -> " + s1.equals(s2));
    System.out.println(s1 + " equals " + s3 + " -> " + s1.equals(s3));
    System.out.println(s1 + " equals " + s4 + " -> " + s1.equals(s4));
    System.out.println(s1 + " equalsIgnoreCase " + s4 + " -> " + s1.equalsIgnoreCase(s4));
  }
}
```
