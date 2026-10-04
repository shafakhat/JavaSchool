---
title: Display Day of Week using Java Calendar
nav: Display Day of Week using ...
description: System.out.println("Current date : " + (now.get(Calendar.MONTH) + 1) + "-"
section: Imported - java2s Archive
order: 1031
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/DisplayDayofWeekusingJavaCalendar.htm
---
```java title=Example.java
import java.util.Calendar;
publicclass Main {
  publicstaticvoid main(String[] args) {
    Calendar now = Calendar.getInstance();
    System.out.println("Current date : " + (now.get(Calendar.MONTH) + 1) + "-"
        + now.get(Calendar.DATE) + "-" + now.get(Calendar.YEAR));
    String[] strDays = new String[] { "Sunday", "Monday", "Tuesday", "Wednesday", "Thusday",
        "Friday", "Saturday" };
    // Day_OF_WEEK starts from 1 while array index starts from 0
    System.out.println("Current day is : " + strDays[now.get(Calendar.DAY_OF_WEEK) - 1]);
  }
}
```
