---
title: Full day name
nav: Full day name
description: Imported from the java2s.com archive: Full day name
section: Imported - java2s Archive
order: 1029
source: https://web.archive.org/web/20100505183251/http://www.java2s.com:80/Tutorial/Java/0120__Development/FulldaynameSimpleDateFormatEEEE.htm
---
```java title=Example.java
import java.text.Format;
import java.text.SimpleDateFormat;
import java.util.Date;
public class Main {
  public static void main(String[] argv) throws Exception {
    Format formatter = new SimpleDateFormat("EEEE");
    String s = formatter.format(new Date());
    System.out.println(s);
  }
}
```
