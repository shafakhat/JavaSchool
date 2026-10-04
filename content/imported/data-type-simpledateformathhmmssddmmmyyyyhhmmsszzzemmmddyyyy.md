---
title: SimpleDateFormat
nav: SimpleDateFormat
description: Imported from the java2s.com archive: SimpleDateFormat
section: Imported - java2s Archive
order: 1297
source: https://web.archive.org/web/20140219015223/http://www.java2s.com/Tutorial/Java/0040__Data-Type/SimpleDateFormathhmmssddMMMyyyyhhmmsszzzEMMMddyyyy.htm
---
```java title=Example.java
import java.text.SimpleDateFormat;
import java.util.Date;
public class SimpleDateFormatDemo {
  public static void main(String args[]) {
    Date date = new Date();
    SimpleDateFormat sdf;
    sdf = new SimpleDateFormat("hh:mm:ss");
    System.out.println(sdf.format(date));
    sdf = new SimpleDateFormat("dd MMM yyyy hh:mm:ss zzz");
    System.out.println(sdf.format(date));
    sdf = new SimpleDateFormat("E MMM dd yyyy");
    System.out.println(sdf.format(date));
  }
}
```
