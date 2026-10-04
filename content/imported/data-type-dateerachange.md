---
title: Date Era change
nav: Date Era change
description: Imported from the java2s.com archive: Date Era change
section: Imported - java2s Archive
order: 1240
source: https://web.archive.org/web/2014/http://www.java2s.com/Tutorial/Java/0040__Data-Type/DateErachange.htm
---
```java title=Example.java
import java.text.DateFormatSymbols;
import java.text.SimpleDateFormat;
import java.util.Date;
public class ChangeEra {
  public static void main(String s[]) {
    SimpleDateFormat sdf = new SimpleDateFormat();
    DateFormatSymbols dfs = sdf.getDateFormatSymbols();
    String era[] = { "BCE", "CE" };
    dfs.setEras(era);
    sdf.setDateFormatSymbols(dfs);
    sdf.applyPattern("MMMM d yyyy G");
    System.out.println(sdf.format(new Date()));
  }
}
```
