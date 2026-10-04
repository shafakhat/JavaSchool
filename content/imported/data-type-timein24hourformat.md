---
title: Time in 24-hour format
nav: Time in 24-hour format
description: Imported from the java2s.com archive: Time in 24-hour format
section: Imported - java2s Archive
order: 1056
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Timein24hourformat.htm
---
```java title=Example.java
import java.text.SimpleDateFormat;
import java.util.Date;
publicclass Main {
  publicstaticvoid main(String[] argv) throws Exception {
    Date date = new Date();
    SimpleDateFormat simpDate;
    simpDate = new SimpleDateFormat("kk:mm:ss");
    System.out.println(simpDate.format(date));
  }
}
```
