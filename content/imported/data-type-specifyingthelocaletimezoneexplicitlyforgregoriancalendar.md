---
title: Specifying the locale(TimeZone) explicitly for Gregorian Calendar
nav: Specifying the locale(Time...
description: GregorianCalendar calendar = new GregorianCalendar(TimeZone.getTimeZone("America/Chicago"),
section: Imported - java2s Archive
order: 1053
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/SpecifyingthelocaleTimeZoneexplicitlyforGregorianCalendar.htm
---
```java title=Example.java
import java.util.GregorianCalendar;
import java.util.Locale;
import java.util.TimeZone;
publicclass MainClass {
  publicstaticvoid main(String[] a) {
    GregorianCalendar calendar = new GregorianCalendar(TimeZone.getTimeZone("America/Chicago"),
        Locale.US);
    System.out.println(calendar);
  }
}
```
