---
title: new SimpleDateFormat('zzzz')
nav: new SimpleDateFormat('zzzz')
description: Imported from java2s.com: new SimpleDateFormat('zzzz')
section: Imported
order: 20069
source: http://www.java2s.com:80/Tutorial/Java/0120__Development/newSimpleDateFormatzzzz.htm
---
```java title=Example.java
import java.text.Format;
import java.text.SimpleDateFormat;
import java.util.Date;
public class Main {
  public static void main(String[] argv) throws Exception {
    Format formatter = new SimpleDateFormat("zzzz");
    String s = formatter.format(new Date());
    System.out.println(s);
  }
}
```
