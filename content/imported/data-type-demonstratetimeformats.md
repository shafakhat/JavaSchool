---
title: Demonstrate time formats.
nav: Demonstrate time formats.
description: df = DateFormat.getTimeInstance(DateFormat.SHORT, Locale.JAPAN);
section: Imported - java2s Archive
order: 1242
source: https://web.archive.org/web/2020/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Demonstratetimeformats.htm
---
```java title=Example.java
import java.text.DateFormat;
import java.util.Date;
import java.util.Locale;
public class TimeFormatDemo {
  public static void main(String args[]) {
    Date date = new Date();
    DateFormat df;
    df = DateFormat.getTimeInstance(DateFormat.SHORT, Locale.JAPAN);
    System.out.println("Japan: " + df.format(date));
    df = DateFormat.getTimeInstance(DateFormat.LONG, Locale.UK);
    System.out.println("United Kingdom: " + df.format(date));
    df = DateFormat.getTimeInstance(DateFormat.FULL, Locale.CANADA);
    System.out.println("Canada: " + df.format(date));
  }
}
```
