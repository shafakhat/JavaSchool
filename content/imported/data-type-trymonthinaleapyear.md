---
title: Try month in a leap year
nav: Try month in a leap year
description: Calendar cal = new GregorianCalendar(2000, Calendar.FEBRUARY, 1);
section: Imported - java2s Archive
order: 1093
source: https://web.archive.org/web/20140616101726/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Trymonthinaleapyear.htm
---
```java title=Example.java
import java.util.Calendar;
import java.util.GregorianCalendar;
public class Main {
  public static void main(String[] argv) throws Exception {
    Calendar cal = new GregorianCalendar(2000, Calendar.FEBRUARY, 1);
    int days = cal.getActualMaximum(Calendar.DAY_OF_MONTH); // 29
  }
}
```
