---
title: Get the last day of a month
nav: Get the last day of a month
description: Imported from the java2s.com archive: Get the last day of a month
section: Imported - java2s Archive
order: 1156
source: https://web.archive.org/web/20140829080418/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Getthelastdayofamonth.htm
---
```java title=Example.java
import java.util.Calendar;
public class Main {
  public static void main(String[] args) {
    Calendar calendar = Calendar.getInstance();
    int lastDate = calendar.getActualMaximum(Calendar.DATE);
    calendar.set(Calendar.DATE, lastDate);
    int lastDay = calendar.get(Calendar.DAY_OF_WEEK);
    System.out.println("Last Date: " + calendar.getTime());
    System.out.println("Last Day : " + lastDay);
  }
}
```
