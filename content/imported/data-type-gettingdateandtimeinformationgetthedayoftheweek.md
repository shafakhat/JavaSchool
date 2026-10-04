---
title: Getting Date and Time Information
nav: Getting Date and Time Info...
description: Imported from the java2s.com archive: Getting Date and Time Information
section: Imported - java2s Archive
order: 1220
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/GettingDateandTimeInformationgetthedayoftheweek.htm
---
```java title=Example.java
import java.util.Calendar;
import java.util.GregorianCalendar;
public class MainClass {
  public static void main(String[] a) {
    GregorianCalendar calendar = new GregorianCalendar();
    calendar.set(Calendar.DAY_OF_WEEK, Calendar.TUESDAY);
    int day = calendar.get(Calendar.DAY_OF_WEEK);
    System.out.println(day);
  }
}
```
