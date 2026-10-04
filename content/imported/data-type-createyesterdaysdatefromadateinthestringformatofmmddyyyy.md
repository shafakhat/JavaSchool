---
title: Create Yesterday's Date from a Date in the String Format of MM/DD/YYYY
nav: Create Yesterday's Date fr...
description: public static void main(String[] args) throws ParseException {
section: Imported - java2s Archive
order: 1074
source: https://web.archive.org/web/20070319212953/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/CreateYesterdaysDatefromaDateintheStringFormatofMMDDYYYY.htm
---
```java title=Example.java
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.GregorianCalendar;
public class MainClass {
  public static void main(String[] args) throws ParseException {
    SimpleDateFormat sdf = new SimpleDateFormat("MM/dd/yyyy");
    GregorianCalendar gc = new GregorianCalendar();
    java.util.Date d = sdf.parse("12/12/2003");
    gc.setTime(d);
    System.out.println("Input Date = " + sdf.format(d));
    int dayBefore = gc.get(Calendar.DAY_OF_YEAR);
    gc.roll(Calendar.DAY_OF_YEAR, -1);
    int dayAfter = gc.get(Calendar.DAY_OF_YEAR);
    if(dayAfter > dayBefore) {
        gc.roll(Calendar.YEAR, -1);
    }
    gc.get(Calendar.DATE);
    java.util.Date yesterday = gc.getTime();
    System.out.println("Yesterdays Date = " + sdf.format(yesterday));
  }
}
```

```java title=Example.java
Input Date = 12/12/2003
Yesterdays Date = 12/11/2003
```
