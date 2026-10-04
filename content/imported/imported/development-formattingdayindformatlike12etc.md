---
title: Formatting day in d format like 1,2 etc
nav: Formatting day in d format...
description: System.out.println("Current day in d format : " + sdf.format(date));
section: Imported
order: 20015
source: http://www.java2s.com:80/Tutorial/Java/0120__Development/Formattingdayindformatlike12etc.htm
---
```java title=Example.java
import java.text.SimpleDateFormat;
import java.util.Date;
public class Main {
  public static void main(String[] args) {
    Date date = new Date();
    String strDateFormat = "d";
    SimpleDateFormat sdf = new SimpleDateFormat(strDateFormat);
    System.out.println("Current day in d format : " + sdf.format(date));
  }
}
```
