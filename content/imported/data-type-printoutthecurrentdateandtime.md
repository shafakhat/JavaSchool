---
title: print out the current date and time
nav: print out the current date...
description: DateFormat df = DateFormat.getDateTimeInstance(DateFormat.FULL,
section: Imported - java2s Archive
order: 1081
source: https://web.archive.org/web/20140829092919/http://www.java2s.com/Tutorial/Java/0040__Data-Type/printoutthecurrentdateandtime.htm
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
  }
}
```
