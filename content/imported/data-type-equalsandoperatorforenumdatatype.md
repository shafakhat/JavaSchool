---
title: equals and = operator for enum data type
nav: equals and = operator for ...
description: Monday, Tuesday, Wednesday, Thursday, Friday, Saturaday, Sunday
section: Imported - java2s Archive
order: 1124
source: https://web.archive.org/web/20140829075558/http://www.java2s.com/Tutorial/Java/0040__Data-Type/equalsandoperatorforenumdatatype.htm
---
```java title=Example.java
enum Week {
  Monday, Tuesday, Wednesday, Thursday, Friday, Saturaday, Sunday
}
public class MainClass {
  public static void main(String args[]) {
    Week day1, day2, day3;
    day1 = Week.Monday;
    day2 = Week.Monday;
    day3 = Week.Monday;
    if(day1.equals(day2))
      System.out.println("Error!");
    if(day1.equals(day3))
      System.out.println(day1 + " equals " + day3);
    if(day2 == day3)
      System.out.println(day2 + " == " + day3);
  }
}
java title=Example.java
Error!
Monday equals Monday
Monday == Monday
```
