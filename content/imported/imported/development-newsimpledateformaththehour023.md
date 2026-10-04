---
title: new SimpleDateFormat('H') // The hour (0-23)
nav: new SimpleDateFormat('H') ...
description: Imported from java2s.com: new SimpleDateFormat('H') // The hour (0-23)
section: Imported
order: 20066
source: http://www.java2s.com:80/Tutorial/Java/0120__Development/newSimpleDateFormatHThehour023.htm
---
```java title=Example.java
import java.text.Format;
import java.text.SimpleDateFormat;
import java.util.Date;
public class Main {
  public static void main(String[] argv) throws Exception {
    Format formatter = new SimpleDateFormat("H");
    String s = formatter.format(new Date());
    System.out.println(s);
  }
}
```
