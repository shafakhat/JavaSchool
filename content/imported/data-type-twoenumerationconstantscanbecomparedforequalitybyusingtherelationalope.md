---
title: Two enumeration constants can be compared for equality by using the == relational operator
nav: Two enumeration constants ...
description: Monday, Tuesday, Wednesday, Thursday, Friday, Saturaday, Sunday
section: Imported - java2s Archive
order: 1126
source: https://web.archive.org/web/20140829075725/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Twoenumerationconstantscanbecomparedforequalitybyusingtherelationaloperator.htm
---
```java title=Example.java
enum Week {
  Monday, Tuesday, Wednesday, Thursday, Friday, Saturaday, Sunday
}
public class MainClass {
  public static void main(String args[]) {
    Week aWeekDay;
    aWeekDay = Week.Monday;
    // Output an enum value.
    System.out.println("Value of aWeekDay: " + aWeekDay);
    System.out.println();
    aWeekDay = Week.Friday;
    // Compare two enum values.
    if (aWeekDay == Week.Friday)
      System.out.println(" Friday.\n");
  }
}
java title=Example.java
Value of aWeekDay: Monday
 Friday.
```
