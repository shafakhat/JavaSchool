---
title: Add minutes to current date using Calendar.add method
nav: Add minutes to current dat...
description: System.out.println("Current time : " + now.get(Calendar.HOUR_OF_DAY) + ":"
section: Imported - java2s Archive
order: 1009
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/AddminutestocurrentdateusingCalendaraddmethod.htm
---
```java title=Example.java
import java.util.Calendar;
publicclass Main {
  publicstaticvoid main(String[] args) {
    Calendar now = Calendar.getInstance();
    System.out.println("Current time : " + now.get(Calendar.HOUR_OF_DAY) + ":"
        + now.get(Calendar.MINUTE) + ":" + now.get(Calendar.SECOND));
    now.add(Calendar.MINUTE, 20);
    System.out.println("New time after adding 20 minutes : " + now.get(Calendar.HOUR_OF_DAY) + ":"
        + now.get(Calendar.MINUTE) + ":" + now.get(Calendar.SECOND));
  }
}
```
