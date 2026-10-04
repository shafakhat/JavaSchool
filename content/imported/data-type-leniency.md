---
title: Leniency
nav: Leniency
description: Leniency refers to whether or not a strict rule will be applied at parsing. If a DateFormat object is lenient, it will accept Jan 32, 2005. In fact, it will take the libe
section: Imported - java2s Archive
order: 1152
source: https://web.archive.org/web/20070319212002/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/Leniency.htm
---
Leniency refers to whether or not a strict rule will be applied at parsing. If a DateFormat object is lenient, it will accept Jan 32, 2005. In fact, it will take the liberty of converting it to Feb 1, 2006. By default, a DateFormat object is lenient.

```java title=Example.java
import java.text.DateFormat;
import java.text.ParseException;
import java.util.Date;
public class MainClass {
  public static void main(String[] args) {
    DateFormat shortDf = DateFormat.getDateInstance(DateFormat.SHORT);
    DateFormat mediumDf = DateFormat.getDateInstance(DateFormat.MEDIUM);
    DateFormat longDf = DateFormat.getDateInstance(DateFormat.LONG);
    DateFormat fullDf = DateFormat.getDateInstance(DateFormat.FULL);
    System.out.println(shortDf.format(new Date()));
    System.out.println(mediumDf.format(new Date()));
    System.out.println(longDf.format(new Date()));
    System.out.println(fullDf.format(new Date()));
    // parsing
    try {
      Date date = shortDf.parse("Jan 32, 2005");
    } catch (ParseException e) {
    }
  }
}
java title=Example.java
1/26/07
Jan 26, 2007
January 26, 2007
Friday, January 26, 2007
```
