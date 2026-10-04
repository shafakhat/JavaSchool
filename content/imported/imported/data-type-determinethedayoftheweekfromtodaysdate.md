---
title: Determine the Day of the Week from Today's Date
nav: Determine the Day of the W...
description: The answer to this question is to use java.util.Calendar.SUNDAY, java.util.Calendar.MONDAY, and so on:
section: Imported - java2s Archive
order: 1087
source: https://web.archive.org/web/20070319212825/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/DeterminetheDayoftheWeekfromTodaysDate.htm
---
The answer to this question is to use java.util.Calendar.SUNDAY, java.util.Calendar.MONDAY, and so on:

```java title=Example.java
import java.text.ParseException;
public class MainClass {
  public static void main(String[] args) throws ParseException {
    java.util.Date today = new java.util.Date();
    java.sql.Date date = new java.sql.Date(today.getTime());
    java.util.GregorianCalendar cal = new java.util.GregorianCalendar();
    cal.setTime(date);
    System.out.println(cal.get(java.util.Calendar.DAY_OF_WEEK));
  }
}
```
