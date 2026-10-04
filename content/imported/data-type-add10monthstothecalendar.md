---
title: Add 10 months to the calendar
nav: Add 10 months to the calen...
description: Imported from the java2s.com archive: Add 10 months to the calendar
section: Imported - java2s Archive
order: 1000
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Add10monthstothecalendar.htm
---
```java title=Example.java
import java.util.Calendar;
publicclass Main {
  publicstaticvoid main(String[] args) {
    Calendar cal = Calendar.getInstance();
    System.out.println("Today : " + cal.getTime());
    // Substract 30 days from the calendar
    cal.add(Calendar.DATE, -30);
    System.out.println("30 days ago: " + cal.getTime());
  }
}
```
