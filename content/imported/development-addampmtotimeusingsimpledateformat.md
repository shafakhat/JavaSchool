---
title: Add AM PM to time using SimpleDateFormat
nav: Add AM PM to time using Si...
description: Imported from the java2s.com archive: Add AM PM to time using SimpleDateFormat
section: Imported - java2s Archive
order: 1000
source: https://web.archive.org/web/20100505183122/http://www.java2s.com:80/Tutorial/Java/0120__Development/AddAMPMtotimeusingSimpleDateFormat.htm
---
```java title=Example.java
import java.text.SimpleDateFormat;
import java.util.Date;
public class Main {
  public static void main(String[] args) {
    Date date = new Date();
    String strDateFormat = "HH:mm:ss a";
    SimpleDateFormat sdf = new SimpleDateFormat(strDateFormat);
    System.out.println(sdf.format(date));
  }
}
//10:20:12 AM
```
