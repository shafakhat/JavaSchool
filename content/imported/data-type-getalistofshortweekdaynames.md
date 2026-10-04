---
title: Get a List of Short Weekday Names
nav: Get a List of Short Weekda...
description: String[] shortWeekdays = new DateFormatSymbols().getShortWeekdays();
section: Imported - java2s Archive
order: 1001
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/GetaListofShortWeekdayNames.htm
---
```java title=Example.java
import java.text.DateFormatSymbols;
public class Main {
  public static void main(String[] args) {
    String[] shortWeekdays = new DateFormatSymbols().getShortWeekdays();
    for (int i = 0; i < shortWeekdays.length; i++) {
      String shortWeekday = shortWeekdays[i];
      System.out.println("shortWeekday = " + shortWeekday);
    }
  }
}
```
