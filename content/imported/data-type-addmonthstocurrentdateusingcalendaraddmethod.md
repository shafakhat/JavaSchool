---
title: Add months to current date using Calendar.add method
nav: Add months to current date...
description: System.out.println("Current date : " + (now.get(Calendar.MONTH) + 1) + "-"
section: Imported - java2s Archive
order: 1009
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/AddmonthstocurrentdateusingCalendaraddmethod.htm
---
```java title=Example.java
import java.util.Calendar;
publicclass Main {
  publicstaticvoid main(String[] args) {
    Calendar now = Calendar.getInstance();
    System.out.println("Current date : " + (now.get(Calendar.MONTH) + 1) + "-"
        + now.get(Calendar.DATE) + "-" + now.get(Calendar.YEAR));
    now.add(Calendar.MONTH, 10);
    System.out.println("date after 10 months : " + (now.get(Calendar.MONTH) + 1) + "-"
        + now.get(Calendar.DATE) + "-" + now.get(Calendar.YEAR));
  }
}
```
