---
title: Date and time with day and month fully spelled-out
nav: Date and time with day and...
description: simpDate = new SimpleDateFormat("EEEE MMMMM dd yyyy kk:mm:ss");
section: Imported - java2s Archive
order: 1085
source: https://web.archive.org/web/20140218022258/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Dateandtimewithdayandmonthfullyspelledout.htm
---
```java title=Example.java
import java.text.SimpleDateFormat;
import java.util.Date;
public class Main {
  public static void main(String[] argv) throws Exception {
    Date date = new Date();
    SimpleDateFormat simpDate;
    simpDate = new SimpleDateFormat("EEEE MMMMM dd yyyy kk:mm:ss");
    System.out.println(simpDate.format(date));
  }
}
```
