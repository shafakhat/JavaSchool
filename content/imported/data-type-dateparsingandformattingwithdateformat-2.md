---
title: Date Parsing and Formatting with DateFormat
nav: Date Parsing and Formattin...
description: DateFormat shortDf = DateFormat.getDateInstance(DateFormat.SHORT);
section: Imported - java2s Archive
order: 1032
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/DateParsingandFormattingwithDateFormat.htm
---
- DateFormat supports styles or patterns.
- There are four styles you can format a Date object to.
- Each style is represented by an int value.
- The four int fields that represent the styles are:

Value  Example
---  ---
DateFormat.SHORT.  For example, 12/2/05
DateFormat.MEDIUM.  For example, Dec 2, 2005.
DateFormat.LONG.  For example, December 2, 2005
DateFormat.FULL.  For example, Friday, December 2, 2005

```java title=Example.java
import java.text.DateFormat;
import java.text.ParseException;
import java.util.Date;
publicclass MainClass {
  publicstaticvoid main(String[] args) {
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
      Date date = shortDf.parse("12/12/2006");
    } catch (ParseException e) {
    }
  }
}
```

```java title=Example.java
1/26/07
Jan 26, 2007
January 26, 2007
Friday, January 26, 2007
```
