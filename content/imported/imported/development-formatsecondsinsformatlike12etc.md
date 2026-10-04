---
title: Format seconds in s format like 1,2 etc.
nav: Format seconds in s format...
description: System.out.println("seconds in s format : " + sdf.format(date));
section: Imported
order: 20008
source: http://www.java2s.com:80/Tutorial/Java/0120__Development/Formatsecondsinsformatlike12etc.htm
---
```java title=Example.java
import java.text.SimpleDateFormat;
import java.util.Date;
public class Main {
  public static void main(String[] args) {
    Date date = new Date();
    SimpleDateFormat sdf = new SimpleDateFormat("s");
    System.out.println("seconds in s format : " + sdf.format(date));
  }
}
//seconds in s format : 40
```
