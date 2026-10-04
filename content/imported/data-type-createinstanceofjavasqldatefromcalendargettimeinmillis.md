---
title: Create instance of java.sql.Date from Calendar.getTimeInMillis()
nav: Create instance of java.sq...
description: java.sql.Date sqlDate = new java.sql.Date(cal.getTimeInMillis());
section: Imported - java2s Archive
order: 1154
source: https://web.archive.org/web/2014/http://www.java2s.com/Tutorial/Java/0040__Data-Type/CreateinstanceofjavasqlDatefromCalendargetTimeInMillis.htm
---
```java title=Example.java
import java.util.Calendar;
public class Main {
  public static void main(String[] args) {
    int year = 2009;
    int month = 0; // January
    int date = 1;
    Calendar cal = Calendar.getInstance();
    cal.clear();
    cal.set(Calendar.YEAR, year);
    cal.set(Calendar.MONTH, month);
    cal.set(Calendar.DATE, date);
    java.sql.Date sqlDate = new java.sql.Date(cal.getTimeInMillis());
    System.out.println(sqlDate);
  }
}
//2009-01-01
```
