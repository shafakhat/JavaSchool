---
title: compareTo() and equals() for enum data type
nav: compareTo() and equals() f...
description: Monday, Tuesday, Wednesday, Thursday, Friday, Saturaday, Sunday
section: Imported - java2s Archive
order: 1052
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/compareToandequalsforenumdatatype.htm
---
```java title=Example.java
enum Week {
  Monday, Tuesday, Wednesday, Thursday, Friday, Saturaday, Sunday
}
publicclass MainClass {
  publicstaticvoid main(String args[]) {
    Week day1, day2, day3;
    day1 = Week.Monday;
    day2 = Week.Tuesday;
    day3 = Week.Friday;
    //
if (day1.compareTo(day2) < 0)
      System.out.println(day1 + " comes before " + day2);
    if (day2.compareTo(day3) > 0)
      System.out.println(day2 + " comes before " + day3);
    if (day1.compareTo(day3) == 0)
      System.out.println(day1 + " equals " + day3);
  }
}
```

```java title=Example.java
Monday comes before Tuesday
```
