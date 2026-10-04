---
title: Add or substract days to current date using Java Calendar
nav: Add or substract days to c...
description: System.out.println("Current date : " + (now.get(Calendar.MONTH) + 1) + "-"
section: Imported - java2s Archive
order: 1008
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/AddorsubstractdaystocurrentdateusingJavaCalendar.htm
---
```java title=Example.java
import java.util.Calendar;

publicclass Main {

  publicstaticvoid main(String[] args) {
    Calendar now = Calendar.getInstance();
    System.out.println("Current date : " + (now.get(Calendar.MONTH) + 1) + "-"
        + now.get(Calendar.DATE) + "-" + now.get(Calendar.YEAR));

    // add days to current date using Calendar.add method
    now.add(Calendar.DATE, 1);

    System.out.println("date after one day : " + (now.get(Calendar.MONTH) + 1) + "-"
        + now.get(Calendar.DATE) + "-" + now.get(Calendar.YEAR));
  }
}
/*
Current date : 2-20-2009
date after one day : 2-21-2009
*/
```
