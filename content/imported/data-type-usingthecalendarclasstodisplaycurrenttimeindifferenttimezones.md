---
title: Using the Calendar Class to Display Current Time in Different Time Zones
nav: Using the Calendar Class t...
description: calNewYork.setTimeZone(TimeZone.getTimeZone("America/New_York"));
section: Imported - java2s Archive
order: 1152
source: https://web.archive.org/web/20140616102004/http://www.java2s.com/Tutorial/Java/0040__Data-Type/UsingtheCalendarClasstoDisplayCurrentTimeinDifferentTimeZones.htm
---
```java title=Example.java
import java.util.Calendar;
import java.util.TimeZone;
public class Main {
  public static void main(String[] args) {
    Calendar calNewYork = Calendar.getInstance();
    calNewYork.setTimeZone(TimeZone.getTimeZone("America/New_York"));
    System.out.println("Time in New York: " + calNewYork.get(Calendar.HOUR_OF_DAY) + ":"
        + calNewYork.get(Calendar.MINUTE));
  }
}
//Time in New York: 11:51
```
