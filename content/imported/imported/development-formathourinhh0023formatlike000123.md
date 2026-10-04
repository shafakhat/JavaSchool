---
title: Format hour in HH (00-23) format like 00, 01..23.
nav: Format hour in HH (00-23) ...
description: System.out.println("hour in HH format : " + sdf.format(date));
section: Imported
order: 20000
source: http://www.java2s.com:80/Tutorial/Java/0120__Development/FormathourinHH0023formatlike000123.htm
---
```java title=Example.java
import java.text.SimpleDateFormat;
import java.util.Date;
public class Main {
  public static void main(String[] args) {
    Date date = new Date();
    SimpleDateFormat sdf = new SimpleDateFormat("HH");
    System.out.println("hour in HH format : " + sdf.format(date));
  }
}
//hour in h format : 11
```
