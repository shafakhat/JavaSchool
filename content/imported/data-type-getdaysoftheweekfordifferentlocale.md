---
title: Get Days Of The Week for different locale
nav: Get Days Of The Week for d...
description: for (dayOfWeek = firstDayOfWeek; dayOfWeek < weekdays.length; dayOfWeek++)
section: Imported - java2s Archive
order: 1119
source: https://web.archive.org/web/2018/http://www.java2s.com/Tutorial/Java/0040__Data-Type/GetDaysOfTheWeekfordifferentlocale.htm
---
```java title=Example.java
import java.text.DateFormatSymbols;
import java.util.Calendar;
import java.util.Locale;
public class DaysOfTheWeek {
  public static void main(String argv[]) {
    Locale usersLocale = Locale.getDefault();
    DateFormatSymbols dfs = new DateFormatSymbols(usersLocale);
    String weekdays[] = dfs.getWeekdays();
    Calendar cal = Calendar.getInstance(usersLocale);
    int firstDayOfWeek = cal.getFirstDayOfWeek();
    int dayOfWeek;
    for (dayOfWeek = firstDayOfWeek; dayOfWeek < weekdays.length; dayOfWeek++)
      System.out.println(weekdays[dayOfWeek]);
    for (dayOfWeek = 0; dayOfWeek < firstDayOfWeek; dayOfWeek++)
      System.out.println(weekdays[dayOfWeek]);
  }
}
```
