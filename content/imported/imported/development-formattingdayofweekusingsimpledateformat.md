---
title: Formatting day of week using SimpleDateFormat
nav: Formatting day of week usi...
description: System.out.println("Current day of week in E format : " + sdf.format(date));
section: Imported
order: 20018
source: http://www.java2s.com:80/Tutorial/Java/0120__Development/FormattingdayofweekusingSimpleDateFormat.htm
---
```java title=Example.java
//Formatting day of week in E format like Sun, Mon etc.
import java.text.SimpleDateFormat;
import java.util.Date;
public class Main {
  public static void main(String[] args) {
    Date date = new Date();
    String strDateFormat = "E";
    SimpleDateFormat sdf = new SimpleDateFormat(strDateFormat);
    System.out.println("Current day of week in E format : " + sdf.format(date));
  }
}
```
