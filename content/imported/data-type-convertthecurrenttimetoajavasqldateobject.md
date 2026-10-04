---
title: Convert the Current Time to a java.sql.Date Object
nav: Convert the Current Time t...
description: public static void main(String[] args) throws ParseException {
section: Imported - java2s Archive
order: 1066
source: https://web.archive.org/web/20070319212923/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/ConverttheCurrentTimetoajavasqlDateObject.htm
---
```java title=Example.java
import java.sql.Date;
import java.text.ParseException;
import java.util.Calendar;
public class MainClass {
  public static void main(String[] args) throws ParseException {
    Calendar currenttime = Calendar.getInstance();
    Date sqldate = new Date((currenttime.getTime()).getTime());
  }
}
```
