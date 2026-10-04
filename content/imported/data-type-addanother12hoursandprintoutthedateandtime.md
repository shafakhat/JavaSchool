---
title: add another 12 hours and print out the date and time
nav: add another 12 hours and p...
description: DateFormat df = DateFormat.getDateTimeInstance(DateFormat.FULL,
section: Imported - java2s Archive
order: 1061
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/addanother12hoursandprintoutthedateandtime.htm
---
```java title=Example.java
import java.text.DateFormat;
import java.util.Calendar;
publicclass CalendarManipulation {
  publicstaticvoid main(String s[]) {
    Calendar cal = Calendar.getInstance();
    DateFormat df = DateFormat.getDateTimeInstance(DateFormat.FULL,
        DateFormat.MEDIUM);
    System.out.println(df.format(cal.getTime()));
    cal.add(Calendar.AM_PM, 1);
    System.out.println(df.format(cal.getTime()));
  }
}
```
