---
title: Get a List of Weekday Names
nav: Get a List of Weekday Names
description: Imported from the java2s.com archive: Get a List of Weekday Names
section: Imported - java2s Archive
order: 1083
source: https://web.archive.org/web/20140829090543/http://www.java2s.com/Tutorial/Java/0040__Data-Type/GetaListofWeekdayNames.htm
---
```java title=Example.java
import java.text.DateFormatSymbols;
public class Main {
  public static void main(String[] args) {
    String[] weekdays = new DateFormatSymbols().getWeekdays();
    for (int i = 0; i < weekdays.length; i++) {
      String weekday = weekdays[i];
      System.out.println("weekday = " + weekday);
    }
  }
}
```
