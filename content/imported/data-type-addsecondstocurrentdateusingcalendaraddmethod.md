---
title: Add seconds to current date using Calendar.add method
nav: Add seconds to current dat...
description: System.out.println("Current time : " + now.get(Calendar.HOUR_OF_DAY) + ":"
section: Imported - java2s Archive
order: 1001
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/AddsecondstocurrentdateusingCalendaraddmethod.htm
---
```java title=Example.java
import java.util.Calendar;
publicclass Main {
  publicstaticvoid main(String[] args) {
    Calendar now = Calendar.getInstance();
    System.out.println("Current time : " + now.get(Calendar.HOUR_OF_DAY) + ":"
        + now.get(Calendar.MINUTE) + ":" + now.get(Calendar.SECOND));
    now.add(Calendar.SECOND, 100);
    System.out.println("New time after adding 100 seconds : " + now.get(Calendar.HOUR_OF_DAY) + ":"
        + now.get(Calendar.MINUTE) + ":" + now.get(Calendar.SECOND));
  }
}
```
