---
title: Comparing Calendars
nav: Comparing Calendars
description: Imported from the java2s.com archive: Comparing Calendars
section: Imported - java2s Archive
order: 1011
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ComparingCalendars.htm
---
```java title=Example.java
import java.util.Calendar;
import java.util.GregorianCalendar;

publicclass MainClass {
  publicstaticvoid main(String[] a) {
    GregorianCalendar today = new GregorianCalendar();
    GregorianCalendar thisDate = new GregorianCalendar();
    thisDate.set(Calendar.YEAR, 2000);
    if (thisDate.before(today)) {
      System.out.println("before");
    }
    if (today.after(thisDate)) {
      System.out.println("after");
    }
  }
}
```
