---
title: Format hour in h (1-12 in AM/PM) format like 1, 2..12.
nav: Format hour in h (1-12 in ...
description: System.out.println("hour in h format : " + sdf.format(date));
section: Imported - java2s Archive
order: 1012
source: https://web.archive.org/web/20100505183203/http://www.java2s.com:80/Tutorial/Java/0120__Development/Formathourinh112inAMPMformatlike1212.htm
---
```java title=Example.java
import java.text.SimpleDateFormat;
import java.util.Date;
public class Main {
  public static void main(String[] args) {
    Date date = new Date();
    String strDateFormat = "h";
    SimpleDateFormat sdf = new SimpleDateFormat(strDateFormat);
    System.out.println("hour in h format : " + sdf.format(date));
  }
}
//hour in h format : 11
```
