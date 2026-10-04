---
title: Parse with a default format
nav: Parse with a default format
description: Date date = DateFormat.getTimeInstance(DateFormat.MEDIUM, Locale.CANADA).parse("21:44:07");
section: Imported - java2s Archive
order: 1126
source: https://web.archive.org/web/20140829090633/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Parsewithadefaultformat.htm
---
```java title=Example.java
import java.text.DateFormat;
import java.util.Date;
import java.util.Locale;
public class Main {
  public static void main(String[] argv) throws Exception {
    Date date = DateFormat.getTimeInstance(DateFormat.MEDIUM, Locale.CANADA).parse("21:44:07");
  }
}
```
