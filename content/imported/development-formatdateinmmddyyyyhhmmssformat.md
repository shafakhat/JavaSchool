---
title: Format date in mm-dd-yyyy hh
nav: Format date in mm-dd-yyyy hh
description: System.out.println("formatted date in mm/dd/yy : " + strDate);
section: Imported - java2s Archive
order: 1010
source: https://web.archive.org/web/20100505183153/http://www.java2s.com:80/Tutorial/Java/0120__Development/Formatdateinmmddyyyyhhmmssformat.htm
---
```java title=Example.java
import java.text.SimpleDateFormat;
import java.util.Date;
public class Main {
  public static void main(String[] args) {
    Date date = new Date();
    SimpleDateFormat sdf = new SimpleDateFormat("MM/dd/yy");
    String strDate = sdf.format(date);
    System.out.println("formatted date in mm/dd/yy : " + strDate);
    sdf = new SimpleDateFormat("MM-dd-yyyy hh:mm:ss");
    strDate = sdf.format(date);
    System.out.println("formatted date in mm-dd-yyyy hh:mm:ss : " + strDate);
  }
}
```
