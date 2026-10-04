---
title: Parse a date and time
nav: Parse a date and time
description: Format formatter = new SimpleDateFormat("yyyy.MM.dd.HH.mm.ss");
section: Imported - java2s Archive
order: 1040
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Parseadateandtime.htm
---
```java title=Example.java
import java.text.Format;
import java.text.SimpleDateFormat;
import java.util.Date;
publicclass Main {
  publicstaticvoid main(String[] argv) throws Exception {
    Format formatter = new SimpleDateFormat("yyyy.MM.dd.HH.mm.ss");
    Date date = (Date) formatter.parseObject("2002.01.29.08.36.33");
    System.out.println(date);
  }
}
```
