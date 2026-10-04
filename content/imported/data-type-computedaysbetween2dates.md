---
title: Compute days between 2 dates
nav: Compute days between 2 dates
description: System.out.println(daysBetween(c1.getTime(), c2.getTime()) + " day(s) between " + args[0] + "-"
section: Imported - java2s Archive
order: 1016
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Computedaysbetween2dates.htm
---
```java title=Example.java
import java.util.Calendar;
import java.util.Date;
import java.util.GregorianCalendar;
public class Main{
  public static void main(String args[]) {
    Calendar c1 = new GregorianCalendar();
    Calendar c2 = new GregorianCalendar();
    c1.set(2000, 12, 12, 0, 0, 0);
    c2.set(2001, 12, 12, 0, 0, 0);
    System.out.println(daysBetween(c1.getTime(), c2.getTime()) + " day(s) between " + args[0] + "-"
        + args[1] + "-" + args[2] + " and " + args[3] + "-" + args[4] + "-" + args[5]);
  }
  static final long ONE_HOUR = 60 * 60 * 1000L;
  public static long daysBetween(Date d1, Date d2) {
    return ((d2.getTime() - d1.getTime() + ONE_HOUR) / (ONE_HOUR * 24));
  }
}
```
