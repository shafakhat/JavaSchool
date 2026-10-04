---
title: Format date in dd/mm/yyyy format
nav: Format date in dd/mm/yyyy ...
description: System.out.println("formatted date in mm/dd/yy : " + strDate);
section: Imported
order: 20002
source: http://www.java2s.com:80/Tutorial/Java/0120__Development/Formatdateinddmmyyyyformat.htm
---
```java title=Example.java
import java.util.Date;
import java.text.SimpleDateFormat;
public class Main {
  public static void main(String[] args) {
    Date date = new Date();
    SimpleDateFormat sdf = new SimpleDateFormat("MM/dd/yy");
    String strDate = sdf.format(date);
    System.out.println("formatted date in mm/dd/yy : " + strDate);
    sdf = new SimpleDateFormat("dd/MM/yyyy");
    strDate = sdf.format(date);
    System.out.println("formatted date in dd/MM/yyyy : " + strDate);
  }
}
```
