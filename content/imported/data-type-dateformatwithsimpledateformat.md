---
title: Date Format with SimpleDateFormat
nav: Date Format with SimpleDat...
description: Imported from the java2s.com archive: Date Format with SimpleDateFormat
section: Imported - java2s Archive
order: 1229
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/DateFormatwithSimpleDateFormat.htm
---
```java title=Example.java
import java.text.SimpleDateFormat;
import java.util.Date;
class DateFormatApp {
  public static void main(String args[]) {
    String pattern = "'The year is '";
    pattern += "yyyy GG";
    pattern += "'.\nThe month is '";
    pattern += "MMMMMMMMM";
    pattern += "'.\nIt is '";
    pattern += "hh";
    pattern += "' o''clock '";
    pattern += "a, zzzz";
    pattern += "'.'";
    SimpleDateFormat format = new SimpleDateFormat(pattern);
    String formattedDate = format.format(new Date());
    System.out.println(formattedDate);
  }
}
```
