---
title: Format month in M format like 1,2 etc
nav: Format month in M format l...
description: System.out.println("Current Month in M format : " + sdf.format(date));
section: Imported - java2s Archive
order: 1017
source: https://web.archive.org/web/20100505183218/http://www.java2s.com:80/Tutorial/Java/0120__Development/FormatmonthinMformatlike12etc.htm
---
```java title=Example.java
import java.text.SimpleDateFormat;
import java.util.Date;
public class Main {
  public static void main(String[] args) {
    Date date = new Date();
    SimpleDateFormat sdf = new SimpleDateFormat("M");
    System.out.println("Current Month in M format : " + sdf.format(date));
  }
}
//Current Month in M format : 2
```
