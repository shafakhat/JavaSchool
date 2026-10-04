---
title: Determine the Day of the Week from Today's Date
nav: Determine the Day of the W...
description: The answer to this question is to use java.util.Calendar.SUNDAY, java.util.Calendar.MONDAY, and so on:
section: Imported - java2s Archive
order: 1015
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/DeterminetheDayoftheWeekfromTodaysDate.htm
---
The answer to this question is to use java.util.Calendar.SUNDAY, java.util.Calendar.MONDAY, and so on:

```java title=Example.java
import java.text.ParseException;

publicclass MainClass {

  publicstaticvoid main(String[] args) throws ParseException {

    java.util.Date today = new java.util.Date();
    java.sql.Date date = new java.sql.Date(today.getTime());
    java.util.GregorianCalendar cal = new java.util.GregorianCalendar();
    cal.setTime(date);
    System.out.println(cal.get(java.util.Calendar.DAY_OF_WEEK));

  }
}
```
