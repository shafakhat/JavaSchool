---
title: Format hour in K (0-11 in AM/PM) format like 0, 1..11.
nav: Format hour in K (0-11 in ...
description: System.out.println("hour in K format : " + sdf.format(date));
section: Imported
order: 20005
source: http://www.java2s.com:80/Tutorial/Java/0120__Development/FormathourinK011inAMPMformatlike0111.htm
---
```java title=Example.java
import java.text.SimpleDateFormat;
import java.util.Date;
public class Main {
  public static void main(String[] args) {
    Date date = new Date();
    SimpleDateFormat sdf = new SimpleDateFormat("K");
    System.out.println("hour in K format : " + sdf.format(date));
  }
}
//hour in h format : 11
```
