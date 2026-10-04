---
title: Format hour in k (1-24) format like 1, 2..24.
nav: Format hour in k (1-24) fo...
description: System.out.println("hour in k format : " + sdf.format(date));
section: Imported - java2s Archive
order: 1016
source: https://web.archive.org/web/20100505182951/http://www.java2s.com:80/Tutorial/Java/0120__Development/Formathourink124formatlike1224.htm
---
```java title=Example.java
import java.text.SimpleDateFormat;
import java.util.Date;
public class Main {
  public static void main(String[] args) {
    Date date = new Date();
    SimpleDateFormat sdf = new SimpleDateFormat("k");
    System.out.println("hour in k format : " + sdf.format(date));
  }
}
//hour in h format : 11
```
