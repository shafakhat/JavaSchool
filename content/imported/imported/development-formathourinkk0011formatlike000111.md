---
title: Format hour in KK (00-11) format like 00, 01,..11.
nav: Format hour in KK (00-11) ...
description: System.out.println("hour in KK format : " + sdf.format(date));
section: Imported
order: 20004
source: http://www.java2s.com:80/Tutorial/Java/0120__Development/FormathourinKK0011formatlike000111.htm
---
```java title=Example.java
import java.text.SimpleDateFormat;
import java.util.Date;
public class Main {
  public static void main(String[] args) {
    Date date = new Date();
    SimpleDateFormat sdf = new SimpleDateFormat("KK");
    System.out.println("hour in KK format : " + sdf.format(date));
  }
}
// hour in h format : 11
```
