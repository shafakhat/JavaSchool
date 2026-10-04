---
title: Create a java.util.Date Object from a Year, Month, Day Format
nav: Create a java.util.Date Ob...
description: public static void main(String[] args) throws ParseException {
section: Imported - java2s Archive
order: 1071
source: https://web.archive.org/web/20070319211920/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/CreateajavautilDateObjectfromaYearMonthDayFormat.htm
---
```java title=Example.java
import java.text.ParseException;
import java.text.SimpleDateFormat;
public class MainClass {
  public static void main(String[] args) throws ParseException {
    int year = 2003;
    int month = 12;
    int day = 12;
    String date = year + "/" + month + "/" + day;
    java.util.Date utilDate = null;
    try {
      SimpleDateFormat formatter = new SimpleDateFormat("yyyy/MM/dd");
      utilDate = formatter.parse(date);
      System.out.println("utilDate:" + utilDate);
    } catch (ParseException e) {
      System.out.println(e.toString());
      e.printStackTrace();
    }
  }
}
java title=Example.java
utilDate:Fri Dec 12 00:00:00 PST 2003
```
