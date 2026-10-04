---
title: Fix Line Separator
nav: Fix Line Separator
description: publicstatic String fixLineSeparator(String xml) throws UnsupportedEncodingException {
section: Imported - java2s Archive
order: 1029
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/FixLineSeparator.htm
---
```java title=Example.java
import java.io.UnsupportedEncodingException;
publicclass Utils {
  publicstatic String fixLineSeparator(String xml) throws UnsupportedEncodingException {
    if ("\r\n".equals(System.getProperty("line.separator"))) {
      xml = xml.replaceAll("\r[^\n]", System.getProperty("line.separator"));
    } else {
      xml = xml.replaceAll("\r\n", System.getProperty("line.separator"));
    }
    return xml;
  }
}
```
