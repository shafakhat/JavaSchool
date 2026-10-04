---
title: Format hour in H (0-23) format like 0, 1...23.
nav: Format hour in H (0-23) fo...
description: System.out.println("hour in H format : " + sdf.format(date));
section: Imported - java2s Archive
order: 1011
source: https://web.archive.org/web/20100505182931/http://www.java2s.com:80/Tutorial/Java/0120__Development/FormathourinH023formatlike0123.htm
---
```java title=Example.java
import java.text.SimpleDateFormat;
import java.util.Date;
public class Main {
  public static void main(String[] args) {
    Date date = new Date();
    SimpleDateFormat sdf = new SimpleDateFormat("H");
    System.out.println("hour in H format : " + sdf.format(date));
  }
}
//hour in h format : 11
```
