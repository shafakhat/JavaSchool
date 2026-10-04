---
title: Add year to current date using Calendar.add method
nav: Add year to current date u...
description: System.out.println("Current date : " + (now.get(Calendar.MONTH) + 1) + "-"
section: Imported - java2s Archive
order: 1011
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/AddyeartocurrentdateusingCalendaraddmethod.htm
---
```java title=Example.java
import java.util.Calendar;

publicclass Main {

  publicstaticvoid main(String[] args) {
    Calendar now = Calendar.getInstance();
    System.out.println("Current date : " + (now.get(Calendar.MONTH) + 1) + "-"
        + now.get(Calendar.DATE) + "-" + now.get(Calendar.YEAR));

    now.add(Calendar.YEAR, 1);
    System.out.println("date after one year : " + (now.get(Calendar.MONTH) + 1) + "-"
        + now.get(Calendar.DATE) + "-" + now.get(Calendar.YEAR));

  }

}
```
