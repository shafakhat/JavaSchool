---
title: Modifying Dates and Times
nav: Modifying Dates and Times
description: Imported from the java2s.com archive: Modifying Dates and Times
section: Imported - java2s Archive
order: 1227
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ModifyingDatesandTimesadding14totheyear.htm
---
```java title=Example.java
import java.util.Calendar;
import java.util.GregorianCalendar;
public class MainClass {
  public static void main(String[] a) {
    GregorianCalendar calendar = new GregorianCalendar();
    calendar.set(Calendar.DAY_OF_WEEK, Calendar.TUESDAY);
    calendar.add(Calendar.YEAR, 14); // 14 years into the future
    System.out.println(calendar.get(Calendar.YEAR));
  }
}
java title=Example.java
2021
```
