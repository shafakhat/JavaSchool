---
title: new SimpleDateFormat('ss')
nav: new SimpleDateFormat('ss')
description: Imported from java2s.com: new SimpleDateFormat('ss')
section: Imported
order: 20068
source: http://www.java2s.com:80/Tutorial/Java/0120__Development/newSimpleDateFormatss.htm
---
```java title=Example.java
import java.text.Format;
import java.text.SimpleDateFormat;
import java.util.Date;
public class Main {
  public static void main(String[] argv) throws Exception {
    Format formatter = new SimpleDateFormat("ss");
    String s = formatter.format(new Date());
    System.out.println(s);
  }
}
```
