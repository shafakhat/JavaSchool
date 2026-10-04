---
title: Date and time with month
nav: Date and time with month
description: Imported from the java2s.com archive: Date and time with month
section: Imported - java2s Archive
order: 1086
source: https://web.archive.org/web/20140218022534/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Dateandtimewithmonth.htm
---
```java title=Example.java
import java.text.SimpleDateFormat;
import java.util.Date;
public class Main {
  public static void main(String[] argv) throws Exception {
    Date date = new Date();
    SimpleDateFormat simpDate;
    simpDate = new SimpleDateFormat("dd MMM yyyy hh:mm:ss a");
    System.out.println(simpDate.format(date));
  }
}
```
