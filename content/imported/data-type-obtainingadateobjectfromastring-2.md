---
title: Obtaining a Date Object From a String
nav: Obtaining a Date Object Fr...
description: DateFormat fmt = DateFormat.getDateInstance(DateFormat.FULL, Locale.US);
section: Imported - java2s Archive
order: 1034
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ObtainingaDateObjectFromaString.htm
---
```java title=Example.java
import java.text.DateFormat;
import java.util.Date;
import java.util.Locale;
publicclass MainClass {
  publicstaticvoid main(String[] a) {
    Date aDate;
    DateFormat fmt = DateFormat.getDateInstance(DateFormat.FULL, Locale.US);
    try {
      aDate = fmt.parse("Saturday, July 4, 1998 ");
      System.out.println("The Date string is: " + fmt.format(aDate));
    } catch (java.text.ParseException e) {
      System.out.println(e);
    }
  }
}
java title=Example.java
The Date string is: Saturday, July 4, 1998
```
