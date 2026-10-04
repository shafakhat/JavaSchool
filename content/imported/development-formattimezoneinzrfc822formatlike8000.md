---
title: Format TimeZone in Z (RFC 822) format like -8000.
nav: Format TimeZone in Z (RFC ...
description: System.out.println("TimeZone in Z format : " + sdf.format(date));
section: Imported - java2s Archive
order: 1021
source: https://web.archive.org/web/20100505182919/http://www.java2s.com:80/Tutorial/Java/0120__Development/FormatTimeZoneinZRFC822formatlike8000.htm
---
```java title=Example.java
import java.text.SimpleDateFormat;
import java.util.Date;
public class Main {
  public static void main(String[] args) {
    Date date = new Date();
    SimpleDateFormat sdf = new SimpleDateFormat("Z");
    System.out.println("TimeZone in Z format : " + sdf.format(date));
  }
}
//TimeZone in Z format : -0800
```
