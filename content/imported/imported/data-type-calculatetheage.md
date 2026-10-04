---
title: Calculate the age
nav: Calculate the age
description: Imported from the java2s.com archive: Calculate the age
section: Imported - java2s Archive
order: 1013
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Calculatetheage.htm
---
```java title=Example.java
import java.util.Calendar;
import java.util.GregorianCalendar;

publicclass Main {

  publicstaticvoid main(String[] args) {
    Calendar cal = new GregorianCalendar(1999, 1, 1);
    Calendar now = new GregorianCalendar();
    int res = now.get(Calendar.YEAR) - cal.get(Calendar.YEAR);
    if ((cal.get(Calendar.MONTH) > now.get(Calendar.MONTH))
        || (cal.get(Calendar.MONTH) == now.get(Calendar.MONTH) && cal.get(Calendar.DAY_OF_MONTH) > now
            .get(Calendar.DAY_OF_MONTH))) {
      res--;
    }
    System.out.println(res);
  }
}
```
