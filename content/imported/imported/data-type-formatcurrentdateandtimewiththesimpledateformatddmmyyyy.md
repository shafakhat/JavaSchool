---
title: Format current date and time with the SimpleDateFormat
nav: Format current date and ti...
description: SimpleDateFormat sdfDate = new SimpleDateFormat("dd/MM/yyyy");
section: Imported - java2s Archive
order: 1018
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/FormatcurrentdateandtimewiththeSimpleDateFormatddMMyyyy.htm
---
```java title=Example.java
import java.text.SimpleDateFormat;
import java.util.Date;

publicclass Main {

  publicstaticvoid main(String[] args) {
    SimpleDateFormat sdfDate = new SimpleDateFormat("dd/MM/yyyy");

    Date now = new Date();

    String strDate = sdfDate.format(now);

    System.out.println("Date: " + strDate);
  }
}
//Date: 18/02/2009
```
