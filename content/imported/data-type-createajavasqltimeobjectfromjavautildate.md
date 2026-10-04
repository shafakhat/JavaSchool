---
title: Create a java.sql.Time Object from java.util.Date
nav: Create a java.sql.Time Obj...
description: java.sql.Time descends from java.util.Date but uses only the hour, minute, and second values.
section: Imported - java2s Archive
order: 1070
source: https://web.archive.org/web/20070324082128/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/CreateajavasqlTimeObjectfromjavautilDate.htm
---
java.sql.Time descends from java.util.Date but uses only the hour, minute, and second values.

```java title=Example.java
import java.text.ParseException;
import java.util.Date;
public class MainClass {
  public static void main(String[] args) throws ParseException {
    new java.sql.Time(new Date().getTime());
  }
}
```
