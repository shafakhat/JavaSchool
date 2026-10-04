---
title: Formatting minute in m format like 1,2 etc.
nav: Formatting minute in m for...
description: System.out.println("minutes in m format : " + sdf.format(date));
section: Imported
order: 20016
source: http://www.java2s.com:80/Tutorial/Java/0120__Development/Formattingminuteinmformatlike12etc.htm
---
```java title=Example.java
import java.text.SimpleDateFormat;
import java.util.Date;
public class Main {
  public static void main(String[] args) {
    Date date = new Date();
    SimpleDateFormat sdf = new SimpleDateFormat("m");
    System.out.println("minutes in m format : " + sdf.format(date));
  }
}
//minutes in m format : 35
```
