---
title: Formatting day of week in EEEE format like Sunday, Monday etc.
nav: Formatting day of week in ...
description: System.out.println("Current day of week in EEEE format : " + sdf.format(new Date()));
section: Imported
order: 20017
source: http://www.java2s.com:80/Tutorial/Java/0120__Development/FormattingdayofweekinEEEEformatlikeSundayMondayetc.htm
---
```java title=Example.java
import java.text.SimpleDateFormat;
import java.util.Date;
public class Main {
  public static void main(String[] args) {
    String strDateFormat = "EEEE";
    SimpleDateFormat sdf = new SimpleDateFormat(strDateFormat);
    System.out.println("Current day of week in EEEE format : " + sdf.format(new Date()));
  }
}
```
