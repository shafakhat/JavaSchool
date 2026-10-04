---
title: new SimpleDateFormat('HH
nav: new SimpleDateFormat('HH
description: Imported from java2s.com: new SimpleDateFormat('HH
section: Imported
order: 20065
source: http://www.java2s.com:80/Tutorial/Java/0120__Development/newSimpleDateFormatHHmmssZ.htm
---
```java title=Example.java
import java.text.Format;
import java.text.SimpleDateFormat;
import java.util.Date;
public class Main {
  public static void main(String[] argv) throws Exception {
    Format formatter = new SimpleDateFormat("HH:mm:ss Z");
    Date date = (Date) formatter.parseObject("22:14:02 -0500");
    System.out.println(date);
  }
}
```
