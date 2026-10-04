---
title: new SimpleDateFormat('HH.mm.ss')
nav: new SimpleDateFormat('HH.m...
description: Imported from java2s.com: new SimpleDateFormat('HH.mm.ss')
section: Imported
order: 20067
source: http://www.java2s.com:80/Tutorial/Java/0120__Development/newSimpleDateFormatHHmmss.htm
---
```java title=Example.java
import java.text.Format;
import java.text.SimpleDateFormat;
import java.util.Date;
public class Main {
  public static void main(String[] argv) throws Exception {
    Format formatter = new SimpleDateFormat("HH.mm.ss");
    String s = formatter.format(new Date());
    System.out.println(s);
  }
}
```
