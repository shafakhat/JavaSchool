---
title: Creating a Date Object for a Particular Date
nav: Creating a Date Object for...
description: Calendar xmas = new GregorianCalendar(1998, Calendar.DECEMBER, 25);
section: Imported - java2s Archive
order: 1022
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/CreatingaDateObjectforaParticularDate.htm
---
```java title=Example.java
import java.util.Calendar;
import java.util.Date;
import java.util.GregorianCalendar;

publicclass Main {
  publicstaticvoid main(String[] argv) throws Exception {

    Calendar xmas = new GregorianCalendar(1998, Calendar.DECEMBER, 25);
    Date date = xmas.getTime();
  }
}
```
