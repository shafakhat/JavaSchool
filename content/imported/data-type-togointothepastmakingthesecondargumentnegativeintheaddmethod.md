---
title: To go into the past
nav: To go into the past
description: Imported from the java2s.com archive: To go into the past
section: Imported - java2s Archive
order: 1042
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Togointothepastmakingthesecondargumentnegativeintheaddmethod.htm
---
```java title=Example.java
import java.util.Calendar;
import java.util.GregorianCalendar;
publicclass MainClass {
  publicstaticvoid main(String[] a) {
    GregorianCalendar calendar = new GregorianCalendar();
    calendar.set(Calendar.DAY_OF_WEEK, Calendar.TUESDAY);
    calendar.add(Calendar.YEAR, -14);
    System.out.println(calendar.get(Calendar.YEAR));
  }
}
```

```java title=Example.java
1993
```
