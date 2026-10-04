---
title: Express a duration in term of HH
nav: Express a duration in term...
description: long secs = (cal2.getTimeInMillis() - cal1.getTimeInMillis()) / 1000;
section: Imported - java2s Archive
order: 1081
source: https://web.archive.org/web/20140218022318/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ExpressadurationintermofHHMMSS.htm
---
```java title=Example.java
import java.util.Calendar;
public class Main {
  public static void main(String args[]) {
    Calendar cal1 = Calendar.getInstance();
    Calendar cal2 = Calendar.getInstance();
    cal2.add(Calendar.HOUR, 2);
    cal2.add(Calendar.MINUTE, 42);
    cal2.add(Calendar.SECOND, 12);
    long secs = (cal2.getTimeInMillis() - cal1.getTimeInMillis()) / 1000;
    String display = String.format("%02d:%02d:%02d", secs / 3600, (secs % 3600) / 60, (secs % 60));
    System.out.println(display);
  }
}
```
