---
title: Convert Date into milliseconds example
nav: Convert Date into millisec...
description: System.out.println("Milliseconds since January 1, 1970, 00:00:00 GMT : " + date.getTime());
section: Imported - java2s Archive
order: 1012
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ConvertDateintomillisecondsexample.htm
---
```java title=Example.java
import java.util.Date;
publicclass Main {
  publicstaticvoid main(String args[]) {
    Date date = new Date();
    System.out.println("Date is : " + date);
    System.out.println("Milliseconds since January 1, 1970, 00:00:00 GMT : " + date.getTime());
  }
}
```
