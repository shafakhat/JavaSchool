---
title: Format Month in MM format like 01, 02 etc.
nav: Format Month in MM format ...
description: System.out.println("Current Month in MM format : " + sdf.format(date)); }
section: Imported - java2s Archive
order: 1018
source: https://web.archive.org/web/20100505183138/http://www.java2s.com:80/Tutorial/Java/0120__Development/FormatMonthinMMformatlike0102etc.htm
---
```java title=Example.java
import java.text.SimpleDateFormat;
import java.util.Date;
public class Main {
  public static void main(String[] args) {
    Date date = new Date();
    SimpleDateFormat  sdf = new SimpleDateFormat("MM");
    System.out.println("Current Month in MM format : " + sdf.format(date));  }
}
//Current Month in M format : 02
```
