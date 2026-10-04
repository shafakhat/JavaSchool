---
title: Formatting the Time Using a Custom Format
nav: Formatting the Time Using ...
description: Imported from the java2s.com archive: Formatting the Time Using a Custom Format
section: Imported - java2s Archive
order: 1239
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/FormattingtheTimeUsingaCustomFormat.htm
---
```java title=Example.java
import java.text.Format;
import java.text.SimpleDateFormat;
import java.util.Date;
public class Main {
  public static void main(String[] argv) throws Exception {
    // The hour (1-12)
    Format formatter = new SimpleDateFormat("h");
    String s = formatter.format(new Date());
    System.out.println(s);
  }
}
```
