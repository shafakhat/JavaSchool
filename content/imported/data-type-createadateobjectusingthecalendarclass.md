---
title: Create a Date object using the Calendar class
nav: Create a Date object using...
description: Imported from the java2s.com archive: Create a Date object using the Calendar class
section: Imported - java2s Archive
order: 1198
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/CreateaDateobjectusingtheCalendarclass.htm
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
    java.util.Date utilDate = cal.getTime();
    System.out.println(utilDate);
  }
}
//2009-01-01
```
