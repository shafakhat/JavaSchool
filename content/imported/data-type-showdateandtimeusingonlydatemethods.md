---
title: Show date and time using only Date methods.
nav: Show date and time using o...
description: System.out.println("Milliseconds since Jan. 1, 1970 GMT = " + msec);
section: Imported - java2s Archive
order: 1206
source: https://web.archive.org/web/2014/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ShowdateandtimeusingonlyDatemethods.htm
---
```java title=Example.java
import java.util.Date;
class DateDemo {
  public static void main(String args[]) {
    Date date = new Date();
    System.out.println(date);
    long msec = date.getTime();
    System.out.println("Milliseconds since Jan. 1, 1970 GMT = " + msec);
  }
}
```
