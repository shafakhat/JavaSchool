---
title: To increment or decrement a field of a calendar by 1 using the roll() method
nav: To increment or decrement ...
description: By +1 or -1, depending on the second argument(true or false).
section: Imported - java2s Archive
order: 1043
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Toincrementordecrementafieldofacalendarby1usingtherollmethod.htm
---
By +1 or -1, depending on the second argument(true or false).

```java title=Example.java
import java.util.Calendar;
import java.util.GregorianCalendar;
publicclass MainClass {
  publicstaticvoid main(String[] a) {
    GregorianCalendar calendar = new GregorianCalendar();
    calendar.roll(Calendar.MONTH, false); // Go back a month
    System.out.println(calendar.get(Calendar.MONTH));
  }
}
```

```java title=Example.java
11
```
