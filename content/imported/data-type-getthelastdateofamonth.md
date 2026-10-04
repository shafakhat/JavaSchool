---
title: Get the last date of a month
nav: Get the last date of a month
description: Imported from the java2s.com archive: Get the last date of a month
section: Imported - java2s Archive
order: 1002
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Getthelastdateofamonth.htm
---
```java title=Example.java
import java.util.Calendar;
public class Main {
  public static void main(String[] args) {
    Calendar calendar = Calendar.getInstance();
    int lastDate = calendar.getActualMaximum(Calendar.DATE);
    System.out.println("Date     : " + calendar.getTime());
    System.out.println("Last Date: " + lastDate);
  }
}
```
