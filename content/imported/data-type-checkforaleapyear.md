---
title: Check for a Leap Year
nav: Check for a Leap Year
description: Imported from the java2s.com archive: Check for a Leap Year
section: Imported - java2s Archive
order: 1009
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/CheckforaLeapYear.htm
---
```java title=Example.java
import java.text.ParseException;
publicclass MainClass {
  publicstaticvoid main(String[] args) throws ParseException {
    System.out.println(isLeapYear(2000));
  }
  publicstaticboolean isLeapYear(int year) {
    if (year < 0) {
      return false;
    }
    if (year % 400 == 0) {
      return true;
    } elseif (year % 100 == 0) {
      return false;
    } elseif (year % 4 == 0) {
      return true;
    } else {
      return false;
    }
  }
}
```
