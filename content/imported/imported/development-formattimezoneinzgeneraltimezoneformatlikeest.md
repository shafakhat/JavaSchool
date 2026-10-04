---
title: Format TimeZone in z (General time zone) format like EST.
nav: Format TimeZone in z (Gene...
description: System.out.println("TimeZone in z format : " + sdf.format(date));
section: Imported - java2s Archive
order: 1020
source: https://web.archive.org/web/20100505183143/http://www.java2s.com:80/Tutorial/Java/0120__Development/FormatTimeZoneinzGeneraltimezoneformatlikeEST.htm
---
```java title=Example.java
import java.text.SimpleDateFormat;
import java.util.Date;
public class Main {
  public static void main(String[] args) {
    Date date = new Date();
    SimpleDateFormat sdf = new SimpleDateFormat("zzz");
    System.out.println("TimeZone in z format : " + sdf.format(date));
  }
}
//TimeZone in z format : PST
```
