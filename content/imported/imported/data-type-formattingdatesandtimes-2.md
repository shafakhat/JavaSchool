---
title: Formatting Dates and Times
nav: Formatting Dates and Times
description: DateFormat fmt = DateFormat.getDateTimeInstance(DateFormat.FULL,
section: Imported - java2s Archive
order: 1012
source: https://web.archive.org/web/20070326194453/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/FormattingDatesandTimes.htm
---
```java title=Example.java
import java.text.DateFormat;
import java.util.Date;
import java.util.Locale;
public class MainClass {
  public static void main(String[] args) {
    Date today = new Date();
    DateFormat fmt = DateFormat.getDateTimeInstance(DateFormat.FULL,
                                                           DateFormat.FULL, Locale.US);
    String formatted = fmt.format(today);
    System.out.println(formatted);
  }
}
```

```java title=Example.java

Tuesday, January 16, 2007 10:03:23 AM PST
```
