---
title: Change multiple components at the same time
nav: Change multiple components...
description: public void set (int year, int month, int date, int hour, int minute, int second)
section: Imported - java2s Archive
order: 1210
source: https://web.archive.org/web/2018/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Changemultiplecomponentsatthesametime.htm
---
```java title=Example.java
public void set (int year, int month, int date)
     public void set (int year, int month, int date, int hour, int minute, int second)
java title=Example.java
import java.util.Calendar;
public class MainClass {
  public static void main(String[] args) {
    Calendar calendar = Calendar.getInstance();
    calendar.set(2001, 1, 1);
  }
}
```
