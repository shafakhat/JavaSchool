---
title: Determine the day of the week
nav: Determine the day of the w...
description: Imported from the java2s.com archive: Determine the day of the week
section: Imported - java2s Archive
order: 1081
source: https://web.archive.org/web/20140829080203/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Determinethedayoftheweek.htm
---
```java title=Example.java
import java.util.Calendar;
import java.util.GregorianCalendar;
public class Main {
  public static void main(String[] argv) throws Exception {
    GregorianCalendar newCal = new GregorianCalendar();
    int day = newCal.get(Calendar.DAY_OF_WEEK);
    newCal = new GregorianCalendar();
    newCal.set(1997, 2, 1, 0, 0, 0);
    newCal.setTime(newCal.getTime());
    day = newCal.get(Calendar.DAY_OF_WEEK);
  }
}
```
