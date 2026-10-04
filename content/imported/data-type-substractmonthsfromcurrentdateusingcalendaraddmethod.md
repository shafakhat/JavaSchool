---
title: Substract months from current date using Calendar.add method
nav: Substract months from curr...
description: System.out.println("Current date : " + (now.get(Calendar.MONTH) + 1) + "-"
section: Imported - java2s Archive
order: 1016
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/SubstractmonthsfromcurrentdateusingCalendaraddmethod.htm
---
```java title=Example.java
import java.util.Calendar;
public class Main {
  public static void main(String[] args) {
    Calendar now = Calendar.getInstance();
    System.out.println("Current date : " + (now.get(Calendar.MONTH) + 1) + "-"
        + now.get(Calendar.DATE) + "-" + now.get(Calendar.YEAR));
    now = Calendar.getInstance();
    now.add(Calendar.MONTH, -5);
    System.out.println("date before 5 months : " + (now.get(Calendar.MONTH) + 1) + "-"
        + now.get(Calendar.DATE) + "-" + now.get(Calendar.YEAR));
  }
}
```
