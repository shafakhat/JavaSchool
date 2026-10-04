---
title: Get current time information
nav: Get current time information
description: System.out.println("Current Hour in 12 hour format is : " + now.get(Calendar.HOUR));
section: Imported - java2s Archive
order: 1089
source: https://web.archive.org/web/20140614152338/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Getcurrenttimeinformation.htm
---
```java title=Example.java
import java.util.Calendar;
public class Main {
  public static void main(String[] args) {
    Calendar now = Calendar.getInstance();
    System.out.println("Current Hour in 12 hour format is : " + now.get(Calendar.HOUR));
    System.out.println("Current Hour in 24 hour format is : " + now.get(Calendar.HOUR_OF_DAY));
    System.out.println("Current Minute is : " + now.get(Calendar.MINUTE));
    System.out.println("Current Second is : " + now.get(Calendar.SECOND));
    System.out.println("Current Millisecond is : " + now.get(Calendar.MILLISECOND));
  }
}
```
