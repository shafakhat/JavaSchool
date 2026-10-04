---
title: Display Month of year using Java Calendar
nav: Display Month of year usin...
description: System.out.println("Current date : " + (now.get(Calendar.MONTH) + 1) + "-"
section: Imported - java2s Archive
order: 1023
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/DisplayMonthofyearusingJavaCalendar.htm
---
```java title=Example.java
import java.util.Calendar;
publicclass Main {
  publicstaticvoid main(String[] args) {
    Calendar now = Calendar.getInstance();
    System.out.println("Current date : " + (now.get(Calendar.MONTH) + 1) + "-"
        + now.get(Calendar.DATE) + "-" + now.get(Calendar.YEAR));
    String[] strMonths = new String[] { "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug",
        "Sep", "Oct", "Nov", "Dec" };
    System.out.println("Current month is : " + strMonths[now.get(Calendar.MONTH)]);
  }
}
```
