---
title: Get observes Daylight Time from SimpleTimeZone
nav: Get observes Daylight Time...
description: SimpleTimeZone simpleTimeZone = new SimpleTimeZone(-21600000, "CST",
section: Imported - java2s Archive
order: 1060
source: https://web.archive.org/web/20130216014212/http://www.java2s.com:80/Code/Java/JDK-7/GetobservesDaylightTimefromSimpleTimeZone.htm
---
```java title=Example.java
import java.util.Calendar;
import java.util.SimpleTimeZone;
public class Test {
  public static void main(String[] args) {
    SimpleTimeZone simpleTimeZone = new SimpleTimeZone(-21600000, "CST",
        Calendar.MARCH, 1, -Calendar.SUNDAY, 7200000, Calendar.NOVEMBER, -1,
        Calendar.SUNDAY, 7200000, 3600000);
    System.out.println(simpleTimeZone.getDisplayName() + " - "
        + simpleTimeZone.observesDaylightTime());
  }
}
```

1.  Handling weeks in Java 1.7
