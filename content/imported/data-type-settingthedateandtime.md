---
title: Setting the Date and Time
nav: Setting the Date and Time
description: Imported from the java2s.com archive: Setting the Date and Time
section: Imported - java2s Archive
order: 1112
source: https://web.archive.org/web/20140829080505/http://www.java2s.com/Tutorial/Java/0040__Data-Type/SettingtheDateandTime.htm
---
```java title=Example.java
import java.util.Date;
import java.util.GregorianCalendar;
public class MainClass {
  public static void main(String[] a) {
    Date date = new Date();
    GregorianCalendar calendar = new GregorianCalendar();
    calendar.setTime(date);
  }
}
```
