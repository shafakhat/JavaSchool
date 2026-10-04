---
title: new SimpleDateFormat('z')
nav: new SimpleDateFormat('z')
description: Imported from java2s.com: new SimpleDateFormat('z')
section: Imported
order: 20071
source: http://www.java2s.com:80/Tutorial/Java/0120__Development/newSimpleDateFormatzThetimezone.htm
---
```java title=Example.java
import java.text.Format;
import java.text.SimpleDateFormat;
import java.util.Date;
public class Main {
  public static void main(String[] argv) throws Exception {
    Format formatter = new SimpleDateFormat("z");
    String s = formatter.format(new Date());
    System.out.println(s);
  }
}
```
