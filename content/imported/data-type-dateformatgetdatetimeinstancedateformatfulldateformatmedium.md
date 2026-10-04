---
title: DateFormat.getDateTimeInstance(DateFormat.FULL,DateFormat.MEDIUM)
nav: DateFormat.getDateTimeInst...
description: DateFormat df = DateFormat.getDateTimeInstance(DateFormat.FULL,DateFormat.MEDIUM);
section: Imported - java2s Archive
order: 1081
source: https://web.archive.org/web/20140829090554/http://www.java2s.com/Tutorial/Java/0040__Data-Type/DateFormatgetDateTimeInstanceDateFormatFULLDateFormatMEDIUM.htm
---
```java title=Example.java
import java.text.DateFormat;
import java.util.Calendar;
public class CalendarManipulation {
  public static void main(String s[]) {
    Calendar cal = Calendar.getInstance();
    DateFormat df = DateFormat.getDateTimeInstance(DateFormat.FULL,DateFormat.MEDIUM);
    System.out.println(df.format(cal.getTime()));
    cal.add(Calendar.AM_PM, 1);
    System.out.println(df.format(cal.getTime()));
  }
}
```
