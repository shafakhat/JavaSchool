---
title: How to define an enumeration
nav: How to define an enumeration
description: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday
section: Imported - java2s Archive
order: 1036
source: https://web.archive.org/web/20070429111119/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/Howtodefineanenumeration.htm
---
- To define a new type, Day.
- Variable of type Day can only store the values specified between the braces.
- Monday, Tuesday, ... Sunday are called enumeration constants.
- These names will correspond to integer values, starting from 0 in this case.

```java title=Example.java
public class MainClass {
  enum Day {
    Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday
  }
  public static void main(String[] args) {
    Day yesterday = Day.Thursday;
    Day today = Day.Friday;
    Day tomorrow = Day.Saturday;
    System.out.println("Today is " + today);
    System.out.println("Tomorrow will be " + tomorrow);
    System.out.println("Yesterday was " + yesterday);
  }
}
java title=Example.java
Today is Friday
Tomorrow will be Saturday
Yesterday was Thursday
```
