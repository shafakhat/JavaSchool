---
title: Display date with day name in a short format
nav: Display date with day name...
description: Imported from the java2s.com archive: Display date with day name in a short format
section: Imported - java2s Archive
order: 1081
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Displaydatewithdaynameinashortformat.htm
---
```java title=Example.java
import java.text.Format;
import java.text.SimpleDateFormat;
import java.util.Date;
public class Main {
  public static void main(String[] argv) throws Exception {
    Format formatter = new SimpleDateFormat("EEE, dd/MM/yyyy");
    String today = formatter.format(new Date());
    System.out.println("Today : " + today);
  }
}
```
