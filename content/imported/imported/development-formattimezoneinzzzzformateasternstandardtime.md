---
title: Format TimeZone in zzzz format Eastern Standard Time.
nav: Format TimeZone in zzzz fo...
description: System.out.println("TimeZone in zzzz format : " + sdf.format(date));
section: Imported - java2s Archive
order: 1022
source: https://web.archive.org/web/20100505183148/http://www.java2s.com:80/Tutorial/Java/0120__Development/FormatTimeZoneinzzzzformatEasternStandardTime.htm
---
```java title=Example.java
import java.text.SimpleDateFormat;
import java.util.Date;
public class Main {
  public static void main(String[] args) {
    Date date = new Date();
    SimpleDateFormat sdf = new SimpleDateFormat("zzzz");
    System.out.println("TimeZone in zzzz format : " + sdf.format(date));
  }
}
//TimeZone in zzzz format : Pacific Standard Time
```
