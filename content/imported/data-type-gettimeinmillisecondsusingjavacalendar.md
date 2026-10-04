---
title: Get time in milliseconds using Java Calendar
nav: Get time in milliseconds u...
description: System.out.println("Current milliseconds since Jan 1, 1970 are :" + now.getTimeInMillis());
section: Imported - java2s Archive
order: 1161
source: https://web.archive.org/web/20140616100001/http://www.java2s.com/Tutorial/Java/0040__Data-Type/GettimeinmillisecondsusingJavaCalendar.htm
---
```java title=Example.java
import java.util.Calendar;
public class Main {
  public static void main(String[] args) {
    Calendar now = Calendar.getInstance();
    System.out.println("Current milliseconds since Jan 1, 1970 are :" + now.getTimeInMillis());
  }
}
```
