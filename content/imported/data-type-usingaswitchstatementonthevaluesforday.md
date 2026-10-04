---
title: Using a switch statement on the values for day
nav: Using a switch statement o...
description: Imported from the java2s.com archive: Using a switch statement on the values for day
section: Imported - java2s Archive
order: 1228
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Usingaswitchstatementonthevaluesforday.htm
---
```java title=Example.java
import java.util.Calendar;
import java.util.GregorianCalendar;
public class MainClass {
  public static void main(String[] a) {
    GregorianCalendar calendar = new GregorianCalendar();
    calendar.set(Calendar.DAY_OF_WEEK, Calendar.TUESDAY);
    int day = calendar.get(Calendar.DAY_OF_WEEK);
    switch (day) {
    case Calendar.MONDAY:
      System.out.println(Calendar.MONDAY);
      break;
    case Calendar.TUESDAY:
      System.out.println(Calendar.TUESDAY);
      break;
    default:
      System.out.println("others");
    }
  }
}
```
