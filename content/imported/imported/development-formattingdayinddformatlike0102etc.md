---
title: Formatting day in dd format like 01, 02 etc.
nav: Formatting day in dd forma...
description: System.out.println("Current day in dd format : " + sdf.format(new Date()));
section: Imported - java2s Archive
order: 1026
source: https://web.archive.org/web/20100505183012/http://www.java2s.com:80/Tutorial/Java/0120__Development/Formattingdayinddformatlike0102etc.htm
---
```java title=Example.java
import java.text.SimpleDateFormat;
import java.util.Date;
public class Main {
  public static void main(String[] args) {
    String strDateFormat = "dd";
    SimpleDateFormat sdf = new SimpleDateFormat(strDateFormat);
    System.out.println("Current day in dd format : " + sdf.format(new Date()));
  }
}
```
