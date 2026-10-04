---
title: Formatting a Date Using a Custom Format
nav: Formatting a Date Using a ...
description: Imported from the java2s.com archive: Formatting a Date Using a Custom Format
section: Imported - java2s Archive
order: 1023
source: https://web.archive.org/web/20100505183225/http://www.java2s.com:80/Tutorial/Java/0120__Development/FormattingaDateUsingaCustomFormat.htm
---
```java title=Example.java
import java.text.Format;
import java.text.SimpleDateFormat;
import java.util.Date;
public class Main {
  public static void main(String[] argv) throws Exception {
    Format formatter = new SimpleDateFormat("yy");
    String s = formatter.format(new Date());
    System.out.println(s);
  }
}
```
