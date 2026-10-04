---
title: Display full date time
nav: Display full date time
description: System.out.println("Current full date time is : " + (now.get(Calendar.MONTH) + 1) + "-"
section: Imported - java2s Archive
order: 1212
source: https://web.archive.org/web/2014/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Displayfulldatetime.htm
---
```java title=Example.java
import java.util.Calendar;
public class Main {
  public static void main(String[] args) {
    Calendar now = Calendar.getInstance();
    System.out.println("Current full date time is : " + (now.get(Calendar.MONTH) + 1) + "-"
        + now.get(Calendar.DATE) + "-" + now.get(Calendar.YEAR) + " "
        + now.get(Calendar.HOUR_OF_DAY) + ":" + now.get(Calendar.MINUTE) + ":"
        + now.get(Calendar.SECOND) + "." + now.get(Calendar.MILLISECOND));
  }
}
```
