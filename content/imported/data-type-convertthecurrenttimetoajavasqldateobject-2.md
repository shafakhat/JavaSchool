---
title: Convert the Current Time to a java.sql.Date Object
nav: Convert the Current Time t...
description: Imported from the java2s.com archive: Convert the Current Time to a java.sql.Date Object
section: Imported - java2s Archive
order: 1011
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ConverttheCurrentTimetoajavasqlDateObject.htm
---
```java title=Example.java
import java.sql.Date;
import java.text.ParseException;
import java.util.Calendar;
publicclass MainClass {
  publicstaticvoid main(String[] args) throws ParseException {
    Calendar currenttime = Calendar.getInstance();
    Date sqldate = new Date((currenttime.getTime()).getTime());
  }
}
```
