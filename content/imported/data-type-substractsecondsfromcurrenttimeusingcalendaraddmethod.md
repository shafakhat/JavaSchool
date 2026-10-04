---
title: Substract seconds from current time using Calendar.add method
nav: Substract seconds from cur...
description: System.out.println("Current time : " + now.get(Calendar.HOUR_OF_DAY) + ":"
section: Imported - java2s Archive
order: 1017
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/SubstractsecondsfromcurrenttimeusingCalendaraddmethod.htm
---
```java title=Example.java
import java.util.Calendar;
public class Main {
  public static void main(String[] args) {
    Calendar now = Calendar.getInstance();
    System.out.println("Current time : " + now.get(Calendar.HOUR_OF_DAY) + ":"
        + now.get(Calendar.MINUTE) + ":" + now.get(Calendar.SECOND));
    now = Calendar.getInstance();
    now.add(Calendar.SECOND, -50);
    System.out.println("Time before 50 minutes : " + now.get(Calendar.HOUR_OF_DAY) + ":"
        + now.get(Calendar.MINUTE) + ":" + now.get(Calendar.SECOND));  }
}
```
