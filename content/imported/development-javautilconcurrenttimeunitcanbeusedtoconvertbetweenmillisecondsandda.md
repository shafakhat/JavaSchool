---
title: java.util.concurrent.TimeUnit can be used to convert between milliseconds and days
nav: java.util.concurrent.TimeU...
description: public static long getDifference(Calendar a, Calendar b, TimeUnit units) {
section: Imported - java2s Archive
order: 1723
source: https://web.archive.org/web/20140829083133/http://www.java2s.com/Tutorial/Java/0120__Development/javautilconcurrentTimeUnitcanbeusedtoconvertbetweenmillisecondsanddays.htm
---
```java title=Example.java
import java.util.Calendar;
import java.util.concurrent.TimeUnit;
public class Main {
  public static long getDifference(Calendar a, Calendar b, TimeUnit units) {
    return units.convert(b.getTimeInMillis() - a.getTimeInMillis(), TimeUnit.MILLISECONDS);
  }
  public static void main(String[] args) {
    Calendar first = Calendar.getInstance();
    first.set(2008, Calendar.AUGUST, 1);
    Calendar second = Calendar.getInstance();
    System.out.println(getDifference(first, second, TimeUnit.DAYS) + " day(s) between ");
  }
}
```
