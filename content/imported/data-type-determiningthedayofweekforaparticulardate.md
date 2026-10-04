---
title: Determining the Day-of-Week for a Particular Date
nav: Determining the Day-of-Wee...
description: Calendar xmas = new GregorianCalendar(1998, Calendar.DECEMBER, 25);
section: Imported - java2s Archive
order: 1266
source: https://web.archive.org/web/2018/http://www.java2s.com/Tutorial/Java/0040__Data-Type/DeterminingtheDayofWeekforaParticularDate.htm
---
```java title=Example.java
import java.util.Calendar;
import java.util.GregorianCalendar;
public class Main {
  public static void main(String[] argv) throws Exception {
    Calendar xmas = new GregorianCalendar(1998, Calendar.DECEMBER, 25);
    int dayOfWeek = xmas.get(Calendar.DAY_OF_WEEK); // 6=Friday
    Calendar cal = new GregorianCalendar(2003, Calendar.JANUARY, 1);
    dayOfWeek = cal.get(Calendar.DAY_OF_WEEK); // 4=Wednesday
  }
}
```
