---
title: Creating Gregorian Calendars
nav: Creating Gregorian Calendars
description: Imported from the java2s.com archive: Creating Gregorian Calendars
section: Imported - java2s Archive
order: 1081
source: https://web.archive.org/web/20140829080329/http://www.java2s.com/Tutorial/Java/0040__Data-Type/CreatingGregorianCalendars.htm
---
```java title=Example.java
import java.util.Date;
import java.util.GregorianCalendar;
public class MainClass {
  public static void main(String[] a) {
    GregorianCalendar calendar = new GregorianCalendar();
    Date now = calendar.getTime();
    System.out.println(now);
  }
}
java title=Example.java
Tue Jan 16 10:06:13 PST 2007
```
