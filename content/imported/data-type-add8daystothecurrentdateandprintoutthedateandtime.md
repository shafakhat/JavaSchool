---
title: add 8 days to the current date and print out the date and time
nav: add 8 days to the current ...
description: DateFormat df = DateFormat.getDateTimeInstance(DateFormat.FULL,
section: Imported - java2s Archive
order: 1263
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/add8daystothecurrentdateandprintoutthedateandtime.htm
---
```java title=Example.java
import java.text.DateFormat;
import java.util.Calendar;
public class CalendarManipulation {
  public static void main(String s[]) {
    Calendar cal = Calendar.getInstance();
    DateFormat df = DateFormat.getDateTimeInstance(DateFormat.FULL,
        DateFormat.MEDIUM);
    System.out.println(df.format(cal.getTime()));
    cal.add(Calendar.DATE, 8);
    System.out.println(df.format(cal.getTime()));
  }
}
```
