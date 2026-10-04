---
title: Format a date into dd/mm/yyyy
nav: Format a date into dd/mm/y...
description: Imported from the java2s.com archive: Format a date into dd/mm/yyyy
section: Imported - java2s Archive
order: 1037
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Formatadateintoddmmyyyy.htm
---
```java title=Example.java
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;
publicclass Main {
  publicstaticvoid main(String[] args) {
    Date date = Calendar.getInstance().getTime();
    // Display a date in day, month, year format
    DateFormat formatter = new SimpleDateFormat("dd/MM/yyyy");
    String today = formatter.format(date);
    System.out.println("Today : " + today);
  }
}
```
