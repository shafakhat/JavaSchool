---
title: Formatting a Date Using a Custom Format
nav: Formatting a Date Using a ...
description: Imported from java2s.com: Formatting a Date Using a Custom Format
section: Imported
order: 20013
source: http://www.java2s.com:80/Tutorial/Java/0120__Development/FormattingaDateUsingaCustomFormat.htm
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
