---
title: Format minutes in mm format like 01, 02 etc.
nav: Format minutes in mm forma...
description: System.out.println("minutes in mm format : " + sdf.format(date));
section: Imported
order: 20009
source: http://www.java2s.com:80/Tutorial/Java/0120__Development/Formatminutesinmmformatlike0102etc.htm
---
```java title=Example.java
import java.text.SimpleDateFormat;
import java.util.Date;
public class Main {
  public static void main(String[] args) {
    Date date = new Date();
    SimpleDateFormat sdf = new SimpleDateFormat("mm");
    System.out.println("minutes in mm format : " + sdf.format(date));
  }
}
// minutes in m format : 35
```
