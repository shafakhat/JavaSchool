---
title: Change date formatting symbols
nav: Change date formatting sym...
description: String[] newMonths = { "JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT",
section: Imported - java2s Archive
order: 1011
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Changedateformattingsymbols.htm
---
```java title=Example.java
import java.text.SimpleDateFormat;
import java.text.DateFormat;
import java.text.DateFormatSymbols;
import java.util.Date;
publicclass Main {
  publicstaticvoid main(String[] args) {
    String[] newMonths = { "JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT",
        "NOV", "DEC" };
    String[] newShortMonths = { "jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep",
        "oct", "nov", "dec" };
    String[] newWeekdays = { "", "Monday", "Tuesday", "Webnesday", "Thursday", "Friday",
        "Saturaday", "Sunday" };
    String[] shortWeekdays = { "", "monday", "tuesday", "webnesday", "thursday", "friday",
        "saturaday", "sunday" };
    DateFormatSymbols symbols = new DateFormatSymbols();
    symbols.setMonths(newMonths);
    symbols.setShortMonths(newShortMonths);
    symbols.setWeekdays(newWeekdays);
    symbols.setShortWeekdays(shortWeekdays);
    DateFormat format = new SimpleDateFormat("dd MMMM yyyy", symbols);
    System.out.println(format.format(new Date()));
    format = new SimpleDateFormat("dd MMM yyyy", symbols);
    System.out.println(format.format(new Date()));
    format = new SimpleDateFormat("EEEE, dd MMM yyyy", symbols);
    System.out.println(format.format(new Date()));
    format = new SimpleDateFormat("E, dd MMM yyyy", symbols);
    System.out.println(format.format(new Date()));
  }
}
```
