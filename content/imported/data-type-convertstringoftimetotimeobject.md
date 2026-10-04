---
title: Convert string of time to time object
nav: Convert string of time to ...
description: Imported from the java2s.com archive: Convert string of time to time object
section: Imported - java2s Archive
order: 1010
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Convertstringoftimetotimeobject.htm
---
```java title=Example.java
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;
public class Main {
  public static void main(String[] args) throws Exception {
    String time = "15:30:18";
    DateFormat sdf = new SimpleDateFormat("hh:mm:ss");
    Date date = sdf.parse(time);
    System.out.println("Date and Time: " + date);
  }
}
```
