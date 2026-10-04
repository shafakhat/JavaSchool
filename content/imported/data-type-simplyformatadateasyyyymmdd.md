---
title: Simply format a date as YYYYMMDD
nav: Simply format a date as YY...
description: System.out.println(gc.get(GregorianCalendar.YEAR) + (m < 10 ? "0" + mm : mm)
section: Imported - java2s Archive
order: 1009
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/SimplyformatadateasYYYYMMDD.htm
---
```java title=Example.java
import java.util.GregorianCalendar;
public class Main {
  public static void main(String[] argv) throws Exception {
    GregorianCalendar gc = new GregorianCalendar();
    gc.setLenient(false);
    gc.set(GregorianCalendar.YEAR, 2003);
    gc.set(GregorianCalendar.MONTH, 12);
    gc.set(GregorianCalendar.DATE, 1);
    int m = gc.get(GregorianCalendar.MONTH) + 1;
    int d = gc.get(GregorianCalendar.DATE);
    String mm = Integer.toString(m);
    String dd = Integer.toString(d);
    System.out.println(gc.get(GregorianCalendar.YEAR) + (m < 10 ? "0" + mm : mm)
        + (d < 10 ? "0" + dd : dd));
  }
}
```
