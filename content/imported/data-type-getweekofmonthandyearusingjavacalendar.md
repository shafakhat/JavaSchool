---
title: Get Week of month and year using Java Calendar
nav: Get Week of month and year...
description: System.out.println("Current week of month is : " + now.get(Calendar.WEEK_OF_MONTH));
section: Imported - java2s Archive
order: 1090
source: https://web.archive.org/web/20140829075924/http://www.java2s.com/Tutorial/Java/0040__Data-Type/GetWeekofmonthandyearusingJavaCalendar.htm
---
```java title=Example.java
import java.util.Calendar;
public class Main {
  public static void main(String[] args) {
    Calendar now = Calendar.getInstance();
    System.out.println("Current week of month is : " + now.get(Calendar.WEEK_OF_MONTH));
    System.out.println("Current week of year is : " + now.get(Calendar.WEEK_OF_YEAR));
    now.add(Calendar.WEEK_OF_MONTH, 1);
    System.out.println("date after one year : " + (now.get(Calendar.MONTH) + 1) + "-"
        + now.get(Calendar.DATE) + "-" + now.get(Calendar.YEAR));
  }
}
```
