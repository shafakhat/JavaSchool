---
title: Calendar adjust date automatically
nav: Calendar adjust date autom...
description: System.out.println("Current Date : " + (now.get(Calendar.MONTH) + 1) + "-"
section: Imported - java2s Archive
order: 1008
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Calendaradjustdateautomatically.htm
---
```java title=Example.java
import java.util.Calendar;

publicclass Main {

  publicstaticvoid main(String[] args) {
    Calendar now = Calendar.getInstance();
    System.out.println("Current Date : " + (now.get(Calendar.MONTH) + 1) + "-"
        + now.get(Calendar.DATE) + "-" + now.get(Calendar.YEAR));
    System.out.println("Current time : " + now.get(Calendar.HOUR_OF_DAY) + ":"
        + now.get(Calendar.MINUTE) + ":" + now.get(Calendar.SECOND));

   System.out.println("New date after adding 10 hours : " + (now.get(Calendar.MONTH) + 1) + "-"
       + now.get(Calendar.DATE) + "-" + now.get(Calendar.YEAR));  }
}
```
