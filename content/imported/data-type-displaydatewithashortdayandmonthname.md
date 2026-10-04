---
title: Display date with a short day and month name
nav: Display date with a short ...
description: Imported from the java2s.com archive: Display date with a short day and month name
section: Imported - java2s Archive
order: 1081
source: https://web.archive.org/web/20140128033401/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Displaydatewithashortdayandmonthname.htm
---
```java title=Example.java
import java.text.Format;
import java.text.SimpleDateFormat;
import java.util.Date;
public class Main {
  public static void main(String[] argv) throws Exception {
    Format formatter = new SimpleDateFormat("EEE, dd MMM yyyy");
    String today = formatter.format(new Date());
    System.out.println("Today : " + today);
  }
}
```
