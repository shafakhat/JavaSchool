---
title: Format year in yyyy format like 2007, 2008 etc.
nav: Format year in yyyy format...
description: System.out.println("Current year in yyyy format : " + sdf.format(date));
section: Imported
order: 20020
source: http://www.java2s.com:80/Tutorial/Java/0120__Development/Formatyearinyyyyformatlike20072008etc.htm
---
```java title=Example.java
import java.text.SimpleDateFormat;
import java.util.Date;
public class Main {
  public static void main(String[] args) {
    Date date = new Date();
    SimpleDateFormat sdf = new SimpleDateFormat("yyyy");
    System.out.println("Current year in yyyy format : " + sdf.format(date));
  }
}
//Current year in yyyy format : 2009
```
