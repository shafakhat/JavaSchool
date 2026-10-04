---
title: Substract 30 days from the calendar
nav: Substract 30 days from the...
description: Imported from the java2s.com archive: Substract 30 days from the calendar
section: Imported - java2s Archive
order: 1057
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Substract30daysfromthecalendar.htm
---
```java title=Example.java
import java.util.Calendar;
publicclass Main {
  publicstaticvoid main(String[] args) {
    Calendar cal = Calendar.getInstance();
    System.out.println("Today : " + cal.getTime());
    cal.add(Calendar.DATE, -30);
    System.out.println("30 days ago: " + cal.getTime());
  }
}
```
