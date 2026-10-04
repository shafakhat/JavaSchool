---
title: Get the number of days in that month
nav: Get the number of days in ...
description: int days = cal.getActualMaximum(Calendar.DAY_OF_MONTH); // 28
section: Imported - java2s Archive
order: 1003
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Getthenumberofdaysinthatmonth.htm
---
```java title=Example.java
import java.util.Calendar;
public class Main {
  public static void main(String[] argv) throws Exception {
    Calendar cal = Calendar.getInstance();
    int days = cal.getActualMaximum(Calendar.DAY_OF_MONTH); // 28
  }
}
```
