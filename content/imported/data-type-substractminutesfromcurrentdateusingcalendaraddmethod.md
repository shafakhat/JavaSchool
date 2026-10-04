---
title: Substract minutes from current date using Calendar.add method
nav: Substract minutes from cur...
description: System.out.println("Current time : " + now.get(Calendar.HOUR_OF_DAY) + ":"
section: Imported - java2s Archive
order: 1038
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/SubstractminutesfromcurrentdateusingCalendaraddmethod.htm
---
```java title=Example.java
import java.util.Calendar;
publicclass Main {
  publicstaticvoid main(String[] args) {
    Calendar now = Calendar.getInstance();
    System.out.println("Current time : " + now.get(Calendar.HOUR_OF_DAY) + ":"
        + now.get(Calendar.MINUTE) + ":" + now.get(Calendar.SECOND));
    now = Calendar.getInstance();
    now.add(Calendar.MINUTE, -50);
    System.out.println("Time before 50 minutes : " + now.get(Calendar.HOUR_OF_DAY) + ":"
        + now.get(Calendar.MINUTE) + ":" + now.get(Calendar.SECOND));
  }
}
```
