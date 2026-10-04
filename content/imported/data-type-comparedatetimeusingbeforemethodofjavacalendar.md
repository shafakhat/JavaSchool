---
title: Compare date time using before method of Java Calendar
nav: Compare date time using be...
description: System.out.println("Is old before now ? : " + old.before(now));
section: Imported - java2s Archive
order: 1005
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ComparedatetimeusingbeforemethodofJavaCalendar.htm
---
```java title=Example.java
import java.util.Calendar;
public class Main {
  public static void main(String[] args) {
    Calendar old = Calendar.getInstance();
    old.set(Calendar.YEAR, 2990);
    Calendar now = Calendar.getInstance();
    System.out.println("Is old before now ? : " + old.before(now));
  }
}
```
