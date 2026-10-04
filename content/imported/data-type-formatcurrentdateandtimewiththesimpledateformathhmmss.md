---
title: Format current date and time with the SimpleDateFormat
nav: Format current date and ti...
description: Imported from the java2s.com archive: Format current date and time with the SimpleDateFormat
section: Imported - java2s Archive
order: 1238
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/FormatcurrentdateandtimewiththeSimpleDateFormatHHmmss.htm
---
```java title=Example.java
import java.text.SimpleDateFormat;
import java.util.Date;
public class Main {
  public static void main(String[] args) {
    SimpleDateFormat sdfTime = new SimpleDateFormat("HH:mm:ss");
    Date now = new Date();
    String strTime = sdfTime.format(now);
    System.out.println("Time: " + strTime);
  }
}
//Time: 13:54:56
```
