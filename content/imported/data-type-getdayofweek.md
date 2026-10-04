---
title: Get day of week
nav: Get day of week
description: Imported from the java2s.com archive: Get day of week
section: Imported - java2s Archive
order: 1160
source: https://web.archive.org/web/20140616095956/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Getdayofweek.htm
---
```java title=Example.java
import java.util.Calendar;
import java.util.Calendar;
public class Main {
  public static void main(String[] args) {
    Calendar calendar = Calendar.getInstance();
    calendar.set(Calendar.YEAR, 2007);
    calendar.set(Calendar.DAY_OF_YEAR, 180);
    // See the full information of the calendar object.
    System.out.println(calendar.getTime().toString());
    // Get the weekday and print it
    int weekday = calendar.get(Calendar.DAY_OF_WEEK);
    System.out.println("Weekday: " + weekday);
  }
}
```
