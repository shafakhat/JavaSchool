---
title: Full length of month name
nav: Full length of month name
description: Imported from java2s.com: Full length of month name
section: Imported
order: 20023
source: http://www.java2s.com:80/Tutorial/Java/0120__Development/FulllengthofmonthnameSimpleDateFormatMMMM.htm
---
```java title=Example.java
import java.text.Format;
import java.text.SimpleDateFormat;
import java.util.Date;
public class Main {
  public static void main(String[] argv) throws Exception {
    Format formatter = new SimpleDateFormat("MMMM");
    String s = formatter.format(new Date());
    System.out.println(s);
  }
}
```
