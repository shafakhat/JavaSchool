---
title: Obtaining all ordinal values using ordinal()
nav: Obtaining all ordinal valu...
description: Monday, Tuesday, Wednesday, Thursday, Friday, Saturaday, Sunday
section: Imported - java2s Archive
order: 1102
source: https://web.archive.org/web/20140829083912/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Obtainingallordinalvaluesusingordinal.htm
---
```java title=Example.java
enum Week {
  Monday, Tuesday, Wednesday, Thursday, Friday, Saturaday, Sunday
}
public class MainClass {
  public static void main(String args[]) {
    // Obtain all ordinal values using ordinal().
    System.out.println("Here are all week constants" + " and their ordinal values: ");
    for (Week day : Week.values())
      System.out.println(day + " " + day.ordinal());
  }
}
java title=Example.java
Here are all week constants and their ordinal values:
Monday 0
Tuesday 1
Wednesday 2
Thursday 3
Friday 4
Saturaday 5
Sunday 6
```
