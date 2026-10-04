---
title: Set with GregorianCalendar.YEAR, MONTH and DATE
nav: Set with GregorianCalendar...
description: Imported from the java2s.com archive: Set with GregorianCalendar.YEAR, MONTH and DATE
section: Imported - java2s Archive
order: 1049
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/SetwithGregorianCalendarYEARMONTHandDATE.htm
---
```java title=Example.java
import java.util.GregorianCalendar;
publicclass Main {
  publicstaticvoid main(String[] argv) throws Exception {
    GregorianCalendar gc = new GregorianCalendar();
    gc.setLenient(false);
    gc.set(GregorianCalendar.YEAR, 2003);
    gc.set(GregorianCalendar.MONTH, 12);
    gc.set(GregorianCalendar.DATE, 1);
    gc.getTime();
  }
}
```
