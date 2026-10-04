---
title: Checking for a Leap Year
nav: Checking for a Leap Year
description: Imported from the java2s.com archive: Checking for a Leap Year
section: Imported - java2s Archive
order: 1002
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/CheckingforaLeapYearusingGregorianCalendar.htm
---
```java title=Example.java
import java.text.ParseException;
import java.util.GregorianCalendar;

publicclass MainClass {

  publicstaticvoid main(String[] args) throws ParseException {
    System.out.println(isLeapYear(2000));
  }

  publicstaticboolean isLeapYear(int year) {

    GregorianCalendar gcal = new GregorianCalendar();
    return gcal.isLeapYear(year);
  }

}
```
