---
title: Fix Line Separator
nav: Fix Line Separator
description: public static String fixLineSeparator(String xml) throws UnsupportedEncodingException {
section: Imported - java2s Archive
order: 1006
source: https://web.archive.org/web/20100412210702/http://java2s.com:80/Tutorial/Java/0040__Data-Type/FixLineSeparator.htm
---
```java title=Example.java
import java.io.UnsupportedEncodingException;
public class Utils {
  public static String fixLineSeparator(String xml) throws UnsupportedEncodingException {
    if ("\r\n".equals(System.getProperty("line.separator"))) {
      xml = xml.replaceAll("\r[^\n]", System.getProperty("line.separator"));
    } else {
      xml = xml.replaceAll("\r\n", System.getProperty("line.separator"));
    }
    return xml;
  }
}
```
