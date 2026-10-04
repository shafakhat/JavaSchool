---
title: Parsing the Time Using a Custom Format
nav: Parsing the Time Using a C...
description: Imported from the java2s.com archive: Parsing the Time Using a Custom Format
section: Imported - java2s Archive
order: 1225
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ParsingtheTimeUsingaCustomFormat.htm
---
```java title=Example.java
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;
public class Main {
  public static void main(String[] argv) throws Exception {
    DateFormat formatter = new SimpleDateFormat("hh.mm.ss a");
    Date date = (Date) formatter.parse("02.47.44 PM");
    System.out.println(date);
  }
}
```
