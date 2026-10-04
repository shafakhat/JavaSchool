---
title: Demonstrate date formats with different DateFormat constants
nav: Demonstrate date formats w...
description: df = DateFormat.getDateInstance(DateFormat.SHORT, Locale.JAPAN);
section: Imported - java2s Archive
order: 1026
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/DemonstratedateformatswithdifferentDateFormatconstants.htm
---
```java title=Example.java
import java.text.DateFormat;
import java.util.Date;
import java.util.Locale;
public class DateFormatDemo {
  public static void main(String args[]) {
    Date date = new Date();
    DateFormat df;
    df = DateFormat.getDateInstance(DateFormat.SHORT, Locale.JAPAN);
    System.out.println("Japan: " + df.format(date));
    df = DateFormat.getDateInstance(DateFormat.MEDIUM, Locale.KOREA);
    System.out.println("Korea: " + df.format(date));
    df = DateFormat.getDateInstance(DateFormat.LONG, Locale.UK);
    System.out.println("United Kingdom: " + df.format(date));
    df = DateFormat.getDateInstance(DateFormat.FULL, Locale.US);
    System.out.println("United States: " + df.format(date));
  }
}
```
