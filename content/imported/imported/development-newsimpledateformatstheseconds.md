---
title: new SimpleDateFormat('s')
nav: new SimpleDateFormat('s')
description: Imported from java2s.com: new SimpleDateFormat('s')
section: Imported
order: 20072
source: http://www.java2s.com:80/Tutorial/Java/0120__Development/newSimpleDateFormatsTheseconds.htm
---
```java title=Example.java
import java.text.Format;
import java.text.SimpleDateFormat;
import java.util.Date;
public class Main {
  public static void main(String[] argv) throws Exception {
    Format formatter = new SimpleDateFormat("s");
    String s = formatter.format(new Date());
    System.out.println(s);
  }
}
```
