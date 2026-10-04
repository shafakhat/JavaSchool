---
title: Substract hours from current date using Calendar.add method
nav: Substract hours from curre...
description: System.out.println("Current Date : " + (now.get(Calendar.MONTH) + 1) + "-"
section: Imported - java2s Archive
order: 1037
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/SubstracthoursfromcurrentdateusingCalendaraddmethod.htm
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
    now = Calendar.getInstance();
    now.add(Calendar.HOUR, -3);
    System.out.println("Time before 3 hours : " + now.get(Calendar.HOUR_OF_DAY) + ":"
        + now.get(Calendar.MINUTE) + ":" + now.get(Calendar.SECOND));
  }
}
```
