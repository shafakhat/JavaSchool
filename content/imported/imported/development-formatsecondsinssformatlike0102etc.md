---
title: Format seconds in ss format like 01, 02 etc.
nav: Format seconds in ss forma...
description: System.out.println("seconds in ss format : " + sdf.format(date));
section: Imported
order: 20011
source: http://www.java2s.com:80/Tutorial/Java/0120__Development/Formatsecondsinssformatlike0102etc.htm
---
```java title=Example.java
import java.text.SimpleDateFormat;
import java.util.Date;
public class Main {
  public static void main(String[] args) {
    Date date = new Date();
    SimpleDateFormat sdf = new SimpleDateFormat("ss");
    System.out.println("seconds in ss format : " + sdf.format(date));
  }
}
//seconds in ss format : 14
```
