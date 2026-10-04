---
title: Parse string date value input with SimpleDateFormat('E, dd MMM yyyy HH
nav: Parse string date value in...
description: Format formatter = new SimpleDateFormat("E, dd MMM yyyy HH:mm:ss Z");
section: Imported - java2s Archive
order: 1045
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ParsestringdatevalueinputwithSimpleDateFormatEddMMMyyyyHHmmssZ.htm
---
```java title=Example.java
import java.text.Format;
import java.text.SimpleDateFormat;
import java.util.Date;
publicclass Main {
  publicstaticvoid main(String[] argv) throws Exception {
    Format formatter = new SimpleDateFormat("E, dd MMM yyyy HH:mm:ss Z");
    Date date = (Date) formatter.parseObject("Tue, 29 Jan 2004 21:14:02 -0500");
  }
}
```
