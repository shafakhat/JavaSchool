---
title: Handling weeks in Java 1.7
nav: Handling weeks in Java 1.7
description: System.out.println(DateFormat.getDateTimeInstance(DateFormat.LONG,
section: Imported - java2s Archive
order: 1081
source: https://web.archive.org/web/20130213064928/http://www.java2s.com:80/Code/Java/JDK-7/HandlingweeksinJava17.htm
---
```java title=Example.java
import java.text.DateFormat;
import java.util.Calendar;
import java.util.SimpleTimeZone;
public class Test {
  public static void main(String[] args) {
    Calendar calendar = Calendar.getInstance();
    if (calendar.isWeekDateSupported()) {
      System.out.println("Number of weeks in this year: "
          + calendar.getWeeksInWeekYear());
      System.out.println("Current week number: "
          + calendar.get(Calendar.WEEK_OF_YEAR));
    }
    calendar.setWeekDate(2012, 16, 3);
    System.out.println(DateFormat.getDateTimeInstance(DateFormat.LONG,
        DateFormat.LONG).format(calendar.getTime()));
  }
}
```

1.  Get observes Daylight Time from SimpleTimeZone
