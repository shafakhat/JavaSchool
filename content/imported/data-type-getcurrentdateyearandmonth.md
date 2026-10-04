---
title: Get current date, year and month
nav: Get current date, year and...
description: System.out.println("Current Year is : " + now.get(Calendar.YEAR));
section: Imported - java2s Archive
order: 1029
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Getcurrentdateyearandmonth.htm
---
```java title=Example.java
import java.util.Calendar;
publicclass Main {
  publicstaticvoid main(String[] args) {
    Calendar now = Calendar.getInstance();
    //
    System.out.println("Current Year is : " + now.get(Calendar.YEAR));
    // month start from 0 to 11
    System.out.println("Current Month is : " + (now.get(Calendar.MONTH) + 1));
    System.out.println("Current Date is : " + now.get(Calendar.DATE));
  }
}
```
