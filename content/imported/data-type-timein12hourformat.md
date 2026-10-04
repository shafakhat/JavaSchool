---
title: Time in 12-hour format
nav: Time in 12-hour format
description: Imported from the java2s.com archive: Time in 12-hour format
section: Imported - java2s Archive
order: 1248
source: https://web.archive.org/web/2014/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Timein12hourformat.htm
---
```java title=Example.java
import java.text.SimpleDateFormat;
import java.util.Date;
public class Main {
  public static void main(String[] argv) throws Exception {
    Date date = new Date();
    SimpleDateFormat simpDate;
    simpDate = new SimpleDateFormat("hh:mm:ss a");
    System.out.println(simpDate.format(date));
  }
}
```
