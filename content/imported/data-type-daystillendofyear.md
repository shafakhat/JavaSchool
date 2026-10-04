---
title: Days Till End Of Year
nav: Days Till End Of Year
description: Imported from the java2s.com archive: Days Till End Of Year
section: Imported - java2s Archive
order: 1012
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/DaysTillEndOfYear.htm
---
```java title=Example.java
import java.util.Calendar;
import java.util.GregorianCalendar;
class Main {
  publicstaticvoid main(String args[]) {
    Calendar calendar1 = Calendar.getInstance();
    int currentDayOfYear = calendar1.get(Calendar.DAY_OF_YEAR);
    int year = calendar1.get(Calendar.YEAR);
    Calendar calendar2 = new GregorianCalendar(year, 11, 31);
    int dayDecember31 = calendar2.get(Calendar.DAY_OF_YEAR);
    int days = dayDecember31 - currentDayOfYear;
    System.out.println(days + " days remain in current year");
  }
}
```
