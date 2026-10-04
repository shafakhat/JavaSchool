---
title: Format year in yy format like 07, 08 etc
nav: Format year in yy format l...
description: System.out.println("Current year in yy format : " + sdf.format(date));
section: Imported - java2s Archive
order: 1027
source: https://web.archive.org/web/20100505183022/http://www.java2s.com:80/Tutorial/Java/0120__Development/Formatyearinyyformatlike0708etc.htm
---
```java title=Example.java
import java.text.SimpleDateFormat;
import java.util.Date;
public class Main {
  public static void main(String[] args) {
    Date date = new Date();
    SimpleDateFormat sdf = new SimpleDateFormat("yy");
    System.out.println("Current year in yy format : " + sdf.format(date));
  }
}
//Current year in yy format : 09
```
